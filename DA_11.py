import requests

url = "http://brickset.com/sets/year-2008"
r = requests.get(url)

print(r.text)
print("Status code:")
print("\t *", r.status_code)

h = requests.head(url)
print("Header:")
print("**********")


for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

headers = {
    'User-Agent' : "Mobile"
}

url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)

import scrapy
class BrickSetSpider(scrapy.Spider):
    name = 'brick_spider'
    start_urls = ['http://brickset.com/sets/year-2008']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
import unittest
class TestScrapper(unittest.TestCase):
    def test_requests(self):
        print("Spoofing current header....\n")
        headers = {'User-Agent': "Mobile"}
        for url in self.start_urls:
            yield requests(url, headers=headers)
        url2 = 'http://httpbin.org/headers'
        rh = requests.get(url2, headers=headers)
        print(rh.text)

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

if __name__=='_main_':
    unittest.main



