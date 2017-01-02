#! /usr/bin/env python
from urlparse import urlsplit
from os.path import basename
import urllib2
import re
import requests
import os
import json
import datetime

if not os.path.exists('images'):
    os.mkdir("images")

print("start>>>>>>>>>>>>>>>>>>>>>>>")

url = "http://tieba.baidu.com/p/4823036908"
response = requests.get(url)
#print(response.text)
img_urls = re.findall('img .*?src="(.*?)"', response.text)
#print(img_urls)

for img_url in img_urls:
    try:
        img_data = urllib2.urlopen(img_url,timeout = 5).read()
        file_name = basename(urlsplit(img_url)[2])
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  " + file_name)
        output = open('images/' + file_name, 'wb')
        output.write(img_data)
        output.close()
    except Exception,e:
        print("error : " + e.message)
        pass

print("end>>>>>>>>>>>>>>>>>>>>>>>")