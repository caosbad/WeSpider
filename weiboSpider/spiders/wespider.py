# -*- coding: utf-8 -*-

__author__ = 'Caos'

from scrapy import Spider, Item, Field, Request, log
from login_api import get_login_cookie
from scrapy.contrib.spiders import CrawlSpider, Rule
from weiboSpider.items import WeibospiderItem





# 考虑是否分开定义不同的item，将数据分类保存起来。

class Wespider(Spider):
    # def __init__(self, config):
    #     super(Wespider, self).__init__(self)
    #     self.config = config

    name, start_urls = 'weSpider', ['http://www.weibo.com/woobaopei']
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
        # 处理特殊字符并截取html
        script = script.replace('\\n', '')
        script = script.replace('\\t', '')
        index = script.find('"html":"')
        script = script[index+8: -3]
        kw = {'body': script}
        # 替换微博内容至response
        r = response.replace(**kw)
        items = []
        for i in range(1, 17):
            item = WeibospiderItem()
            # 微博内容的位置
            node = r.xpath('/html/body/div/div[2]/div[%s]/div[1]/div[2]' % i)

            # topWeibo = node.xpath('/div[1]/a[1]/@ignore').extract()
            contentDiv = node.xpath('div[1]/text()')
            aInContent = node.xpath('div[1]/a')
            # linkInContent = node.xpath('/div[1]/a/@title').extract()[0]
            postTime = node.xpath('div[2]/a[1]/@title').extract()
            postTime1 = node.xpath('div[3]/a[1]/@title').extract()
            subUser = node.xpath('div[2]/div[2]/div[1]/a[1]/text()').extract()
            subContent = node.xpath('div[2]/div[2]/div[2]/text()').extract()
            # subTime = node.xpath('div[2]/div[2]/div[5]/div[2]/a[1]/@title').extract()

            # 大于1说明文本中有链接或者@其他人
            if len(contentDiv) > 1:
                a = []
                for k in range(0, len(contentDiv)):
                    # 只有K小于链接个数时有效
                    if k < len(aInContent):
                        if len(aInContent[k].xpath('@title')) > 0:
                            outLink = aInContent[k].xpath('@title').extract()[0].encode('utf-8')
                        else:
                            outLink = None
                        # 不为空则是外链
                        if outLink is not None:
                            # 忽略置顶
                            if outLink == '微博会员特权':
                                link = ''
                            else:
                                link = '[链接]' + '(' + outLink + ')'

                        else:
                           link = aInContent[k].xpath('text()').extract()[0].encode('utf-8')

                        c = contentDiv[k].extract().strip().encode('utf-8') + link

                    else:

                        c = contentDiv[k].extract().strip().encode('utf-8').strip()

                    a.append(c)
                item['content'] = ''.join(a)
            else:
                item['content'] = contentDiv[0].extract().strip().encode('utf-8')






            # item['subTime'] = ''.join(subTime)
            if len(subUser) > 0:
                item['subUser'] = '> *' + ''.join(subUser).encode('utf-8') + '*'
                item['postTime'] = ''.join(postTime1).encode('utf-8')
            else:
                item['subUser'] = ''
                item['postTime'] = ''.join(postTime).encode('utf-8')
            if len(subContent) > 0:
                item['subContent'] = '>' + ''.join(subContent).encode('utf-8')

            else:
                item['subContent'] = ''







            items.append(item)

        return items



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