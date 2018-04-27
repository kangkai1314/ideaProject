# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class ZhihuspiderPipeline(object):
    def process_item(self, item, spider):
        with open('test1.txt ','a') as f:
            f.write(item['content'].encode('utf-8')+'\n')


class ImagePipeLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        for i in item['imageurl']:
            yield Request(i)




