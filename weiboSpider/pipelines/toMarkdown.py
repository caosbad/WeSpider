# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from weiboSpider.spiders.user_settings import settings
import os
class WeibospiderPipeline(object):

    def __init__(self):
        fileName = os.getenv('HOME')+'/'+settings['exportFile']
        if os.path.exists(fileName):
            self.file = open(fileName, 'wb')
        else:
            self.file = file(fileName, 'wb')

    def process_item(self, item, spider):

        line = item['content']+'\n'+item['subUser']+'\n'+item['subContent']+'\n\n'+item['postTime']
        self.file.write(line)

        return item
