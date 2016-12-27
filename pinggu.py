# /usr/bin/python
#coding:utf-8

__Date__ = "2016-10-14 15:04"
__Author__ = 'eyu Fanne'

from urllib import urlencode


aaa = u'农行'

bbb = {'ddd':'nud',
       '222':'农行',
       'se':'试试'}

print urlencode(bbb)