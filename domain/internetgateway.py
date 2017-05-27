from __future__ import print_function
import boto3
class InternetGatewayAttachment:
    State = ''
    VpcId = ''

class InternetGateway:
    RawData = ''
    InternetGatewayId = ''
    Attachments = []

    Name = ''
    VpcId = ''

    Attachments = []


    def __init__(self, item):
        self.RawData = item



    def hydratefromitem(self):
        self.InternetGatewayId = self.RawData.get('InternetGatewayId')


    @staticmethod
    def loaddata(profilename, region):

        subnets = []

        dev = boto3.session.Session(profile_name=profilename)  
        client = boto3.client('ec2', verify=False, region_name=region)
        response = client.describe_internet_gateways(
            DryRun=False
        )

        for item in response['InternetGateways']:
            print(item)

        

        # print (response)
    
    def dumpjson(self):
        print (self.RawData)    

