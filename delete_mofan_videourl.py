# /usr/bin/python
#coding:utf-8

__Date__ = "2016-10-08 15:23"
__Author__ = 'eyu Fanne'

###删除莫烦视频内容代码中的一些链接内容
###匹配删除行，并写回原文件

import os
import re
import shutil
videoDir = r'G:\tutorials'

###多行匹配
comment = re.compile(r'^#.*tutorials/',re.DOTALL)


def delVideoUrl(pyFile):
    if pyFile.endswith('.py'):
        print pyFile
        with open(pyFile,'rt') as f:
            data = f.read()
        re_data = comment.sub(" ",data)  ###匹配替换为空格
        f_new = open('%s_new' %pyFile,'wt')
        f_new.write(re_data)  ##写入到新的文本
        f_new.close()
        os.remove(pyFile)
        os.rename('%s_new' %pyFile,pyFile)





if __name__ == '__main__':
    print 'aaaaddd'
    print videoDir
    for root,dirs,files in os.walk(videoDir):
        print 'aaa'
        print root
        print dirs
        print files
        for videofile in files:
            videofile = os.path.join(root,videofile)
            print videofile
            delVideoUrl(videofile)

