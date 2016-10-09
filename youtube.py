# /usr/bin/python
#coding:utf-8

__Date__ = "2016-07-20 10:45"
__Author__ = 'eyu Fanne'


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

myText = requests.get(downUrl,verify=False).text
print myText

print "======================="

mySoup = BeautifulSoup(myText,'lxml')

# print len(myText)
# print len(str(mySoup))

# print mySoup

# print myText
#
# num_start = u'青云志'
# num_end = u'诛仙青云志'
#
#
# myList = re.findall("\/watch\?v=.*;index=\d",myText)
# for i in myList:
#     print "%s%s" %(youtubeUrl,i)

# myList = BeautifulSoup(myStr,'lxml')
#
# print myList

