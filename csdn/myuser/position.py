# -*- coding: utf-8 -*-

from scrapy.utils.path import urlpath
from scrapy.storage.url import Url
from scrapy.storage.html import Html

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

        self.push()

    def push(self):
        Url(self.urls,self.uuid).save()

class Content:
    
    def __init__(self,html,uuid):
        self.html = html
        self.attrs = []
        self.uuid = uuid
        self.htmls = []          
    def parse(self):

        try:
            spans = self.html.findAll('span',{'class':'link_title'})
            for span in spans:
                articleurl = '/'.join(['blog.csdn.net',span.find('a').get('href')])
                title = span.find('a').text
                self.htmls.append((articleurl ,title))
        except: 
            pass
           
        self.push()
 
    def push(self):
        for url,title in self.htmls:
            Html(url,title).save() 
