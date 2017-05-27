class Account:
    id = ''
    name = ''
    profilename = ''

    regions = []

    def __init__(self) :
        self.profilename = ''

    def hydratefromitem(self):
        
        for item in self.regions:
            item.hydratefromitem()

    def prettyprint(self):
        
        print('Number of Regions: {}  '.format(len(self.regions)))

        print ('------------ Account Printout  -------------------')
        print ('Account Id ' + str(self.id))

        print ('-------------Regions---------------------------- ')
        for region in self.regions:
            region.prettyprint(' ', 5)

    def dumpjson(self):
        
        for item in self.regions:
            print(item.dumpjson())
