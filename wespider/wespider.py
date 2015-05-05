# -*- coding: utf-8 -*-

__author__ = 'Caos'

from scrapy import Spider, Item, Field

class Weibo(Item):
    name = Field()
    content = Field()
    time = Field()
    image = Field()
    outLink = Field()
    reName = Field()
    reContent = Field()
    reOutLink = Field()
    reTime = Field()
    reImage = Field()

# 考虑是否分开定义不同的item，将数据分类保存起来。

class Wespider(Spider):
    # def __init__(self, config):
    #     super(Wespider, self).__init__(self)
    #     self.config = config

    name, start_urls = 'weSpider', ['http://weibo.com']
    # self.config.get('urls'

    def parse(self, response):

        itemList = []
        # 暂时设置默认值为第一页的数据(45条)，进行遍历查询。
        for i in range(1, 45):
            Weibo['name'] = response.xpath(xpathMap['nameXpath'] % i).extract()
            Weibo['content'] = response.xpath(xpathMap['contentXpath'] % i).extract()
            Weibo['time'] = response.xpath(xpathMap['timeXpath'] % i).extract()
            list.append(Weibo)

        return itemList
        # return [Post(title=e.extract()) for e in response.css("#Pl_Official_MyProfileFeed__22 > div > div.WB_feed.WB_feed_profile > div:nth-child(2) > div.WB_feed_detail.clearfix > div.WB_detail")]


xpathMap = {
    # 基础的XPATH路径，后续会根据实际的元素拼接
    'baseXpath': '//*[@id="v6_pl_content_homefeed"]/div/div[4]/div[',
    'nameXpath': '//*[@id="v6_pl_content_homefeed"]/div/div[4]/div[%s]/div[1]/div[3]/div[1]/a[1]/text()',
    'contentXpath': '//*[@id="v6_pl_content_homefeed"]/div/div[4]/div[%s]/div[1]/div[3]/div[2]/text()',
    'timeXpath': '//*[@id="v6_pl_content_homefeed"]/div/div[4]/div[%s]/div[1]/div[3]/div[4]/a[1]/@title',
    'imageXpath': '//*[@id="v6_pl_content_homefeed"]/div/div[4]/div[%s]/div[1]/div[3]/div[3]/div/div/ul/li[%s]/img/@src',
    'outLinkXpath': '//*[@id="v6_pl_content_homefeed"]/div/div[4]/div[%s]/div[1]/div[3]/div[2]/a/@href',
    'reNameXpath': '//*[@id="v6_pl_content_homefeed"]/div/div[4]/div[%s]/div[1]/div[3]/div[3]/div[2]/div[1]/a/text()',
    'reContentXpath': '//*[@id="v6_pl_content_homefeed"]/div/div[4]/div[%s]/div[1]/div[3]/div[3]/div[2]/div[2]/text()',
    'reOutLinkXpath': '//*[@id="v6_pl_content_homefeed"]/div/div[4]/div[%s]/div[1]/div[3]/div[3]/div[2]/div[2]/a/@href',
    'reTimeXpath': '//*[@id="v6_pl_content_homefeed"]/div/div[4]/div[%s]/div[1]/div[3]/div[5]/a[1]/@title',
    'reImageXpath': '//*[@id="v6_pl_content_homefeed"]/div/div[4]/div[%s]/div[1]/div[3]/div[3]/div[2]/div[3]/div/div/ul/li[%s]/img/@src'
}