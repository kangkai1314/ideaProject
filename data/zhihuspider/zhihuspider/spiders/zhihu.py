# -*- coding: utf-8 -*-
import scrapy
from .items import ZhihuspiderItem

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    url='https://www.zhihu.com/question/39640358'
    url1='https://zhuanlan.zhihu.com/p/29749782'
    start_urls = ['https://www.zhihu.com/question/39640358']

    def parse(self, response):
        title=response.xpath('//title/text()')
        print title
        item=ZhihuspiderItem()
        item['title']=title
        #content=response.xpath('//div[@class="RichText Post-RichText"]/p/text()').extract()
        content=response.xpath('//span[@class="RichText CopyrightRichText-richText"]/text()').extract()
        for i in content:
            if i ==[]:
                break
            else:
                item['content']=i
                yield item

                with open('help1.txt','a') as f:

                    print type(i)
                    f.write(i.encode('utf-8')+'\n')




