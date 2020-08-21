# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['qq.com']
    start_urls = ['https://news.qq.com/']

    def parse(self, response):
        href = response.xpath('')
        print(response.body)

