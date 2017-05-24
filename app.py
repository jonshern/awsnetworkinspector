from __future__ import print_function
import sys
sys.path.append('domain/')
sys.path.append('helpers/')

import json
import os
import csv
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


def main(args):
    
    args = parser_args(sys.argv[1:])


    if args['profile'] == None:
        print('At least one profile needs to be specified')
        exit

    
    for profilename in args['profile']:


        if args['inspect']:
            print('Starting the inspection of the network')
            account = populateaccount(profilename)

            account.prettyprint()

        if args['vpc']:
            vpclist = getvpclist(profilename)
            for item in vpclist:
                    print (item.prettyprint())
            # print (str(item))

        if args['elasticip']:
            getelasticips(profilename)
        
        if args['subnet']:
            subnets = Subnet.loaddata(profilename)
            for item in subnets:
                item.prettyprint()

        
        if args['ec2']:
            getec2list(profilename)


def parser_args(args):
    parser = argparse.ArgumentParser(
    description='Inspect the network in AWS and create a report')


    parser.add_argument(
        '-p', '--profile', help='Set the Profile, this can specified many times.', action='append')

    parser.add_argument(
        '-i', '--inspect', help='Initiate the inspection of the aws network', action='store_true')

    parser.add_argument(
        '-v', '--vpc', help='Get a list of the vpcs', action='store_true')
    parser.add_argument(
        '-e', '--elasticip', help='Get a list of the Elasic Ips', action='store_true')
    parser.add_argument(
        '-s', '--subnet', help='Get a list of the subnets', action='store_true')


    parser.add_argument(
        '-ec', '--ec2', help='Get a list of the EC2 Instances', action='store_true')
    args = vars(parser.parse_args())

    return args




def getelasticips(profilename):
    
    eips = ElasticIp.loaddata(profilename)

    for eip in eips:
        eip.prettyprint()


def populateaccount(profilename):
    
    vpcs = Vpc.loaddata(profilename)
  
    eips = ElasticIp.loaddata(profilename)
    instances = EC2.loaddata(profilename)


    
    account = Account(eips,instances)
    account.vpcs = vpcs

    subnets = Subnet.loaddata(profilename)
    account.subnets = subnets

    account.linksubnetstovpcs()

    writetoyaml(account)

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