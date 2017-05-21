
class Vpc:
    id = ''
    cidr_block = ''
    dhcp_options_id = ''
    instance_tenancy = ''
    ipv6_cidr_block_association_set = ''
    is_default = ''
    state = ''
    tags = ''
    vpc_id = ''

    item = ''
    subnets = []
    securitygroups = []
    

    def __init__(self, item):
        self.item = item

    def printvpc(self):
        print (self.item)

