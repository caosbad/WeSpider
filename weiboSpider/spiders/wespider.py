# -*- coding: utf-8 -*-

__author__ = 'Caos'

from scrapy import Spider, Item, Field, Request, log
from login_api import get_login_cookie
from scrapy.contrib.spiders import CrawlSpider, Rule



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

class Wespider(CrawlSpider):
    # def __init__(self, config):
    #     super(Wespider, self).__init__(self)
    #     self.config = config

    name, start_urls = 'weSpider', ['http://www.weibo.com/u/1674242970']
    # self.config.get('urls'
    cookies = None

    # def process_request(self, request):
    #     request = request.replace(**{'cookies': self.cookies})
    #     return request

    def parse(self, response):
        script_set = response.xpath('//script')
        script = ''
        for s in script_set:
            try:
                s_text = s.xpath('text()').extract()[0].encode('utf8').replace(r'\"', r'"').replace(r'\/', r'/')
            except:
                return response
            if s_text.find('WB_feed_detail') > 0:
                script = s_text
                break
        kw = {'body': script}
        response = response.replace(**kw)

    def extract_weibo_response(self, response):     # 提取weibo内容,替换response
        script_set = response.xpath('//script')
        script = ''
        for s in script_set:
            try:
                s_text = s.xpath('text()').extract()[0].encode('utf8').replace(r'\"', r'"').replace(r'\/', r'/')
            except:
                return response
            if s_text.find('WB_feed_detail') > 0:
                script = s_text
                break
        kw = {'body': script}
        response = response.replace(**kw)
        return response

    def _parse_response(self, response, callback, cb_kwargs, follow=True):  # 继承crawlspider这个方法,这个方法在解析页面/提取链接前调用
            response = self.extract_weibo_response(response)
            return super(Wespider, self)._parse_response(response, callback, cb_kwargs, follow)


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