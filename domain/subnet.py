from __future__ import print_function
import boto3

class Subnet:
    # RawData = ''
    VpcId = ''
    AvailabilityZone = ''
    SubnetId = ''
    CidrBlock = ''
    AssignIpv6AddressOnCreation = ''
    State = ''

    def __init__(self, item):
        # self.RawData = item
        self.VpcId = item.get('VpcId')
        self.AvailabilityZone = item.get('AvailabilityZone')
        self.SubnetId = item.get('SubnetId')
        self.CidrBlock = item.get('CidrBlock')
        self.AssignIpv6AddressOnCreation = item.get('AssignIpv6AddressOnCreation')
        self.State = item.get('State')




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
