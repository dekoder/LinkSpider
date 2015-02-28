#!/usr/bin/env python

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from LinkSpider.config import start_link, domains

class UrlsSpider(CrawlSpider):
    name = "urls"
    allowed_domains = domains
    start_urls = [
        start_link,
    ]

    rules = (
        Rule(LinkExtractor(allow=()), callback='parse_item', follow = True),
    )

    def parse_item(self, response):
        pass
