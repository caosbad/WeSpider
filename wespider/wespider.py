# -*- coding: utf-8 -*-

__author__ = 'Caos'

from scrapy import Spider, Item, Field

class Post(Item):
    title = Field()

class Wespider(Spider):
    # def __init__(self, config):
    #     super(Wespider, self).__init__(self)
    #     self.config = config
    name, start_urls = 'weSpider', ['http://weibo.com/woobaopei']
    # self.config.get('urls'

    def parse(self, response):
        return [Post(title=e.extract()) for e in response.css("#Pl_Official_MyProfileFeed__22 > div > div.WB_feed.WB_feed_profile > div:nth-child(2) > div.WB_feed_detail.clearfix > div.WB_detail")]
