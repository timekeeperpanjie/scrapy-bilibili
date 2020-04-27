#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import requests
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
url = "https://m.space.bilibili.com/1?from=video"
#url = "http://www.baidu.com"
ret = requests.get(url,headers=headers)
print(ret.status_code)
