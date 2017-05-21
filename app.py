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
    id = ''
    cidr_block = ''
    dhcp_options_id = ''
    instance_tenancy = ''
    ipv6_cidr_block_association_set = ''
    is_default = ''
    state = ''
    tags = ''
    vpc_id = ''

    item = ''
    subnets = []
    securitygroups = []
    

    def __init__(self, item):
        self.item = item

    def printvpc(self):
        print (self.item)


class ElasticIp:
    NetworkInterfaceId = ''
    AssociationId = ''
    NetworkInterfaceOwnerId = ''
    PublicIp = ''
    AllocationId = ''
    PrivateIpAddress = ''

    def __init__(self, item):
        if 'NetworkInterfaceId' in item:
            self.NetworkInterfaceId = item['NetworkInterfaceId']

        if 'AssociationId' in item:
            self.AssociationId = item['AssociationId']

        if 'NetworkInterfaceOwnerId' in item:
            self.NetworkInterfaceOwnerId = item['NetworkInterfaceOwnerId']

        if 'PublicIp' in item:
            self.PublicIp = item['PublicIp']

        if 'AllocationId' in item:
            self.AllocationId = item['AllocationId']

        if 'PrivateIpAddress' in item:
            self.PrivateIpAddress = item['PrivateIpAddress']


    def printeip(self):
        print ('----------------------------------')
        print ('Public IP ' + self.PublicIp)
        print ('Private IP ' + self.PrivateIpAddress)


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
        '-p', '--profile', help='Set the Profile', default='')

    parser.add_argument(
        '-i', '--inspect', help='Initiate the inspection of the aws network', action='store_true')
    parser.add_argument(
        '-v', '--vpc', help='Get a list of the vpcs', action='store_true')
    parser.add_argument(
        '-e', '--elasticip', help='Get a list of the Elasic Ips', action='store_true')
    args = vars(parser.parse_args())



    profilename = args['profile']

    if args['inspect']:
        print 'Starting the inspection of the network'

    if args['vpc']:
        vpclist = getvpclist(profilename)
        for item in vpclist:
                print (item.printvpc())
        # print (str(item))

    if args['elasticip']:
        getelasticips(profilename)


def initializeaccountlist():
    accountlist = []


def getelasticips(profilename):

    dev = boto3.session.Session(profile_name=profilename)  
    ec2 = boto3.client('ec2')
    filters = [
        {'Name': 'domain', 'Values': ['vpc']}
    ]
    response = ec2.describe_addresses(Filters=filters)
    
    items = response['Addresses']
    for item in items:
        eip = ElasticIp(item)
        eip.printeip()
        # print (item)


def getvpclist(profilename):

    dev = boto3.session.Session(profile_name=profilename)  
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
        vpcobject = Vpc(item)
        vpcs.append(vpcobject)

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