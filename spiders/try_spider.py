import scrapy

class TrySpider(scrapy.Spider):
    name="title"
    start_urls=[
        'https://www.sainithapamagar.com.np',
        'https://www.abisheksubedi.com.np',
        "https://www.onlinekhabar.com",
        "https://www.daraz.com.np"
    ]

    def parse(self,response):
        title=response.css('title::text').extract()
        yield {'titletext':title}