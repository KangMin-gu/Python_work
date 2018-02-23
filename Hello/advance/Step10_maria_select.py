#-*- coding:utf-8 -*- 

import mysql.connector

#DB 접속 정보를 dict type 으로 준비한다.
config={
        'user':'root', #계정
        'password':'maria', #비밀번호
        'host':'127.0.0.1', #여기가 ip주소 
        'database':'mingu',
        'port':3306 # 포트번호는 3306 오라클일경우는 1521이였다.
    }

if __name__ == '__main__':
    
    try:
        #Maria DB 연결 객체 
        conn = mysql.connector.connect(**config) #dict type 을 풀어서 전달. 
        #dict로안하면 (user='root', password='maria'.....) 전부 써줘야한다. 
        
        cursor=conn.cursor() #java(oracle) 로 따지면 Preparedstatement
        #실행할 query 문
        sql="""
        select num,name,addr 
        from member 
        ORDER By num ASC
        
        """
        #여러줄의 쿼리문을 쓸때는 """xx""" or '''xx''' 사이에 작성한다. 한줄쓸때는 "" 이안에 쓴다.  주석으로 인식안하고 문자열로 인식해준다.
        #조건절은 oracle ? 이지만 python은 $s로 쓴다
        # query 문 수행
        cursor.execute(sql)
        # result 는 tuple 이 순서대로 들어 있는 list 이다. 
        result = cursor.fetchall()
        #java 로 치면(oracle) ResultSet
      
        for tmp in result:
            #tmp 는 select 된 row 정보가 들어 있는 tuple 이다.
            num=tmp[0] #select query문의 작성 순서대로 tuple 에 들어간다.
            name=tmp[1]
            addr=tmp[2]
            print u"번호:{}, 이름:{}, 주소:{}"\
                .format(num, name, addr)
        
    except Exception, e:
        print e 
    finally:
        conn.close()
        
    print "메인 메소드가 종료 됩니다."
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        