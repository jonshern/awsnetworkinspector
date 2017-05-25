from __future__ import print_function
import boto3

class InternetGateway:
    # RawData = ''
    InternetGatewayId = ''
    Name = ''
    Attachments = []


    def __init__(self, item):
        # self.RawData = item
        self.InternetGatewayId = item.get('InternetGatewayId')




    # def prettyprint(self, character, offset):
    #     print (character * offset + '------------Subnet Object----------------------')
    #     print (character * offset + 'VpcId ' + str(self.VpcId))
    #     print (character * offset + 'SubnetId ' + str(self.SubnetId))
    #     print (character * offset + 'CidrBlock ' + str(self.CidrBlock))

    @staticmethod
    def loaddata(profilename):

        subnets = []

        dev = boto3.session.Session(profile_name=profilename)  
        client = boto3.client('ec2', verify=False)
        response = client.describe_internet_gateways(
            DryRun=False
        )

        for item in response['InternetGateways']:
            print(item)

        # print (response)

