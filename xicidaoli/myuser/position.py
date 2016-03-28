# -*- coding: utf-8 -*-

from scrapy.utils.path import urlpath
from scrapy.storage.url import Url
from scrapy.storage.proxy import Proxy

START_URL = 'www.xicidaili.com/nn/4'
SCRAPY_UUID = 'xicidaili4'
class Link:
    def __init__(self,html,uuid):
        self.html = html
        self.urls = []
        self.site = 'www.xicidaili.com'
        self.uuid = uuid
    def parse(self):
        try: 
            hrefs = self.html.find('div',{'class':'pagination'}).findAll('a')
            self.urls = [urlpath('/'.join([self.site,a.get('href')])) for a in hrefs]
        except:
            pass

        self.push()

    def push(self):
        Url(self.urls,self.uuid).save()
 
class Content:
    
    def __init__(self,html,uuid):
        
        self.html = html
        self.attrs = []        
    def parse(self):

        try:
            table = self.html.find('table',{'id':'ip_list'})
            trs = table.findAll('tr')
            for tr in trs:
                
                tds = tr.findAll('td')
                if not tds:
                    continue
                
                attr = {}
                attr['ip'] = tds[2].text.strip()
                attr['port'] = tds[3].text.strip()
                attr['scheme'] = tds[6].text.strip()
                attr['anonymous'] = tds[5].text.strip()
                self.attrs.append(attr)
        except: 
            pass
        self.push()
 
    def push(self):
        Proxy(self.attrs).save()
        sendproxys(self.attrs) 
        
