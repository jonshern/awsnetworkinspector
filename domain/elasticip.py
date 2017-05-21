import boto3

class ElasticIp:
    NetworkInterfaceId = ''
    AssociationId = ''
    NetworkInterfaceOwnerId = ''
    PublicIp = ''
    AllocationId = ''
    PrivateIpAddress = ''

    def __init__(self, item):
        self.NetworkInterfaceId = item.get('NetworkInterfaceId')
        self.AssociationId = item.get('AssociationId')
        self.NetworkInterfaceOwnerId = item.get('NetworkInterfaceOwnerId')
        self.PublicIp = item.get('PublicIp')
        self.AllocationId = item.get('AllocationId')
        self.PrivateIpAddress = item.get('PrivateIpAddress')
    

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
