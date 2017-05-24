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

    def linksubnetstovpcs(self):
        for vpc in self.vpcs:
            for subnet in self.subnets:
                if subnet.VpcId == vpc.VpcId:
                    vpc.subnets.append(subnet)
    
    def prettyprint(self):
        
        print('Number of Vpcs: {}  '.format(len(self.vpcs)))

        print ('------------ Account Printout  -------------------')
        print ('Account Id ' + str(self.id))

        for vpc in self.vpcs:
            vpc.prettyprint(' ', 5)


        print ('-------------Instances---------------------------- ')
        for instance in self.instances:
            instance.prettyprint()

        print ('-------------Elastic Ips---------------------------- ')
        for eip in self.elasticips:
            eip.prettyprint()
        
        # print ('-------------Subnets---------------------------- ')
        # for subnet in self.subnets:
        #     subnet.prettyprint()