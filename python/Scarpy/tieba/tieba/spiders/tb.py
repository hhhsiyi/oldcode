# -*- coding: utf-8 -*-
import scrapy


class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['tieba.com']
    start_urls = ['http://tieba.com/f?kw=%C0%EE%D2%E3&fr=ala0&tpl=5']

    def parse(self, response):
        div_list = response.xpath('//a[@class="j_th_tit "]/text()')
        for div in div_list:
            print(div)
