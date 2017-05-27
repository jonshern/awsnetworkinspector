import yaml


class AccountConfig(object):
    configuredregions = dict()
    accounts = dict()

    def initializefromdictionary(self, settings):
        self.configuredregions = settings["accounts"]["allowedregions"]
        self.accounts = settings["accounts"]["configuredaccounts"]



    def initializefromfile(self, filename):
        with open(filename, "r") as f:
            settings = yaml.load(f)

        print('File Contents')    
        print(settings)      

        self.initializefromdictionary(settings)      