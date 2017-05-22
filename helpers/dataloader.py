

class DataLoader:
    

    @staticmethod    
    def loadvpcdata(profilename):
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

    @staticmethod
    def loadinstancedata(profilename):

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