from __future__ import print_function
import boto3

class EC2:
    VpcId = ''
    PublicDnsName = ''
    PublicIpAddress = ''
    PrivateIpAddress = ''
    PublicIp = ''
    SubnetId = ''
    PrivateIpAddress = ''
    LaunchTime = ''
    ImageId = ''

    def __init__(self, item):
        self.RawData = item

    def hydratefromitem(self):
        self.PublicDnsName = self.RawData.get('PublicDnsName')
        self.PublicIpAddress = self.RawData.get('PublicIpAddress')
        self.PrivateIpAddress = self.RawData.get('PrivateIpAddress')
        self.SubnetId = self.RawData.get('SubnetId')
        self.PrivateIpAddress = self.RawData.get('PrivateIpAddress')
        self.LaunchTime = self.RawData.get('LaunchTime')
        self.VpcId = self.RawData.get('VpcId')
        self.ImageId = self.RawData.get('ImageId')


    def prettyprint(self):
        print ('----------------------------------')
        print ('Public DNS ' + str(self.PublicDnsName))
        print ('Public IP Address ' + str(self.PublicIpAddress))

    @staticmethod
    def loaddata(profilename, region):

        instances = []

        dev = boto3.session.Session(profile_name=profilename)  
        client = boto3.client('ec2', verify=False, region_name=region)
        response = client.describe_instances(
            DryRun=False,
            Filters=[
                {
                    'Name': 'instance-state-name',
                    'Values': [
                        'running',
                    ]
                },
            ]
        )
        
        for item in response['Reservations']:
            for subitem in item['Instances']:
                instance = EC2(subitem)
                instances.append(instance)
        return instances                 

    def printeip(self):
        print ('----------------------------------')
        print ('Public IP ' + self.PublicIp)
        print ('Private IP ' + self.PrivateIpAddress)

    def dumpjson(self):
        print (self.RawData)    