#-*- coding:utf-8 -*- 
from pip._vendor import requests
import threading

def getHtml(url):
    #get 방식 요청해서 응답 객체를 리턴 받는다. 
    responseObj=requests.get(url)
    #응답 문자열 출력해보기
    print responseObj.text
    
if __name__ == '__main__':
    print "메인 스레드가 시작됨"
    
    #요청 url
    url = "http://daum.net"
    
    t=threading.Thread(target=getHtml, args=(url,))
    t.start()

    print "메인 스레드가 종료됨"