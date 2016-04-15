# -*- coding: utf-8 -*-

from fastscrapy.utils.path import urlpath
from fastscrapy.storage.url import Url
from fastscrapy.storage.html import Html
from fastscrapy.storage.jpg import Jpg
import traceback

# START_URL = 'mm3825.com/html/part/index17.htm'
# SCRAPY_UUID = 'jpg_mm3825'
START_URL = 'mm3825.com/html/article/index12056.htm'
SCRAPY_UUID = '1_mm3825'

class Link:
    def __init__(self,html,uuid):
        self.html = html
        self.urls = []
        self.uuid = uuid
        
    def parse(self):
        try: 
            hrefs = self.html.find('div',{'class':'pagination'}).findAll('a')
            self.urls = [urlpath('/'.join(['mm3825.com',a.get('href')])) for a in hrefs]
        except:
            pass
        self.push()

    def push(self):
        Url(self.urls,self.uuid).save()
        print self.urls

class NLink(Link):

    def parse(self):
    
        try:
            div = self.html.find('div',{'align':'center'})
            aes = div.findAll('a')
            ae = aes[-1]
            self.urls = [urlpath('/'.join(['mm3825.com',ae.get('href')]))] 
        except:
            print str(traceback.format_exc()) 
        self.push()
 
class Content:
    
    def __init__(self,html,uuid):
        self.html = html
        self.attrs = []
        self.uuid = uuid
        self.htmls = []          
    def parse(self):

        try:
            eas = self.html.findAll('a',{'target':'_blank'})
            for ea in eas:
                articleurl = '/'.join(['mm3825.com',ea.get('href')])
                title = ea.text
                self.htmls.append((articleurl ,title))
        except: 
            print traceback.format_exc()
            pass
        print self.htmls 
        self.push()
 
    def push(self):
        for url,title in self.htmls:
            Html(url,title).save() 


class IMG(Content):
    def parse(self):
        try:
            imgs = self.html.findAll('img')
            for img in imgs:
                self.htmls.append(img.get('src'))
        except:
            print traceback.format_exc()
            pass
        print self.htmls
        self.push()

    def push(self):
        for src in self.htmls:
            try:
                Jpg(src).save()
            except:
                print traceback.format_exc()

