
import boto3

class Vpc:
    VpcId = ''
    DhcpOptionsId = ''
    CidrBlock = ''
    IsDefault = ''
    subnets = []


    def __init__(self, item):
        self.RawData = item


    def hydratefromitem(self):
        self.VpcId = self.RawData.get('VpcId')
        self.DhcpOptionsId = self.RawData.get('DhcpOptionsId')
        self.CidrBlock = self.RawData.get('CidrBlock')
        self.IsDefault = self.RawData.get('IsDefault')
        self.subnets = []


    @staticmethod    
    def loaddata(profilename):
        dev = boto3.session.Session(profile_name=profilename)  
        """Get a list of all of the vpcs for a given aws account"""
        client = boto3.client('ec2', verify=False)
        response = client.describe_vpcs(
        DryRun=False,
            Filters=[
                {
                    'Name': 'state',
                    'Values': [
                        'available',
                    ]
                },
            ]
        )
        items = response['Vpcs']
        vpcs = []
        firstitem = items[0]
        seconditem = items[1]
        for item in items:
            vpcobject = Vpc(item)
            vpcs.append(vpcobject)

        return vpcs

    def prettyprint(self, character, offset):
        print (character * offset + '--------------VPCs--------------------')
        print (character * offset + 'Vpc Id: ' + str(self.VpcId))
        print (character * offset + 'Cidr Block: ' + str(self.CidrBlock))
        print (character * offset + 'IsDefault: ' + str(self.IsDefault))
        
        print (character * offset + '--------------Nested Subnets--------------------')
        for subnet in self.subnets:
            print(subnet.prettyprint(' ', 5 + offset))
        # print (self.item)



# {u'VpcId': 'vpc-1472e072', u'InstanceTenancy': 'default', u'Tags': [{u'Value': 'tgrc-sandbox', u'Key': 'Name'}, {u'Value': 'esa', u'Key': 'BusinessUnit'}, {u'Value': '905611', u'Key': 'BillingCode'}], u'State': 'available', u'
# DhcpOptionsId': 'dopt-63c25304', u'CidrBlock': '10.12.160.0/22', u'IsDefault': False}