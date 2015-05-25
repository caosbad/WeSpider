# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from spiders import user_settings as settings
import os

class WeibospiderPipeline(object):

    def __init__(self):
        self.fileName = os.path.join(os.environ['HOME'], settings['exportFile'])
        if os.path.exists(self.fileName):
            self.file = open(self.fileName, 'wb')
        else:
            self.file = file(self.fileName, 'wb')

    def process_item(self, item, spider):

        line = item['content']+'\n'+item['subUser']+'\n'+item['subContent']+'\n'+item['subTime']+'\n\n'+item['postTime']
        self.file.write(line)

        return item
