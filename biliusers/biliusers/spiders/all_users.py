# -*- coding: utf-8 -*-
import scrapy
import json
import random
import time
from biliusers.items import BiliusersItem

class AllUsersSpider(scrapy.Spider):
    name = 'all-users'
    allowed_domains = ['bilibili.com']
    start_urls = [f'https://api.bilibili.com/x/space/acc/info?mid={id}' for id in range(1,10)]

    def parse(self, response):
        t = random.random()
        time.sleep(t)
        item = BiliusersItem()
        data = json.loads(response.text)
        item['mid'] = data['data']['mid']
        item['name'] = data['data']['name']
        item['sex'] = data['data']['sex']
        item['sign'] = data['data']['sign']
        item['rank'] = data['data']['rank']
        item['level'] = data['data']['level']
        item['birthday'] = data['data']['birthday']
        item['vip'] = data['data']['vip']['type']
        yield item
        #print(data['data']['name'])
