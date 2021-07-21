import scrapy
from ..items import AmazonReviewsItem

class AmazonSpider(scrapy.Spider):
    name =                              'amazon'
    allowed_domains =                   ['amazon.com']
    start_urls = [
            'https://www.amazon.com/Fortnite-7-Llama-Loot-Plush/product-reviews/B07GJ2MWTZ',
    ]


    def parse(self, response):
        
        items = AmazonReviewsItem()
        
        for review in response.xpath('//div[@data-hook="review"]'):
            grade =                     review.xpath(".//i[@data-hook='review-star-rating']/span/text()").get()

            if type(grade) == str:
                grade =                 float(review.xpath(".//i[@data-hook='review-star-rating']/span/text()").get()[0:3])
            else:
                grade =                 "not found"

            items["grade"] =            grade
            items["review_title"] =     review.xpath(".//a[@data-hook='review-title']/span/text()").get()
            items["comment"] =          review.xpath('.//span[@data-hook="review-body"]/span/text()').get()
            
            yield items 
                
        next_page =                     response.xpath('//li[@class="a-last"]').css('a::attr(href)').get()

        if next_page is not None:
            yield response.follow("https://www.amazon.com" + next_page, callback=self.parse)

