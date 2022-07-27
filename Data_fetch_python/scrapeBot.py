import urllib.request, json
import pandas as pd

api = "f370525e-0480-4336-9bf4-9cdaf5ed772f"

class scrapeBot():
    def getData(self):
        self.key_list = ('all-ads','all-analytics','all-javascript','all-cms','all-Web-Master','all-cdn','all-media','all-cdns','all-framework','all-payment','all-Web-Server','all-hosting')
        self.value_list = []
        self.dict_values = {}
        
        for k in self.key_list:
            self.value_list.append(self.data2[0][k])
            
        for i in range(len(self.key_list)):
            self.dict_values[self.key_list[i]] = self.value_list[i]
        self.df = pd.DataFrame.from_dict(self.dict_values, orient='index').transpose()
        
        return self.df,self.data2[0]['companyname']

    def __init__(self,title):
        with urllib.request.urlopen("https://api.builtwith.com/daltv1/api.json?KEY="+api+"&LOOKUP="+title) as url:
            self.data2 = json.loads(url.read().decode())
