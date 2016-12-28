# /usr/bin/python
#coding:utf-8

__Date__ = "2016-11-17 19:13"
__Author__ = 'eyu Fanne'

from bs4 import BeautifulSoup
import requests


pageUrl = r'http://m.dingdianzw.com/wapbook/2430.html'


headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Host":"m.dingdianzw.com",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36",
}

pageText = requests.get(pageUrl,headers=headers).text
pageSoup = BeautifulSoup(pageText,'lxml')

print pageSoup