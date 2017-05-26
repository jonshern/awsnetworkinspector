from __future__ import print_function
import sys
sys.path.append('domain/')
sys.path.append('helpers/')

import pickle
import os
import csv
import sys
import argparse
import boto3
from jinja2 import Environment, FileSystemLoader, Template
import datetime
import yaml
from tinydb import TinyDB, Query



from elasticip import ElasticIp
from vpc import Vpc
from ec2 import EC2
from account import Account
from subnet import Subnet
from internetgateway import InternetGateway


def main(args):
    
    db = TinyDB('awsinfra.json')
    
    args = parser_args(sys.argv[1:])


    if args['profile'] == None:
        print('At least one profile needs to be specified')
        exit

    filename = args['filename']
    
    for profilename in args['profile']:

        if args['synctodatabase']:
            account = populateaccount(profilename)
            account.hydratefromitem()
            serializepickle(account,filename)

        if args['retrievefromdatabase']:
            account = populateaccount(profilename)
            account.hydratefromitem()
            serializepickle(account,filename)

        

        if args['test']:
            testcommand(profilename)

            


def parser_args(args):
    parser = argparse.ArgumentParser(
    description='Inspect the network in AWS and create a report')


    parser.add_argument(
        '-p', '--profile', help='Set the Profile, this can specified many times.', action='append')

    parser.add_argument(
        '-f', '--filename', help='Set filename to save database', default='awsaccount.pickle')

    parser.add_argument(
        '-s', '--synctodatabase', help='Sync AWS Data to Local DB', action='store_true')

    parser.add_argument(
        '-r', '--retrievefromdatabase', help='Retrieve AWS Data from Local DB', action='store_true')


    # parser.add_argument(
    #     '-r', '--retrievefromdatabase', help='Retrieve AWS Data from Local DB', action='store_true')

    parser.add_argument(
        '-t', '--test', help='Test a command', action='store_true')


    parser.add_argument(
        '-ec', '--ec2', help='Get a list of the EC2 Instances', action='store_true')
    args = vars(parser.parse_args())

    return args



def testcommand(profilename):
    ig = InternetGateway.loaddata(profilename)

    


def getelasticips(profilename):
    
    eips = ElasticIp.loaddata(profilename)

    for eip in eips:
        eip.prettyprint()


def populateaccount(profilename):
    
    vpcs = Vpc.loaddata(profilename)
  
    eips = ElasticIp.loaddata(profilename)
    instances = EC2.loaddata(profilename)

    account = Account()
    account.elasticips = eips
    account.instances = instances
    account.vpcs = vpcs

    subnets = Subnet.loaddata(profilename)
    account.subnets = subnets

    account.linksubnetstovpcs()

    writetoyaml(account)

    

    return account


def serializepickle(account, filename):
    with open(filename, 'w') as outfile:
        pickle.dump(account, outfile)


def deserializepickle(account, filename):
    fileObject = open(filename,'r')  
    account = pickle.load(fileObject)  

    return account



def writetoyaml(account):
    stream = file('data/document.yaml', 'w')
    yaml.dump(account, stream)
    print (yaml.dump(account)) 


def getec2list(profilename):
    
    instances = EC2.loaddata(profilename)
    for instance in instances:
        instance.prettyprint()

# def apply_template(imagelist):
#     env = Environment(loader = FileSystemLoader('templates'))
#     template = env.get_template('awsreport.html')
#     renderedtemplate = template.render(images=imagelist)
#     return renderedtemplate

# def write_to_file(data_to_be_written, filename):
#     f = open(filename,'w')
#     f.write(data_to_be_written)
#     f.close()






if __name__ == '__main__':
    main(sys.argv[1:])