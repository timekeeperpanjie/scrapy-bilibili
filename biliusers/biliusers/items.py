# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BiliusersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mid = scrapy.Field()
    name = scrapy.Field()
    sex = scrapy.Field()
    sign = scrapy.Field()
    rank = scrapy.Field()
    level = scrapy.Field()
    birthday = scrapy.Field()
    vip = scrapy.Field()
    #yield item
