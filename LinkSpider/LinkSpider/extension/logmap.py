from scrapy import signals

from LinkSpider.tools.UrlManager import UrlManager

class LogMap(object):

    def __init__(self, manager):
        self.manager = manager

    @classmethod
    def from_crawler(cls, crawler):
        crawler._urlmanager = UrlManager()

        o = cls(crawler._urlmanager)

        crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)

        return o

    def spider_closed(self, spider):
        print self.manager.layer()

