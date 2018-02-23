#-*- coding:utf-8 -*-
'''
    lambda 는 한줄짜리 익명의 함수 이다.
    
    - 형식 
    
    lambda 함수의 인자 : 리턴값
'''

def useFunc(func):
    print "useFunc() 가 호출되었습니다."
    result=func(99, 1) # 인자로 전달된 함수 호출
    print "result:", result
    print "userFunc() 가 리턴 됩니다."


if __name__ == '__main__':
    
    print lambda a,b : a+b
    print "--------"
    print (lambda a,b :a+b)(10, 20)
    
    # f1 은 함수 type 이다 
    f1=lambda a,b : a+b
    
    # f1 함수와 동일한 기능을 하는 f2 함수 
    def f2(a,b):
        return a+b
    
    # result 는 int type 3 이다.
    result=(lambda a,b : a+b)(1, 2)
    
    useFunc(lambda a,b : a+b)
    
    useFunc(lambda a,b : a*b)
    
    useFunc(lambda a,b : a-b)
    
    

    
    
  
  
  
    
    
    
    
    