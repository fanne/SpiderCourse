# /usr/bin/python
#coding:utf-8

__Date__ = "2016-11-02 16:02"
__Author__ = 'eyu Fanne'

#多行数据合并一行写入文本
newfile = []
with open('tmptest','rb') as f:
    for data in  f.readlines():
        data = data.strip()
        newfile.append(data)

print newfile

with open("newfile.txt",'wb') as nf:
    nf.write(''.join(newfile))
