# /usr/bin/python
#coding:utf-8

__Date__ = "2016-10-13 17:12"
__Author__ = 'eyu Fanne'



##模拟登入seebug站点
##验证码图片识别
##https://www.seebug.org/

import requests
import urllib
import os
from bs4 import BeautifulSoup



class seebugLogin(object):
    def __init__(self):
        self.session = requests.Session()
        self.webUrl = r'https://sso.telnet404.com'
        self.loginUrl = r'https://sso.telnet404.com/cas/login/?next=/'
        self.headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch, br",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Connection":"keep-alive",
            "Host":"sso.telnet404.com",
            "Referer":"https://sso.telnet404.com/cas/login/?next=/",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
        }
        self.loginHeaders = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Content-Length":"110",
            "Content-Type":"application/x-www-form-urlencoded",
            "Host":"sso.telnet404.com",
            "Origin":"https://sso.telnet404.com",
            "Referer":"https://sso.telnet404.com/cas/login/?next=/",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
            }


    def getImg(self):
        dataList = []
        myText = self.session.get(self.loginUrl,headers=self.headers).text
        mySoup = BeautifulSoup(myText,'lxml')
        imgUrl = mySoup.find('img',{'class':'captcha'})
        captchaUrl = '%s%s' %(self.webUrl,imgUrl.get('src'))
        captchaFile = self.session.get(captchaUrl,headers=self.headers).content
        file('captcha.gif','wb').write(captchaFile)
        dataList.append('captcha.gif')
        tokenId = mySoup.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
        dataList.append(tokenId)
        return dataList

    def getData(self):
        imgFile = self.getImg()
        print imgFile[1]
        os.system('call %s' %imgFile[0])
        captchacode = raw_input('captcha:')
        loginData = {
            "csrfmiddlewaretoken":imgFile[1],
            "email":"896661380@qq.com",
            "password":"ljf891029",
            "captcha":captchacode,
        }
        return loginData


    def loginSeebug(self):
        data = self.getData()
        print data
        loginWork = self.session.post(self.loginUrl,headers=self.loginHeaders,data=data)
        print loginWork.status_code
        loginText = self.session.get(self.webUrl,headers=self.headers).text
        print loginText



if __name__ == '__main__':
    login = seebugLogin()
    login.loginSeebug()

