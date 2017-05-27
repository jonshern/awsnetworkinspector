from __future__ import print_function
import boto3

class Subnet:
    VpcId = ''
    AvailabilityZone = ''
    SubnetId = ''
    CidrBlock = ''
    AssignIpv6AddressOnCreation = ''
    State = ''

    def __init__(self, item):
        self.RawData = item


    def hydratefromitem(self):
        self.VpcId = self.RawData.get('VpcId')
        self.AvailabilityZone = self.RawData.get('AvailabilityZone')
        self.SubnetId = self.RawData.get('SubnetId')
        self.CidrBlock = self.RawData.get('CidrBlock')
        self.AssignIpv6AddressOnCreation = self.RawData.get('AssignIpv6AddressOnCreation')
        self.State = self.RawData.get('State')
        
    def prettyprint(self, character, offset):
        print (character * offset + '------------Subnet Object----------------------')
        print (character * offset + 'VpcId ' + str(self.VpcId))
        print (character * offset + 'SubnetId ' + str(self.SubnetId))
        print (character * offset + 'CidrBlock ' + str(self.CidrBlock))

    @staticmethod
    def loaddata(profilename):

        subnets = []

        dev = boto3.session.Session(profile_name=profilename)  
        client = boto3.client('ec2', verify=False)
        response = client.describe_subnets(
            DryRun=False
        )

        for item in response['Subnets']:
            subnet = Subnet(item)
            subnets.append(subnet)

        return subnets

    def dumpjson(self):
        print (self.RawData)    
