#/usr/bin/python
#coding:utf-8

__Author__ = 'eyu Fanne'
__Date__ = '2016/9/3'

##批量冲命名文件

import os

# 执行重命名功能
##执行目录像以下的就不能执行
## F:\慕课大巴2\001已去除解压密码\领测软件测试视频教程\领测软件测试视频教程
##带了001，会被转码

path = u'I:\慕课大巴4\SVN 视频教程'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)) == True:
        newname = file.replace(u"尚硅谷_", u"")
        os.rename(os.path.join(path, file), os.path.join(path, newname))
        # newname2 = file.replace(u'[mukedaba.com]徐老师大数据－',"")
        # os.rename(os.path.join(path,file),os.path.join(path,newname2))

