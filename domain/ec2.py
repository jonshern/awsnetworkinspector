from __future__ import print_function
import boto3

class EC2:
    PublicDnsName = ''
    PublicIpAddress = ''
    PrivateIpAddress = ''
    PublicIp = ''
    SubnetId = ''
    PrivateIpAddress = ''

    def __init__(self, item):
        self.RawData = item

    def hydratefromitem(self):
        self.PublicDnsName = self.RawData.get('PublicDnsName')
        self.PublicIpAddress = self.RawData.get('PublicIpAddress')
        self.PrivateIpAddress = self.RawData.get('PrivateIpAddress')
        self.SubnetId = self.RawData.get('SubnetId')
        self.PrivateIpAddress = self.RawData.get('PrivateIpAddress')

    def prettyprint(self):
        print ('----------------------------------')
        print ('Public DNS ' + str(self.PublicDnsName))
        print ('Public IP Address ' + str(self.PublicIpAddress))

    @staticmethod
    def loaddata(profilename):

        instances = []

        dev = boto3.session.Session(profile_name=profilename)  
        client = boto3.client('ec2', verify=False)
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