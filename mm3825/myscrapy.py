# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.worker.core.arch import Scrapy
from scrapy.worker.core.proc import Proc

from userm.position import Link,Content,START_URL,SCRAPY_UUID
from sysm.conf import MyConf
from sysm.static import ST_DIR,LOCAL_HOST
from userm.position import NLink,IMG

class MyProc(Proc):
    
    def getclasses(self):
        return [NLink,IMG]
    
    def getconf(self):
        return MyConf
    
class MySracpy(Scrapy):
    
    def getproc(self):
        return MyProc
        
if __name__ == '__main__':

    MySracpy(SCRAPY_UUID,START_URL).start(LOCAL_HOST,ST_DIR)
    

