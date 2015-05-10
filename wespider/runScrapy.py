#!/usr/bin/env/python
# -*- coding: utf-8 -*-
__author__ = 'Caos'


import os
os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'project.settings') #Must be at the top before other imports

from scrapy import log, signals, project
from scrapy.xlib.pydispatch import dispatcher
from scrapy.settings import default_settings as settings
from scrapy.crawler import CrawlerProcess
from multiprocessing import Process, Queue


class CrawlerScript():
    def __init__(self):
        self.crawler = CrawlerProcess(settings)
        if not hasattr(project, 'crawler'):
            self.crawler.install()
        self.crawler.configure()
        self.items = []
        dispatcher.connect(self._item_passed, signals.item_passed)

    def _item_passed(self, item):
        self.items.append(item)

    def _crawl(self, queue, spider_name):
        spider = self.crawler.spiders.create(spider_name)
        if spider:
            self.crawler.queue.append_spider(spider)
            self.crawler.start()
            self.crawler.stop()
            queue.put(self.items)

    def crawl(self, spider):
        queue = Queue()
        p = Process(target=self._crawl, args=(queue, spider,))
        p.start()
        p.join()
        return queue.get(True)



if __name__ == "main":
    log.start()


    items = list()
    crawler = CrawlerScript()
    list.append(crawler.crawl('weSpider'))
    print items
