from bs4 import BeautifulSoup
from urllib.request import urlopen
import bs4
url1 = "https://www.mk.co.kr/news/bestclick/"
url2 = "https://www.hankyung.com/ranking"

html1 = urlopen(url1)
html2 = urlopen(url2)

bs_obj1 = bs4.BeautifulSoup(html1.read(),"html.parser")#html형식으로 쉽게 보여줌
bs_obj2 = bs4.BeautifulSoup(html2.read(),"html.parser")

div = bs_obj1.find("div",{"class":"list_area"})
dts = div.findAll("dt",{"class":"tit"})

#print(dts)
#for i in dts:
#    print(i.text)#텍스트만 떼오기
ul = bs_obj2.find("ul",{"class":"down_rank_news"})
divs = ul.findAll("h2")

print(divs)

for i in divs:
    print(i.text)#텍스트만 떼오기

