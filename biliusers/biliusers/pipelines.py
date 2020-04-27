# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3 as sqlite

class BiliusersPipeline(object):
    def process_item(self, item, spider):
        conn = sqlite.connect('users.db')
        cur = conn.cursor()
        #cur.execute("select * from users;")
        #ret = cur.fetchall()
        #for i in ret:
        #    print(i)
        insert = "insert into users(mid,name,sex,sign,rank,level,birthday,vip) values(%d,'%s','%s','%s',%d,%d,'%s',%d);"
        cur.execute(insert %(item['mid'],item['name'],item['sex'],item['sign'],item['rank'],item['level'],item['birthday'],item['vip']))
        conn.commit()
        #return item
