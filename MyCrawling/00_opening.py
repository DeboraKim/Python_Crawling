from bs4 import BeautifulSoup
from urllib.request import urlopen
import bs4#BeautifulSoup => 페이지 url

url1 = "https://www.naver.com"
html1 =urlopen(url1)
#print(html1)

bs_obj1 = bs4.BeautifulSoup(html1.read(), "html.parser")
#print(bs_obj1)#html1의 페이지 소스 출력
find_div = bs_obj1.find("div", {"class":"section_navbar"})
#print(find_div)#class명에 따른 html정보를 가져옴

find_txt = find_div.findAll("span",{"class":"an_txt"})#span태그의 an_txt 클래스의 모든 정보들을 찾아옴 /리스트 형태로 반환

print(find_txt)

for i in find_txt:
    print(i.text)#해당 클래스 text값들만 출력

