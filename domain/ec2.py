from __future__ import print_function
import boto3

class EC2:
    PublicDnsName = ''
    PublicIpAddress = ''
    PrivateIpAddress = ''
    PublicIp = ''
    SubnetId = ''
    PrivateIpAddress = ''
    RawData = ''

    def __init__(self, item):
        self.PublicDnsName = item.get('PublicDnsName')
        self.PublicIpAddress = item.get('PublicIpAddress')
        self.PrivateIpAddress = item.get('PrivateIpAddress')
        self.SubnetId = item.get('SubnetId')
        self.PrivateIpAddress = item.get('PrivateIpAddress')
        self.RawData = item

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