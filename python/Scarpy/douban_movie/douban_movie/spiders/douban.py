# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['https://movie.douban.com/top250']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        selectors = response.xpath('//a/span')
        for selector in selectors:
            #//a/span[@class]
            #//span[@class]
            #//span[@class="title"][1]
            print(selector)
            name = selector.xpath('./span[@class="title"][1]/text()').get()
            score = selector.xpath('../span[4]/text()').get()
            #print(score)
            if name!=None :
                #print(name,score)
                 print(name)
                 #print(score)

