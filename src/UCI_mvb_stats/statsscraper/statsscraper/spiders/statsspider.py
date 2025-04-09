import scrapy


class StatsspiderSpider(scrapy.Spider):
    name = "statsspider"
    allowed_domains = ["ucirvinesports.com"]
    start_urls = ["https://ucirvinesports.com/sports/mens-volleyball/roster/shane-aitken/7170"]

    def parse(self, response):
        pass
