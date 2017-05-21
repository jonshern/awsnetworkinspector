from __future__ import print_function
import sys
sys.path.append('domain/')


import json
import os
import csv
import sys
import argparse
import boto3
from jinja2 import Environment, FileSystemLoader, Template
import datetime


from elasticip import ElasticIp
from vpc import Vpc
from ec2 import EC2
from account import Account


    
class InternetGateway:
    def __init__(self, **entries):
        self.__dict__.update(entries)

class VpnGateway:
    def __init__(self, **entries):
        self.__dict__.update(entries)  





class Subnet:
    def __init__(self, **entries):
        self.__dict__.update(entries)

class SecurityGroup:
    def __init__(self, **entries):
        self.__dict__.update(entries)
            



def main():
    
    parser = argparse.ArgumentParser(
        description='Inspect the network in AWS and create a report')

    parser.add_argument(
        '-p', '--profile', help='Set the Profile', default='')

    parser.add_argument(
        '-i', '--inspect', help='Initiate the inspection of the aws network', action='store_true')

    parser.add_argument(
        '-v', '--vpc', help='Get a list of the vpcs', action='store_true')
    parser.add_argument(
        '-e', '--elasticip', help='Get a list of the Elasic Ips', action='store_true')

    parser.add_argument(
        '-ec', '--ec2', help='Get a list of the EC2 Instances', action='store_true')
    args = vars(parser.parse_args())



    profilename = args['profile']

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
    
    if args['ec2']:
        getec2list(profilename)

    
def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), default=json_serial, sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, default=json_serial, sort_keys=sort, indent=indents))
    return None



def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable")



def initializeaccountlist():
    accountlist = []



def getelasticips(profilename):
    
    eips = ElasticIp.loaddata(profilename)

    for eip in eips:
        eip.prettyprint()


def populateaccount(profilename):
  
    eips = ElasticIp.loaddata(profilename)
    instances = EC2.loaddata(profilename)

    vpcs = Vpc.loaddata(profilename)
    
    account = Account(eips,instances)
    account.vpcs = vpcs
      
    return account





def getec2list(profilename):
    
    instances = EC2.loaddata(profilename)
    for instance in instances:
        instance.prettyprint()

def apply_template(imagelist):
    env = Environment(loader = FileSystemLoader('templates'))
    template = env.get_template('awsreport.html')
    renderedtemplate = template.render(images=imagelist)
    return renderedtemplate

def write_to_file(data_to_be_written, filename):
    f = open(filename,'w')
    f.write(data_to_be_written)
    f.close()






if __name__ == '__main__':
    main()