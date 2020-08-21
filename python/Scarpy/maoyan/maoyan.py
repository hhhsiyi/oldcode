import threading
import time
from queue import Queue
from lxml import etree
import requests
import json


class ThreadCrawl(threading.Thread):
    def __init__(self,threadName,pageQueue,dataQueue):
        super(ThreadCrawl,self).__init__()
        self.threadName = threadName#线程名
        self.pageQueue = pageQueue#页码队列
        self.dataQueue = dataQueue#数据队列
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
        }

    def run(self):
        print("启动"+self.threadName)
        while not CRAWL_EXIT:
            try:
                page = self.pageQueue.get(False)
                url = 'http://www.mafengwo.cn/search/q.php?q=' + str(page) + '&p={}&t=pois&kt=1'
                content = requests.get(url,headers = self.headers)
                self.dataQueue.put(content)

            except:
                pass
        print("结束"+self.threadName)


class ThreadParse(threading.Thread):
    def __init__(self,threadname,dataQueue,filename):
        super(ThreadParse,self).__init__()
        self.threadname = threadname
        self.dataQueue = dataQueue
        self.filename = filename

    def run(self):
        while not PARSE_EXIT:
            try:
                html = self.dataQueue(False)
                self.parse(html)
            except:
                pass
    def parse(self,html):
        html = etree.HTML(html)



CRAWL_EXIT = False
PARSE_EXIT = False
def main():
    time_start = time.time()
    filename = open("duanzi.json","a")
    pageQueue = Queue(10)
    for i in range(1,11):
        pageQueue.put(i)

    dataQueue = Queue()
    crawlList=['t1','t2','t3']
    threadcrawl = []
    for threadname in crawlList:
        thread = ThreadCrawl(threadname,pageQueue,dataQueue)
        thread.start()
        threadcrawl.append(thread)

    #解析过程
    parseList = ["解析线程1","解析线程2","解析线程3"]
    threadparse = []
    for threadname in parseList:
        thread = ThreadParse(threadname,dataQueue,filename)
        ThreadCrawl.start()
        threadparse.append(thread)



    while not pageQueue.empty():
        pass

    global CRAWL_EXIT
    CRAWL_EXIT = True

    print("页码队列为空 ，退出循环")

    for thread in threadcrawl:
        thread.join()
        print("1")

    time_end = time.time()
    print("程序运行时间为"+str(time_end-time_start))

if __name__ =="__main__":
    main()