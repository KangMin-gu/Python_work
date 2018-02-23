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
        result = num2/float(num1)   
        
        print "{} 를 {} 로 나눈값은 {} 입니다."\
            .format(num2, num1, result)
    # except 예외 type, 예외 정보를 받을 변수 :
    except ZeroDivisionError, zde:
        print zde
        print "어떤 수를 0으로 나눌수는 없습니다."    
    except ValueError, ve:
        print ve
        print "숫자로 변환할 수 없습니다."
    except Exception, e:
        print "기타 예외 발생!"
    else: #예외가 발생하지 않으면 실행되는 블럭
        print "예외가 발생하지 않으면 실행되는 블럭"
    finally: #java finally와 같다
        print "예외 발생과 상관없이 실행되는 블럭"    
    #zde ve 에러 외 예러면 exception 으로가고 에러가 안나면 ELSE 갓다 finally 간다.
        
    print "메인 스레드가 종료 됩니다."
    
    
