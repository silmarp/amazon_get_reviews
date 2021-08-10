import scrapy
import re

def remove_end_string(link):
    pattern =re.compile(r'/reviews/')
    match = re.search(pattern, link)
    return link[:match.span()[0]]


class HomestarsSpider(scrapy.Spider):
    name = 'homestars'
    start_urls = ['https://homestars.com/on/toronto/categories/']

    def parse(self, response):
        
        for link in response.xpath('//a[@class="category-group__link"]'):

            next_site = "https://homestars.com" + link.css('a::attr(href)').get() + "?page=1"
            
            yield response.follow(next_site, callback=self.parse_category)
    
    def parse_category(self, response):
        
        for company in response.xpath('//a[@class="review-row-text__link"]'):
            target = "https://homestars.com" + company.css('a::attr(href)').get()
            target = remove_end_string(target)
            yield response.follow(target, callback=self.parse_company)



        next_page = "https://homestars.com" + response.xpath('//a[@rel="next"]').css('a::attr(href)').get()
        if next_page is not None:        
            yield response.follow(next_page, callback=self.parse_category)        



    def parse_company(self, response):
        
        url = "https://homestars.com" + response.xpath('//a[@class="company-header-details__name"]').css('a::attr(href)').get()
        company_name = response.xpath('//a[@class="company-header-details__name"]/h1/text()').get()
        company_number = response.xpath('//button[@class="company-header-contact__button"]/span/text()').get()
        
        yield{
            "COMPANY NAME": company_name,
            "PHONE NUMBER": company_number,
            "WEBSITE URL": url,
        }