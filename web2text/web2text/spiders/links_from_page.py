from typing import Iterable

import scrapy


class LinksFromPageSpider(scrapy.Spider):
    name = 'links_from_page'

    def __init__(self, url="https://aardwolfarchers.org.uk", **kwargs):
        self.url = url
        super().__init__(**kwargs)

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        yield response.css('a::attr("href")').getall()