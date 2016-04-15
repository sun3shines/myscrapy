# -*- coding: utf-8 -*-

import os
from static import PROC_BFS_LIMIT,PROC_DFS_LIMIT,PROC_TOTAL_LIMIT,\
    TRY_TIMES,SLEEP_INTERVAL,CONTROLLER_HOST,CONTROLLER_PORT, ST_DIR
    
from fastscrapy.worker.core.conf import Conf
class MyConf(Conf):
    
    def getbfs(self):
        return PROC_BFS_LIMIT
    
    def getdfs(self):
        return PROC_DFS_LIMIT
    def gettotal(self):
        return PROC_TOTAL_LIMIT
    
    def getcontrollerhost(self):
        return CONTROLLER_HOST
    def getcontrollerport(self):
        return CONTROLLER_PORT
    
    def getlocalhost(self):
        return '192.168.36.201'
    
    def getparent(self):
        return ST_DIR
    
    def gettrytimes(self):
        return TRY_TIMES
    
    def getsleepinterval(self):
        return SLEEP_INTERVAL
    