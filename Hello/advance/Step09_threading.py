#-*- coding:utf-8 -*- 
'''
    
'''
import threading
count=0

def printCount():
    
    for i in range(10000):
        print i
    
    print "end printCount()"

if __name__ == '__main__':
    
    print "메인 스레드가 시작 되었습니다."
    # printcount 함수를 다른 스레드에서 수행 시키기
    # 스레드 객체 샏ㅇ성해서 .Thread(target=함수)
    t=threading.Thread(target=printCount)
    #스레드 시작 시키기 
    t.start()
    print "메인 스레드가 종료됩니다."