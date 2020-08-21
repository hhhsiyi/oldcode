# -*- coding: utf-8 -*-
import scrapy


class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'#爬虫名字，必须唯一
    allowed_domains = ['xicidaili.com']#允许采集的域名
    #start_urls = [f'https://www.xicidaili.com/nn/{page}' for page in range(1,4)]#开始采集的网站
    start_urls = ['https://www.xicidaili.com/nn/5']  # 开始采集的网站
    #start_urls = ['https://www.xicidaili.com/nn/']
    def parse(self, response):
        #提取数据
        #response.xpath('表达式')
        #response.xpath('//tr/td[2]/text()').extract()
        selectors = response.xpath('//tr')
        for selector in selectors:
            ip = selector.xpath('./td[2]/text()').get()#只保留data字段
            port = selector.xpath('./td[3]/text()').get()
            print("ip地址",ip,"端口号",port)

            # items={
            #     '地址': selector.xpath('./td[2]/text()').get(),
            #     '端口': selector.xpath('./td[3]/text()').get()
            # }


        #翻页操作
        # next_page=response.xpath('//a[@class="next_page"]/@href').get()
        # if next_page:
        #     print(next_page)
        #     #next_page='https://www.xicidaili.com/nn/'+next_page
        #     next_url=response.urljoin(next_page)
        #     #发出请求 request callback是回调函数 就是将请求得到的相应 交给自己处理
        #     yield scrapy.Request(next_url, callback=self.parse)# 生成器、算是一种递归
