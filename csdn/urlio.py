from fastscrapy.common.requests.task import Url
from BeautifulSoup import BeautifulSoup
from myuser.position import Link,Content
class UrlIO(Url):

    def save(self,path):
        with open(path,'w') as f:
            f.write(self.html)

def gethtml():

    ip = '58.20.128.123'
    port = '80'
    httpurl = 'http://blog.csdn.net/ACdreamers/article/list/1'
    u = UrlIO(ip,port,httpurl)
    u.save('test.txt')
    print u.status

def parse():
    f = BeautifulSoup(file('test.txt').read())    
    classes = [Link,Content]
    for position_class in classes:
        position_class(f,'').parse()

if __name__ == '__main__':
    parse()

