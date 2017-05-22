
import boto3

class Vpc:
    VpcId = ''
    DhcpOptionsId = ''
    CidrBlock = ''
    IsDefault = ''

    item = ''


    def __init__(self, item):
        self.item = item

        self.VpcId = item.get('VpcId')
        self.DhcpOptionsId = item.get('DhcpOptionsId')
        self.CidrBlock = item.get('CidrBlock')
        self.IsDefault = item.get('IsDefault')
        
        

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

        

    def prettyprint(self):
        print ('--------------VPCs--------------------')
        print ('Vpc Id: ' + str(self.VpcId))
        print ('Cidr Block: ' + str(self.CidrBlock))
        print ('IsDefault: ' + str(self.IsDefault))

        # print (self.item)



# {u'VpcId': 'vpc-1472e072', u'InstanceTenancy': 'default', u'Tags': [{u'Value': 'tgrc-sandbox', u'Key': 'Name'}, {u'Value': 'esa', u'Key': 'BusinessUnit'}, {u'Value': '905611', u'Key': 'BillingCode'}], u'State': 'available', u'
# DhcpOptionsId': 'dopt-63c25304', u'CidrBlock': '10.12.160.0/22', u'IsDefault': False}