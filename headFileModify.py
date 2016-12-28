# /usr/bin/python
#coding:utf-8

__Date__ = "2016-10-10 15:13"
__Author__ = 'eyu Fanne'

###修改header文件

import re

headerFile = r'headFile'

def getFile():
    f = open(headerFile,'rt')
    for i in f.readlines():
        head = i.strip()
        head_2 = re.sub(':','":"',head,1)  ##查找到符号 ：进行替换，并只是执行第一个的:符号替换
        print '"%s",' %head_2





if __name__ == '__main__':
    getFile()

