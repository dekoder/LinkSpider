import urllib

from scrapy.http import Request

from LinkSpider.config import store_path

class UrlLogMiddleware(object):

    def __init__(self):

        self.storeFile = urllib.quote_plus(store_path)
        self.urls = []

    def process_spider_output(self, response, result, spider):
        def _writeUrls():
            with open(self.storeFile, "a+") as f:
                f.write('\n'.join(self.urls).encode('utf-8'))
                f.write('\n')
        def _log(r):
            if isinstance(r, Request):
                self.urls.append(r.url)
            return True

        result = (r for r in result or () if _log(r))
        _writeUrls()

        return result

