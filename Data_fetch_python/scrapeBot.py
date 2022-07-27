import urllib.request, json
import pandas as pd


class scrapeBot():
    def sendReturn(self):
        self.key_list = ('all-ads','all-analytics','all-javascript','all-cms','all-Web-Master','all-cdn','all-media','all-cdns','all-framework','all-payment','all-Web-Server','all-hosting')
        self.value_list = []
        self.dict_values = {}
        
        for k in self.key_list:
            self.value_list.append(self.data2[0][k])
            
        for i in range(len(self.key_list)):
            self.dict_values[self.key_list[i]] = self.value_list[i]
        self.df = pd.DataFrame.from_dict(self.dict_values, orient='index').transpose()
        
        return self.df
    
    def returnData(self):
        return self.data2, self.data[0]['companyname']

    def __init__(self,title):
        with urllib.request.urlopen("https://api.builtwith.com/daltv1/api.json?KEY=59dd064f-4d0c-4ab6-8f5a-a8c699cbf391&LOOKUP="+title) as url:
            self.data2 = json.loads(url.read().decode())

        