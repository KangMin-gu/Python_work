#-*- coding:utf-8 -*- 
'''
    javascript 비동기 / java 동기
    예외 처리 문법 학습 java의 try {} catch{} 문과 같다.
'''
from test.Step02_DataType import num1

if __name__ == '__main__':
        
    try:
        num = input("젯수 입력:")
        num2 = input("피젯수 입력:")
        
        # num1 이 0 이면 ZeroDivisionError type 예외가 발생한다.
        result = num2/num1
        
        print "{} 를 {} 로 나눈값은 {} 입니다."\
            .format(num2, num1, result)
    # except 예외 type, 예외 정보를 받을 변수 :
    except ZeroDivisionError, zde:
        print zde
        print "어떤 수를 0으로 나눌수는 없습니다."    
        
    print "메인 스레드가 종료 됩니다."
