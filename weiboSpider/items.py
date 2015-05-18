# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeibospiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()
    image = scrapy.Field()
    outLink = scrapy.Field()
    reName = scrapy.Field()
    reContent = scrapy.Field()
    reOutLink = scrapy.Field()
    reTime = scrapy.Field()
    reImage = scrapy.Field()
    pass
