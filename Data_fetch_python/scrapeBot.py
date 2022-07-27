import urllib.request, json
import pandas as pd

api = "dff2f050-6308-45cc-bb19-1ff5b8fb6ed1"

class scrapeBot():
    def getData(self):
        self.key_list = ('all-ads','all-analytics','all-javascript','all-cms','all-Web-Master','all-cdn','all-media','all-cdns','all-framework','all-payment','all-Web-Server','all-hosting')
        self.dkey_list = ('all_ads','all_analytics','all_javascript','all_cms','all_Web_Master','all_cdn','all_media','all_cdns','all_framework','all_payment','all-_Web-Server','all_hosting')
        self.value_list = []
        self.dict_values = {}
        
        for k in self.key_list:
            self.value_list.append(self.data2[0][k])
            
        for i in range(len(self.key_list)):
            self.dict_values[self.dkey_list[i]] = self.value_list[i]
        self.df = pd.DataFrame.from_dict(self.dict_values, orient='index').transpose()
        
        return self.dict_values ,self.data2[0]['companyname']

    def __init__(self,title):
        with urllib.request.urlopen("https://api.builtwith.com/daltv1/api.json?KEY="+api+"&LOOKUP="+title) as url:
            self.data2 = json.loads(url.read().decode())

