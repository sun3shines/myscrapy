from fastscrapy.common.requests.task import Url
from BeautifulSoup import BeautifulSoup
from userm.position import Link,Content
from userm.position import START_URL,NLink,IMG
from userm.position import SCRAPY_UUID
class UrlIO(Url):

    def save(self,path):
        with open(path,'w') as f:
            f.write(self.html)

def gethtml():
    ip = '122.96.59.104'
    port = '80'

    httpurl = 'http://' + START_URL

    u = UrlIO(ip,port,httpurl,p=False)
    u.save(SCRAPY_UUID+'.txt')
    print u.status

def parse():
    f = BeautifulSoup(file('test.txt').read())    
    classes = [Link,Content]
    for position_class in classes:
        position_class(f,'').parse()

def parsecls(cls,path):
    f = BeautifulSoup(file(path).read())
    classes = cls 
    for position_class in classes:
        position_class(f,'').parse()

if __name__ == '__main__':
#    parse()
#    gethtml()
#    parsecls([IMG],SCRAPY_UUID+'.txt')
    print UrlIO('117.21.182.109','8080','mm3825.com/html/article/index12056.htm').status
