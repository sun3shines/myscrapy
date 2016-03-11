# -*- coding: utf-8 -*-

from scrapy.utils.path import urlpath
from scrapy.parse.http import sendurls

START_URL = 'blog.csdn.net/ACdreamers/article/list/1'
SCRAPY_UUID = 'csdn_ACdreamers'

class Link:
    def __init__(self,html,uuid):
        self.html = html
        self.urls = []
        self.uuid = uuid
        
    def parse(self):
        try: 
            hrefs = self.html.find('div',{'id':'papelist'}).findAll('a')
            self.urls = [urlpath('/'.join(['blog.csdn.net',a.get('href')])) for a in hrefs]
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
            spans = self.html.findAll('span',{'class':'link_title'})
            for span in spans:
                articleurl = '/'.join(['blog.csdn.net',span.find('a').get('href')])
                title = span.find('a').text
                print articleurl ,title
        except: 
            pass
            
    def push(self):
        pass
