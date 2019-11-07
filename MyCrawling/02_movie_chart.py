from bs4 import BeautifulSoup
from urllib.request import urlopen
import bs4
import webbrowser
from datetime import datetime

now = datetime.now()

yesterday_date = str(now.year)+str(now.month)+str(now.day-1)
url1 ="https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=%yesterday_date"
html1 = urlopen(url1)
bs_obj1 = bs4.BeautifulSoup(html1.read(),"html.parser")

table = bs_obj1.find("table",{"class":"list_ranking"})
div = table.findAll("div",{"class":"tit5"})
td  = table.findAll("td",{"class":"point"})

movie_name = [div[i].a.string for i in range(0,len(div))]
movie_score = [td[i].string for i in range(0,len(div))]

for i in range(len(div)):
    print(movie_name[i],":",movie_score[i])
#movie_name = [div[i]]

while True:
    movie_search1 = (str)(input("\n어떤 영화를 찾으시나요?\n"))
    url2 = ("https://search.naver.com/search.naver?sm=top_sug.pre&fbm=1&acr=6&acq=vkdl&qdt=0&ie=utf8&query={movie_search}".format(
        movie_search = movie_search1))
    webbrowser.open(url2)
    exit(0)



'''
for i in table:
    for j in div:
        print(j.text, end="")
'''