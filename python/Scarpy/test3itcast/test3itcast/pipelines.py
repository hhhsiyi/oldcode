# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging


logger = logging.getLogger(__name__)
class Test3ItcastPipeline(object):
    def process_item(self, item, spider):
        item['hello']='world'
        return item


class Test3ItcastPipeline1(object):
    def process_item(self, item, spider):
        if spider.name == 'itcast':
            logger.warning(item)
            print(item)
        return item
