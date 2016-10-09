#/usr/bin/python
#coding:utf-8

__Author__ = 'eyu Fanne'
__Date__ = '2016/10/9'

from bs4 import BeautifulSoup
import requests
import json
import sys
import re
reload(sys)
import urllib2
sys.setdefaultencoding('utf8')


downUrl = r'https://www.youtube.com/playlist?list=PLQqbdnAgoRmag4RdUZAKl8Vz0H70T0wDA'
youtubeUrl = r'https://www.youtube.com'

myText = requests.get(downUrl,verify=False).text
#print myText

print "======================="

mySoup = BeautifulSoup(myText,'lxml')
urlList = mySoup.findAll("a",{"class":"pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link "})
for myurl in urlList:
    #print myurl
    videotitle = myurl.get_text()
    videourl = myurl.get("href")
    print '%s  %s%s' %(videotitle,youtubeUrl,videourl)