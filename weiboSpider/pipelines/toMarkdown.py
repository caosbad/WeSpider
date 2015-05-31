# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from weiboSpider.spiders.user_settings import settings
import os
import codecs

class WeibospiderPipeline(object):

    def __init__(self):
        fileName = os.getenv('HOME')+'/'+settings['exportFile']
        if not os.path.exists(fileName):
            file(fileName)

        self.file = codecs.open(fileName, 'w')

    def process_item(self, item, spider):

        line = item['content']+'\n'+item['subUser']+'\n'+item['subContent']+'\n\n'+item['postTime']+'\n\n\n-----\n\n\n'
        self.file.write(line)


        return item
