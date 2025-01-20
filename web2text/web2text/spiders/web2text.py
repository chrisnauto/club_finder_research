from pathlib import Path
import re

import scrapy
from bs4 import BeautifulSoup

class Web2Text(scrapy.Spider):
    name = "web2text"

    def __init__(self, url="https://aardwolfarchers.org.uk/", **kwargs):
        self.url = url
        super().__init__(**kwargs)

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        title = response.xpath("//title/text()").extract_first()
        raw_text = ''.join(response.xpath("//body//text()").extract()).strip()

        #remove all html tags and then separate the pages line by line
        soup = BeautifulSoup(raw_text, "html.parser").get_text().strip()
        text = "\n".join(soup.split())#re.sub(r"[\n\t]", "", soup)

        page = response.url.split("/")[2]
        name = page.split(".")[0]
        filename = f"web-{name}.txt"

        with open(filename, "a") as f:
            f.write(title + "\n")
            f.write(text + "\n")
            f.close()

        self.log("saved raw text")

        #pagination for websites should go through all links available
        #TODO check page hasn't already been visited
        # pages = response.css('a::attr("href")').getall()
        # for page in pages:
        #     if page is not None:
        #         yield response.follow(page, self.parse)


class LinksFromPageSpider(scrapy.Spider):
    name = 'links_from_page'

    def __init__(self, url="https://aardwolfarchers.org.uk", **kwargs):
        self.url = url
        super().__init__(**kwargs)

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        yield response.css('a::attr("href")').getall()


if __name__ == "__main__":
    links = LinksFromPageSpider(ulr="https://aardwolfarchers.org.uk")
    print(links)
