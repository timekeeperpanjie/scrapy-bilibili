# -*- coding: utf-8 -*-
import scrapy


class BiliSpider(scrapy.Spider):
    name = "bili"
    allowed_domains = ["https://bilibili.com"]
    start_urls = ["https://search.bilibili.com/all?keyword=%E5%86%A0%E7%8A%B6%E7%97%85%E6%AF%92&from_source=nav_search_new&page=1"]

    def parse(self, response):
        selectors = response.xpath("//ul/li")
        for selector in selectors:
            title = selector.xpath("./a/@title").extract_first()
            up_name = selector.xpath("./div/div[3]/span[4]/a/text()").extract_first()
            links = selector.xpath("./a/@href").extract_first()
            items = {
				'title':title,
				'upname':up_name,
				'links':links
            }
            yield items
