from scrapy.http import Request, Response
from scrapy import log

from LinkSpider.tools.HashCount import hashCount

class FilterByDomTreeMiddleware(object):

    def __init__(self):
        self.treehash = {}

    def getHash(self, data):
        return hashCount(data)

    def process_response(self, request, response, spider):
        data = response.body

        if -1 == data.find("<html") == data.find("<meta") == data.find("<body"):
            return response

        h = self.getHash(data)
        if self.treehash.has_key(h):
            if self.treehash[h] >= 5:
                log.msg(format="Filtered dom tree repeat %(request)s",
                        level=log.DEBUG, spider=spider, request=request)
                return Response("")
            else:
                self.treehash[h] += 1
                return response
        else:
            self.treehash[h] = 1
            return response

