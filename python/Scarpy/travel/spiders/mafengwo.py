import time

import requests
# 安装: pip3 install lxml
from lxml import etree
import re

from travel.db.mongodb import mongo
"""
1. 准备URL列表
2. 遍历URL列表, 发送请求, 获取响应数据
3. 解析数据
4. 保存数据
"""


class MaFengWoSpider(object):

    def __init__(self, city):
        self.city = city
        self.url_pattern = 'http://www.mafengwo.cn/search/q.php?q=' + city + '&p={}&t=pois&kt=1'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
        }

    def get_url_list(self):  # 获取url
        url_list = []
        for i in range(1, 21):
            url = self.url_pattern.format(i)
            url_list.append(url)
        return url_list

    def get_page_from_url(self, url):
        # 根据url 发送请求 获取页面数据
        response = requests.get(url, headers=self.headers)  # 请求
        return response.content.decode()  # 返回

    def get_datas_from_page(self, page):
        # 解析页面数据
        element = etree.HTML(page)
        lis = element.xpath('//div/div[2]/h3')
        # 遍历标签，提取数据
        # 定义列表，存储数据
        data_list = []
        for e in lis:
            item = {}

            name = ''.join(e.xpath('./a//text()'))

            count_comment = ''.join(e.xpath('../ul/li[2]/a//text()'))
            count_travel_notes = ''.join(e.xpath('../ul/li[3]/a//text()'))
            item2 = {}

            total = ''.join(e.xpath('./a//text()'))
            total = total + '~' + ' '.join(e.xpath('../ul/li[2]/a//text()'))
            total = total + '~' + ' '.join(e.xpath('../ul/li[3]/a//text()'))

            # if(total.find('景点')==0):
            #     print(type(total))
            # print("以下是美食")
            # if(total.find('美食')==0):
            #     print(total)
            # print(name+" "+count_comment+" "+count_travel_notes)
            # //div/div[2]/ul/li[2]//text()
            # if(not name.find('景点')):
            #     print(name)
            if name.find('景点') == -1:
                continue
            # name.replace('景点-',' ',name)
            item['name'] = name.replace('景点 - ', '')
            item['city'] = self.city
            item['address'] = ''.join(e.xpath('../ul/li[1]/a//text()'))
            # item['comments'] = ''.join(e.xpath('../ul/li[2]/a//text()'))
            comments = ''.join(e.xpath('../ul/li[2]/a//text()'))
            comments = re.findall('蜂评\((\d+)', comments)[0]
            item['comments_num'] = comments
            travels = ''.join(e.xpath('../ul/li[3]/a//text()'))
            travels = re.findall('游记\((\d+)', travels)[0]
            item['travel_notes_num'] = travels
            # item['travel'] = ''.join(e.xpath('../ul/li[3]/a//text()'))

            print(item)
            data_list.append(item)
        return data_list

    def run(self):
        # 程序入口
        url_list = self.get_url_list()
        # 获取要爬取的url列表
        print(url_list)
        # 发送请求，获取数据
        for url in url_list:
            page = self.get_page_from_url(url)
            datas = self.get_datas_from_page(page)
            self.save_data(datas)
        pass

    def save_data(self, datas):
        # 保存
        for data in datas:
            # 景点名称指定为主键
            data['_id'] = data['name']
            mongo.save(data)
        pass


if __name__ == '__main__':
    time_start = time.time()
    ms = MaFengWoSpider('北京')
    ms.run()
    time_end = time.time()
    print("爬虫运行时间为"+str(time_end-time_start))