#-*- coding:utf-8 -*-

def ourDeco(func):
    # 장식이 되는 함수에 전달되는 모든 인자를 받을수 있는 준비하기
    def wrapper(*args, **kwargs):
        print args, kwargs
        func(*args, **kwargs)
    
    return wrapper

@ourDeco
def test1():
    print "test1()"

@ourDeco
def test2(num):
    print "test2()"

@ourDeco
def test3(num, name):
    print "test3()"
    
test1()
test2(1)
test3(2, "haegol")
test3(num=3, name="monkey")







