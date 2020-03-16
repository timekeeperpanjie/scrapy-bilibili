# -*- coding: utf-8 -*-
import scrapy
import json
import time

class BiliSpider(scrapy.Spider):
    name = "math"
    allowed_domains = ["https://bilibili.com"]
    start_urls = [f'https://api.bilibili.com/x/tag/ranking/archives?tag_id=936917&rid=39&type=0&pn={page}&ps=20' for page in range(1,5)]

    def parse(self, response):
        selectors = json.loads(response.text)['data']['archives']
        for sel in selectors:
            title = sel['title']
            desc = sel['desc']
            date = time.localtime(float(sel['pubdate']))
            link = "%s%s" % ("https://www.bilibili.com/video/av",sel['aid'])
            items = {
                'title':title,
                'desc':desc,
                'date':time.strftime("%Y-%m-%d %H:%M:%S",date),
                'link':link
            }
            yield items
