from __future__ import print_function
import sys
sys.path.append('domain/')
sys.path.append('helpers/')

import pickle
import os
import sys
import argparse
import boto3
from jinja2 import Environment, FileSystemLoader, Template
import datetime
import yaml

from elasticip import ElasticIp
from vpc import Vpc
from ec2 import EC2
from account import Account
from subnet import Subnet
from internetgateway import InternetGateway
from elasticloadbalancer import ElasticLoadBalancer


def main(args):
    
    accounts = []

    args = parser_args(sys.argv[1:])

    #if profile is specified use that.
    # otherwise use a yaml file  
    if args['profile'] == None:
        print ('No profile was specified, looking for a yaml file')
    # else:
    #     loadaccountyamlfile(args['accountyamlfilename'])


    filename = args['filename']
    
    for profilename in args['profile']:

        if args['dumpjson']:
            account = populateaccount(profilename)
            account.hydratefromitem()
            serializepickle(account,filename)
            account = deserializepickle(filename)
            account.dumpjson()
            

        if args['offline']:
            account = deserializepickle(filename)

        if args['createreport']:
            account = populateaccount(profilename)
            account.hydratefromitem()
            serializepickle(account,filename)
            account = deserializepickle(filename)
            data = apply_template(account)
            write_to_file(data, 'report.md')


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
        '-o', '--offline', help='Retrieve AWS Data from Local DB', action='store_true')

    parser.add_argument(
        '-r', '--createreport', help='Create Markdown Report', action='store_true')

    parser.add_argument(
        '-a', '--accountyamlfilename', help='Use markdown file for some account info', default='data/accounts.yaml')

    parser.add_argument(
        '-t', '--test', help='Test a command', action='store_true')

    parser.add_argument(
        '-d', '--dumpjson', help='Dump Json', action='store_true')

    parser.add_argument(
        '-ec', '--ec2', help='Get a list of the EC2 Instances', action='store_true')
    args = vars(parser.parse_args())

    return args



def testcommand(profilename):
    ElasticLoadBalancer.loaddata(profilename)

    


def getelasticips(profilename):
    
    eips = ElasticIp.loaddata(profilename)

    for eip in eips:
        eip.prettyprint()


def populateaccount(profilename):
    
    vpcs = Vpc.loaddata(profilename)
  
    eips = ElasticIp.loaddata(profilename)
    instances = EC2.loaddata(profilename)

    account = Account()
    account.profilename = profilename
    account.elasticips = eips
    account.instances = instances
    account.vpcs = vpcs

    subnets = Subnet.loaddata(profilename)
    account.subnets = subnets

    loadbalancers = ElasticLoadBalancer.loaddata(profilename)
    account.elasticloadbalancers = loadbalancers

    account.linksubnetstovpcs()

    # writetoyaml(account)

    

    return account


def serializepickle(account, filename):
    with open(filename, 'w') as outfile:
        pickle.dump(account, outfile)


def deserializepickle(filename):
    fileObject = open(filename,'r')  
    account = pickle.load(fileObject)  

    return account



def writetoyaml(account):
    stream = file('data/document.yaml', 'w')
    yaml.dump(account, stream)
    # print (yaml.dump(account)) 


def getec2list(profilename):
    
    instances = EC2.loaddata(profilename)
    for instance in instances:
        instance.prettyprint()

def apply_template(accountObject):
    env = Environment(loader = FileSystemLoader('templates'))
    template = env.get_template('awsreport.md')
    renderedtemplate = template.render(profilename='a profile name', account=accountObject)
    return renderedtemplate

def write_to_file(data_to_be_written, filename):
    f = open('data/' + filename,'w')
    f.write(data_to_be_written)
    f.close()






if __name__ == '__main__':
    main(sys.argv[1:])