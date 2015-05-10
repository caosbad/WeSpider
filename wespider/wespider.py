# -*- coding: utf-8 -*-

__author__ = 'Caos'

from scrapy import Spider, Item, Field, Request, log
from login_api import get_login_cookie

from scrapy.shell import inspect_response


class WeiboItem(Item):
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

    name, start_urls = 'weSpider', ['http://www.weibo.com/woobaopei']
    # self.config.get('urls'
    cookies = None

    def parse(self, response):
        '''

        '''

        self.log('A response from %s just arrived!' % response.url)
        print '---===-----====-----=====----====----====='

        r = response
        scriptList = r.xpath("//script")
        body = ''

        for script in scriptList:
            html =  script.xpath('text()').extract()[0].encode('utf8').replace(r'\"', r'"').replace(r'\/', r'/')
            # 找出JS动态生成的代码，进行截取操作
            if html.startswith('FM.view({'):
                index = html.find(r'"html"')
                html = html[index: ]
                body = body + html
        kw = {'body': body}
        r = r.replace(**kw)
        print r.body

    def start_requests(self):
        for url in self.start_urls:
            if not self.cookies:
                self.cookies = get_login_cookie(url)    # 得到该url下的cookie
            yield Request(url, dont_filter=True, cookies=self.cookies, meta={'cookiejar': 1})  # 这里填入保存的cookies



# 暂行的Xpath储存办法
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