class Account:
    id = ''
    name = ''
    profilename = ''

    instances = []
    vpcs = []
    elasticips = []
    subnets = []

    def __init__(self, elasticips, instances):
        
        self.instances = instances
        self.elasticips = elasticips
        self.profilename = ''

    
    def prettyprint(self):
        print ('------------ Account Printout  -------------------')
        print ('Account Id ' + str(self.id))

        print ('-------------Vpcs---------------------------- ')
        for vpc in self.vpcs:
            vpc.prettyprint()


        print ('-------------Instances---------------------------- ')
        for instance in self.instances:
            instance.prettyprint()

        print ('-------------Elastic Ips---------------------------- ')
        for eip in self.elasticips:
            eip.prettyprint()
        
        print ('-------------Subnets---------------------------- ')
        for subnet in self.subnets:
            subnet.prettyprint()