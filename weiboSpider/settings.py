# -*- coding: utf-8 -*-

# Scrapy settings for weibo_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'weiboSpider'

SPIDER_MODULES = ['weiboSpider']
NEWSPIDER_MODULE = 'weiboSpider'
DOWNLOAD_DELAY = 2
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weibo_spider (+http://www.yourdomain.com)'
