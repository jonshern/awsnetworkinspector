import json
import os
import csv
import sys
import argparse
import boto3
from jinja2 import Environment, FileSystemLoader, Template


class Account:
    name = ''
    id = ''
    vpcs = []

    def __init__(self, **entries):
        self.__dict__.update(entries)
    
class InternetGateway:
    def __init__(self, **entries):
        self.__dict__.update(entries)

class VpnGateway:
    def __init__(self, **entries):
        self.__dict__.update(entries)  

class Vpc:
    Subnets = []

    def __init__(self, **entries):
        self.__dict__.update(entries)

class Subnet:
    def __init__(self, **entries):
        self.__dict__.update(entries)

class SecurityGroup:
    def __init__(self, **entries):
        self.__dict__.update(entries)
    
class Ec2:    
    SecurityGroups = []
    def __init__(self, **entries):
        self.__dict__.update(entries)
            



def main():
    

    parser = argparse.ArgumentParser(
        description='Inspect the network in AWS and create a report')
    parser.add_argument(
        '-i', '--inspect', help='Initiate the inspection of the aws network', action='store_true')
    args = vars(parser.parse_args())

    vpclist = getvpclist()

    if args['inspect']:
        print 'Starting the inspection of the network'



def initializeaccountlist():
    accountlist = []


    

def getvpclist():
    """Get a list of all of the vpcs for a given aws account"""
    client = boto3.client('ec2', verify=False)
    response = client.describe_vpcs(
    DryRun=False,
        Filters=[
            {
                'Name': 'state',
                'Values': [
                    'available',
                ]
            },
        ]
    )

    items = response['Vpcs']

    vpcs = []
    firstitem = items[0]
    seconditem = items[1]
    for item in items:
        vpcobject = AWSVPC(item)
        vpcs.append(vpcobject)

    # items = response['Vpcs']

    return vpcs

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