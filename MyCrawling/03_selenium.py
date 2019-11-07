from bs4 import BeautifulSoup
from urllib.request import urlopen
import bs4
import webbrowser
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome('./chromedriver.exe')
driver.get('http://eclass2.hufs.ac.kr:8181/ilos/main/main_form.acl')
delay = 3
driver.implicitly_wait(delay)

driver.find_element_by_xpath('//*[@id="header"]/div[2]/ul/li/a/img').click()#로그인창 xpath
driver.find_element_by_name('usr_id').send_keys('')
driver.find_element_by_name('usr_pwd').send_keys('')
driver.find_element_by_xpath('//*[@id="myform"]/div/div/div/fieldset/div[1]/input').click()#로그인 버튼
driver.implicitly_wait(delay)


sleep(5.0)
driver.close