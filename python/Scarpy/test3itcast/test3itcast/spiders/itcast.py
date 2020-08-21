# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        #pass
        # ret = response.xpath('//div[@class="tea_con"]//h3/text()').extract()
        # for r in ret:
        #     print(r)
        li_list = response.xpath('//div[@class="tea_con"]//li')
        for li in li_list:
            item = {
                'name': li.xpath('.//h3/text()').get(),
                'title': li.xpath('.//h4/text()').get()
            }
            logger.warning(item)
            #print(item)
            yield item#减少内存占用