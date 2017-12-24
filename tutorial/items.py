# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field  

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WebcrawlerScrapyItem(Item):
    title = scrapy.Field()    # 标题
    degree = scrapy.Field()     # 链接
    desc = scrapy.Field()     # 简述