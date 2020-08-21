# -*- coding: utf-8 -*-
import scrapy


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['wz.sun076191.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest']

    def parse(self, response):
        selectors = response.xpath('//li[@class="clear"]')
        #print(selectors)
        for selector in selectors:
            # print(selector.xpath('./span[5]').get())
            # item = {
            #       '问题摘要': selector.xpath('./span[3]//text()').get(),
            #       '更新日期': selector.xpath('./span[5]/text()').get(),
            #       '目前状态': selector.xpath('./span[2]/text()').get(),
            #       'href': 'http://wz.sun0769.com/'+selector.xpath('./span[3]/a[@href]/@href').get()
            # }
            item = {}
            item['问题摘要'] = selector.xpath('./span[3]//text()').get(),
            item['更新日期'] = selector.xpath('./span[5]/text()').get(),
            item['href'] = 'http://wz.sun0769.com' + selector.xpath('./span[3]/a[@href]/@href').get()
            #print(item)
            #yield item
            yield scrapy.Request(
                item["href"],
                callback=self.parse_detail,
                meta={"item": item},
            dont_filter = True
            )
            #print(item)
            #yield item
        #下一页  翻页相关
        next_url = response.xpath('//div[@class="mr-three paging-box"]/a[@class="arrow-page prov_rota"]/@href').get()
        next_url='http://wz.sun0769.com'+next_url
        #print(next_url)
        if next_url :
            yield scrapy.Request(
                next_url,
                callback=self.parse,
            #dont_filter = True
            )


    def parse_detail(self,response):  # 处理详情页面
        #print("==========")
        item = response.meta["item"]
        #print(item)
        item["content"] = response.xpath('//div[@class="details-box"]//text()').extract()
        # item["图片内容"] = response.xpath('//div[@class="clear details-img-list"//img/@src').get()
        # item["图片内容"] = response.xpath['http://wz.sun0769.com' + (i for i in item["图片内容"])]
        yield item
