# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonReviewsItem(scrapy.Item):
    grade =                scrapy.Field()
    review_title =         scrapy.Field()
    comment =              scrapy.Field()