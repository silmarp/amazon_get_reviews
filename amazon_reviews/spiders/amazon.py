import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    
    def start_requests(self):
        start_urls = [
            'https://www.amazon.com/Fortnite-7-Llama-Loot-Plush/dp/B07GJ2MWTZ',
        ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        print("worked till here 3")
        pass
