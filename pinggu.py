# /usr/bin/python
#coding:utf-8

__Date__ = "2016-10-14 15:04"
__Author__ = 'eyu Fanne'

##按关键词爬取人大经济论坛

from urllib import urlencode
from bs4 import BeautifulSoup
import os
import requests
import json


class getPinggu(object):
    def __init__(self):
        self.session = requests.Session()
        self.searchUrl = r'http://s.pinggu.org/search.php?searchsubmit=yes'
        self.headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Content-Length":"75",
            "Content-Type":"application/x-www-form-urlencoded",
            "Host":"s.pinggu.org",
            "Origin":"http://s.pinggu.org",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
        }
        self.searcWord = raw_input('输入搜索的内容:')

    def searchWork(self):
        formhash_text = self.session.get(r'http://s.pinggu.org/search.php').text
        formhash_soup = BeautifulSoup(formhash_text,'lxml')
        formhash_data = formhash_soup.find('input',{'name':'formhash'}).get('value')
        print formhash_data
        data = {
            "formhash":formhash_data,
            "mod":"forum",
            "srchtype":"title",
            "confirm":"yes",
            "srchtxt":self.searcWord,
        }
        # postdata = urlencode(data)
        # print postdata
        serchText = self.session.post(self.searchUrl,headers=self.headers,data=data)
        print serchText.status_code
        print serchText.headers
        print type(serchText.headers)
        # print json.dumps(serchText.headers,indent=4)
        # print serchText.text






if __name__ == '__main__':
    startSearch = getPinggu()
    startSearch.searchWork()