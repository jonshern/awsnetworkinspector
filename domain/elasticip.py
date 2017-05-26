import boto3

class ElasticIp:
    NetworkInterfaceId = ''
    AssociationId = ''
    NetworkInterfaceOwnerId = ''
    PublicIp = ''
    AllocationId = ''
    PrivateIpAddress = ''
    

    def __init__(self, item):
        self.RawData = item



    def hydratefromitem(self):
        self.NetworkInterfaceId = self.RawData.get('NetworkInterfaceId')
        self.AssociationId = self.RawData.get('AssociationId')
        self.NetworkInterfaceOwnerId = self.RawData.get('NetworkInterfaceOwnerId')
        self.PublicIp = self.RawData.get('PublicIp')
        self.AllocationId = self.RawData.get('AllocationId')
        self.PrivateIpAddress = self.RawData.get('PrivateIpAddress')
    

    @staticmethod
    def loaddata(profilename):
        
        eips = []

        dev = boto3.session.Session(profile_name=profilename)  
        ec2 = boto3.client('ec2')
        filters = [
            {'Name': 'domain', 'Values': ['vpc']}
        ]
        response = ec2.describe_addresses(Filters=filters)
        
        items = response['Addresses']
        for item in items:
            eip = ElasticIp(item)
            eips.append(eip)

        return eips            
        
    def prettyprint(self):
        print ('----------------------------------')
        print ('Public IP ' + str(self.PublicIp))
        print ('Private IP ' + str(self.PrivateIpAddress))
