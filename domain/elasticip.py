

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
    

    def prettyprint(self):
        print ('----------------------------------')
        print ('Public IP ' + str(self.PublicIp))
        print ('Private IP ' + str(self.PrivateIpAddress))
