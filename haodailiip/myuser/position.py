# -*- coding: utf-8 -*-

from scrapy.utils.path import urlpath
from scrapy.parse.http import sendproxys,sendurls

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
            print 'ERROR\n\n\n'
            print self.html,'\n\n\n'
        print self.urls

        self.push()

    def push(self):
        sendurls(self.urls,self.uuid) 

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
            print self.attrs
            self.push()
        except: 
            pass
            
    def push(self):
        sendproxys(self.attrs) 
