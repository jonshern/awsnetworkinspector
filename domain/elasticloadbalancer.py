import boto3

class ElasticLoadBalancer:
    RawData = ''
    IpAddressType = ''
    VpcId = ''
    LoadBalancerArn = ''
    DNSName = ''
    LoadBalancerName = ''
    Scheme = ''
    

    def __init__(self, item):
        self.RawData = item

    def hydratefromitem(self):
        self.IpAddressType = self.RawData.get('IpAddressType')
        self.VpcId = self.RawData.get('VpcId')
        self.LoadBalancerArn = self.RawData.get('LoadBalancerArn')
        self.DNSName = self.RawData.get('DNSName')
        self.LoadBalancerName = self.RawData.get('LoadBalancerName')
        self.Scheme = self.RawData.get('Scheme')

# {u'IpAddressType': 'ipv4', u'VpcId': 'vpc-1472e072', u'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-east-1:475602056032:loadbalancer/app/LoadBalancerTest/d7a9fad1cf658dc4', u'State': {u'Code': 'a
# ctive'}, u'DNSName': 'LoadBalancerTest-1726258815.us-east-1.elb.amazonaws.com', u'SecurityGroups': ['sg-e6029698'], u'LoadBalancerName': 'LoadBalancerTest', u'CreatedTime': datetime.datetime(2017, 5, 2
# 7, 3, 40, 39, 890000, tzinfo=tzutc()), u'Scheme': 'internet-facing', u'Type': 'application', u'CanonicalHostedZoneId': 'Z35SXDOTRQ7X7K', u'AvailabilityZones': [{u'SubnetId': 'subnet-1b152c52', u'ZoneNa
# me': 'us-east-1a'}, {u'SubnetId': 'subnet-eb2462b0', u'ZoneName': 'us-east-1b'}]}

    

    @staticmethod
    def loaddata(profilename):
        loadbalancers = []
        dev = boto3.session.Session(profile_name=profilename)
        # client = boto3.client('elb')
        client = boto3.client('elbv2')

        response = client.describe_load_balancers()

        for item in response['LoadBalancers']:
            loadbalancers.append(ElasticLoadBalancer(item))

        return loadbalancers
        
    def prettyprint(self):
        print ('----------------------------------')
        # print ('Public IP ' + str(self.PublicIp))
        # print ('Private IP ' + str(self.PrivateIpAddress))

