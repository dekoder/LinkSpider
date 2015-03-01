from scrapy.http import Request
from scrapy import log


class FilterByDomTree(object):

    def __init__(self):
        self.treehash = {}

    def process_spider_output(self, response, result, spider):

        def _filter(r):
            if not isinstance(r, Request):
                return True

            url = r.url
            if not self.pathSet.dismatch(url):
                return False
            if not self.manager.addUrl(url):
                return False

            return True

        return (r for r in result or () if _filter(r))


