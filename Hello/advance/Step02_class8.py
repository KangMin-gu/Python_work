#-*- coding:utf-8 -*-

class Test:
    
    # 참조값으로 call 할수 있도록 
    def __call__(self):
        print "called!"

# decorator 를 class 로 정의하기

class HelloBye:
    #생성자
    def __init__(self, func):
        self.func=func
    # call 되었을때 할 동작
    def __call__(self, *args, **kwargs):
        print "hello!"
        self.sing()
        self.dance()
        result=self.func(*args, **kwargs)
        print "bye~"
        return result
    def sing(self):
        print "노래를 해요"
    def dance(self):
        print "춤을 춰요"
    
@HelloBye
def test1():
    print "test1() 호출됨"

@HelloBye    
def test2():
    print "test2() 호출됨"

if __name__ == '__main__':
    t1=Test()
    t1() # call 가능 
    print "-------"
    test1()
    test2()
    
    
    
    
    
    
    
    