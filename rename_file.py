#/usr/bin/python
#coding:utf-8

__Author__ = 'eyu Fanne'
__Date__ = '2016/9/3'

##批量冲命名文件

import os

# 执行重命名功能
path = u'F:\慕课大巴2\【慕课大巴分享】尚学堂_尧玮_Android 5.0视频教程'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)) == True:
        newname = file.replace(u"尚学堂_尧玮_", "")
        os.rename(os.path.join(path, file), os.path.join(path, newname))
        # newname2 = file.replace(u'[mukedaba.com]徐老师大数据－',"")
        # os.rename(os.path.join(path,file),os.path.join(path,newname2))

