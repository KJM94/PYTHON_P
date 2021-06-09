#정보 수집 스크래핑/크롤링

'''
인터넷
    -네트워크의 네트워크, 여러 네트워크들을 연결 시킨 개념
웹
    -월드 와이드 웹(www - word wide web)은 인터넷에 연결된 컴퓨터들을 통해
    사람들이 정보를 공유할 수 있는 전 세계적인 정보 공간

URL
    -파일식별자, 유일자원 지시자, 인터넷 상에서 자원이 어디 있는지를 표시하기 위한 규칙

웹 페이지
    -web 상에서 각각의 문서들

웹 스크래핑
    -웹페이지에서 정보를 추출하는 행위
    -데이터 수집이 목적
    -데이터를 수집하여 분석하여 더 부가가치가 높은 데이터 생성

방법론
    -페이지 구조 분석
    -페이지 다운로드
    -데이터 추출

브라우져 개발자 도구 사용 F12

웹페이지는 기본적으로 HTML이라는 언어로 작성
가져올 내용은 BODY에 포함

CSS
    -시각적으로 미려하게 표현하기 위해 사용
JavaScript
    -웹페이지의 동적인 기능을 구현

웹 페이지 구성 = HTML(요소)+CSS(스타일표현)+JavaScript(동적 기능)


'''

'''
import requests
url = "http://www.naver.com"
res = requests.get(url)
print(res.status_code)
print(res.content)
'''

'''
import requests
from bs4 import BeautifulSoup

url = "http://www.naver.com"
res = requests.get(url)

#soup변수에 html 요소 저장
#첫번째 인사 html 소수, 두번째 인자 parser

soup = BeautifulSoup(res.content,"html.parser")
#soup 변수를 이용해 html 요소를 탐색할 수 있다.

print(soup.find_all('ul'))
print(soup.find_all('span',attrs={"class":"ah_k"}))
#soup.find_all(id="아이디")
#soup.find_all(class="클래스")
#class,id 속성을 쉽게 검색에 이용할 수 있는 shorcut

#test = soup.find_all('span',attrs={"class":"ah_k"}[1].get_text())
'''


import requests
from bs4 import BeautifulSoup
url = "http://www.boannews.com/media/t_list.asp"

param = {"kind":0}
res=requests.get(url,params = param)

if res.status_code != 200:
    exit(1)

soup = BeautifulSoup(res.content,"html.parser")

news_list = soup.find_all(class_="news_list")


'''
news = news_list[0]
print(news)
print("\n\n\n\n\n")
print(news.find(class_="news_txt").get_text())

news = news_list[1]
print(news)
print("\n\n\n\n\n")
print(news.find(class_="news_txt").get_text())
'''

for news in news_list :
    print(news.find(class_="news_txt").get_text())
    print(news.find_all("a")[1].get_text())
    print(news.find_all("a")[1].get("href"))



test = new_news_list = soup.find_all(class_="HitNews_img")
print(test)



#https://book.coalstudy.com/data-crawling/week-1














































