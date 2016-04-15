# -*- coding: utf-8 -*-

from fastscrapy.utils.path import urlpath
from fastscrapy.stroage.url import Url
from fastscrapy.storage.proxy import Proxy

START_URL = 'www.haodailiip.com/guonei/1'
SCRAPY_UUID = 'proxyhaodaili'

class Link:
    def __init__(self,html,uuid):
        self.html = html
        self.urls = []
        self.uuid = uuid
        
    def parse(self):
        try: 
            hrefs = self.html.find('td',{'class':'td760'}).findAll('a')
            self.urls = [urlpath('/'.join(['www.haodailiip.com',a.get('href')])) for a in hrefs]
        except:
            pass
        self.push()

    def push(self):
        Url(self.urls,self.uuid).save() 

class Content:
    
    def __init__(self,html,uuid):
        self.html = html
        self.attrs = []
        self.uuid = uuid
                
    def parse(self):

        try:
            table = self.html.find('table',{'class':'proxy_table'})
            trs = table.findAll('tr')
            for tr in trs:
                tds = tr.findAll('td')
                attr = {}
                attr['ip'] = tds[0].text.strip()
                if attr['ip'].startswith('IP'):
                    continue

                attr['port'] = tds[1].text.strip()
                attr['scheme'] = tds[3].text.strip()
                attr['anonymous'] = tds[4].text.strip()
                self.attrs.append(attr)
        except: 
            pass
        self.push()
 
    def push(self):
        Proxy(self.attrs).save()
