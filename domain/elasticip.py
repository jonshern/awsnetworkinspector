

class ElasticIp:
    NetworkInterfaceId = ''
    AssociationId = ''
    NetworkInterfaceOwnerId = ''
    PublicIp = ''
    AllocationId = ''
    PrivateIpAddress = ''

    def __init__(self, item):
        if 'NetworkInterfaceId' in item:
            self.NetworkInterfaceId = item['NetworkInterfaceId']

        if 'AssociationId' in item:
            self.AssociationId = item['AssociationId']

        if 'NetworkInterfaceOwnerId' in item:
            self.NetworkInterfaceOwnerId = item['NetworkInterfaceOwnerId']

        if 'PublicIp' in item:
            self.PublicIp = item['PublicIp']

        if 'AllocationId' in item:
            self.AllocationId = item['AllocationId']

        if 'PrivateIpAddress' in item:
            self.PrivateIpAddress = item['PrivateIpAddress']


    def printeip(self):
        print ('----------------------------------')
        print ('Public IP ' + self.PublicIp)
        print ('Private IP ' + self.PrivateIpAddress)
