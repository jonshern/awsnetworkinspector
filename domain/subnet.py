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
        self.VpcId = item.get('VpcId')
        self.AvailabilityZone = item.get('AvailabilityZone')
        self.SubnetId = item.get('SubnetId')
        self.CidrBlock = item.get('CidrBlock')
        self.AssignIpv6AddressOnCreation = item.get('AssignIpv6AddressOnCreation')
        self.State = item.get('State')


    def prettyprint(self):
        print ('----------------------------------')
        print ('VpcId ' + str(self.VpcId))
        print ('SubnetId ' + str(self.SubnetId))
        print ('CidrBlock ' + str(self.CidrBlock))

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
        
    def printeip(self):
        print ('----------------------------------')
        print ('Public IP ' + self.PublicIp)
        print ('Private IP ' + self.PrivateIpAddress)