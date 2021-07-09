import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = [
            'https://www.amazon.com/Fortnite-7-Llama-Loot-Plush/product-reviews/B07GJ2MWTZ',
    ]


    def parse(self, response):
        for review in response.xpath('//div[@data-hook="review"]'):
            try:
                yield {
                    'grade' :            float(review.xpath(".//i[@data-hook='review-star-rating']/span/text()").get()[0:3]),
                    'review title' :     review.xpath(".//a[@data-hook='review-title']/span/text()").get(),
                    'comment' :          review.xpath('.//span[@data-hook="review-body"]/span/text()').get(),
                }
            except:
                yield {
                    'grade' :            0,
                    'review title' :     "Not Found",
                    'comment' :          review.xpath('.//span[@data-hook="review-body"]/span/text()').get(),
                }
                
        next_page = response.xpath('//li[@class="a-last"]').css('a::attr(href)').get()

        if next_page is not None:
            yield response.follow("https://www.amazon.com" + next_page, callback=self.parse)

