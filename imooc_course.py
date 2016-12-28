# /usr/bin/python
#coding:utf-8

__Date__ = "2016-12-05 14:47"
__Author__ = 'eyu Fanne'

import requests
from bs4 import BeautifulSoup
import time,sys,os,configparser


##初始化数据
imooc_url = r'http://www.imooc.com/'
login_url = r'http://www.imooc.com/passport/user/login'
verify_t = str(int(time.time()*1000))
login_session = requests.session()
login_header = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Connection":"keep-alive",
    "Content-Length":"284",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Host":"www.imooc.com",
    "Origin":"http://www.imooc.com",
    "Referer":"http://www.imooc.com/user/newlogin",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
}


##获取验证码
def getVerificationCode():
    verifycode_url = r'http://www.imooc.com/passport/user/verifycode?t=%s' %verify_t
    verify_data = login_session.get(verifycode_url).content
    file("imooc_vcode.gif", 'wb').write(verify_data)
    if sys.platform.find('linux') >= 0:
        os.system('xdg-open imooc_vcode.gif')
    elif sys.platform.find('darwin') > 0:
        os.startfile('imooc_vcode.gif')
    else:
        os.system('call imooc_vcode.gif')
    verycode = raw_input('code:')
    return verycode



##模拟登入
def starLogin():
    config = configparser.ConfigParser()
    config.read("config.ini")
    configname = 'imooc'
    username = config.get(configname,'username')
    password = config.get(configname,'password')
    login_data = {
        "username":username,
        "password":password,
        "verify":getVerificationCode(),
        "remember":"1",
        "pwencode":"1",
        "referer":"http://www.imooc.com",
    }

    start_login = login_session.post(login_url,data=login_data,headers=login_header)
    print start_login.status_code
    for k,v in start_login.json().items():
            print k,v



##程序入口
if __name__ == '__main__':
    starLogin()