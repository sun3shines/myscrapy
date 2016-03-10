# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.worker.core.arch import Scrapy
from scrapy.worker.core.proc import Proc

from myuser.position import Link,Content,START_URL,SCRAPY_UUID
from mysys.conf import MyConf
from mysys.static import ST_DIR,LOCAL_HOST

class MyProc(Proc):
    
    def getclasses(self):
        return [Link,Content]
    
    def getconf(self):
        return MyConf
    
class MySracpy(Scrapy):
    
    def getproc(self):
        return MyProc
        
if __name__ == '__main__':

    MySracpy(SCRAPY_UUID,START_URL).start(LOCAL_HOST,ST_DIR)
    

