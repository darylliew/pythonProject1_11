import requests
# Set the target webpage
url = "http://brickset.com/sets/year-2008"
r = requests.get(url)
# This will get the full page
print(r.text)
print("Status code:")
print("\t *", r.status_code)

h = requests.head(url)
print("Header:")
print("**********")
# To print line by line

for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

headers = {
    'User-Agent' : "Mobile"
}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)

import scrapy
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ["http://brickset.com/sets/year-2008"]
    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {
                    'Image Link': x.xpath(newsel).extract_first(),
            }
            Page_selector = '.next a ::attr(href)'
            next_page = response.css(Page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
            )
