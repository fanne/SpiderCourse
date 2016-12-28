# /usr/bin/python
#coding:utf-8

__Date__ = "2016-12-05 15:50"
__Author__ = 'eyu Fanne'

from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')


from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print driver.page_source