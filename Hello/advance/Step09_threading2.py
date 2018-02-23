#-*- coding:utf-8 -*- 
'''
    
'''
import threading
import time
count=0

def printCount(num, name):
    #전달 받은 인자 출력해 보기
    for i in range(10):
        print "num:",num,"name:",name
        # time 페키지의 sleep() 메소드를 이용해서 스레드 1초 sleep
        time.sleep(1) # java = Thread.sleep(1000); python에서는 초단위로 표현한다. 
        print i
    
    print "end printCount()"

if __name__ == '__main__':
    
    print "메인 스레드가 시작 되었습니다."
    # printcount 함수를 다른 스레드에서 수행 시키기
    
    # 스레드 객체 샏성해서 .Thread(target=함수)
    t=threading.Thread(target=printCount, args=(1, u'김구라'))
    #스레드 시작 시키기 
    t.start()
    
    # 스래드 객체 하나더 생성해서 
    t2=threading.Thread(target=printCount, args=(2, u'해골'))
    #스레드 시작 시키기 
    t2.start()
    print "메인 스레드가 종료됩니다."
    
    
    