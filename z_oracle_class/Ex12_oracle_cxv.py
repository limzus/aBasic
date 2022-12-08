# [ 파이썬 + 디비 절차 ]
# 1. 연결객체 얻어오기(Connection)
# 2. sql 문장
# 3. cursor 객체 얻어오기
# 4. 실행
# 5. cursor 객체 닫기
# 6. 연결객체 닫기
import cx_Oracle as oci
import csv

def createDBTable():
    # 1. 연결객체 얻어오기(Connection)
    # 계정명 / 비밀번호 / @ / IP / 오라클 포트번호 / xe
    conn = oci.connect('scott/tiger@192.168.0.32:1521/xe')
    print(conn.version)
    # 2. sql 문장
    sql = '''
        CREATE TABLE supply
        (
            id              number primary key,
            Supplier_Name   varchar2(50),
            Invoice_Number  varchar2(50),
            Part_Number     varchar2(50),
            Cost            number,
            Purchase_Date   date
        )
    '''
    # 3. cursor 객체 얻어오기
    cursor = conn.cursor()
    # 4. 실행
    cursor.execute(sql)
    sql2 = 'create sequence seq_supply_id'
    cursor.execute(sql2)
    # 5. cursor 객체 닫기
    cursor.close()
    # 6. 연결객체 닫기
    conn.close()

def saveDBTable(data):
    # 1. 연결객체 얻어오기(Connection)
    conn = oci.connect('scott/tiger@192.168.0.32:1521/xe')
    # 2. sql 문장
    sql = '''
    INSERT INTO supply
    VALUES(seq_supply_id.NEXTVAL, :0,:1,:2,:3,:4)
    '''
    # 3. cursor 객체 얻어오기
    cursor = conn.cursor()
    # 4. 실행
    cursor.execute(sql, data)
    # 5. cursor 객체 닫기
    cursor.close()
    # commit 잊지말자
    conn.commit()
    # 6. 연결객체 닫기
    conn.close()

def viewDBTable(tableName):

    # 넘겨받은 테이블명의 데이타를 화면에 출력
    # 연결객체 얻어오기
    conn = oci.connect('scott/tiger@192.168.0.32:1521/xe')


    sql='select * from'+tableName
    cursor = conn.cursor()
    cursor.execute(sql)
    datas= cursor.fetchall()
    for data in datas:
        print(data)
    cursor.close()
    conn.close()

    return datas



if __name__ =='__main__':
    # (1) 테이블 생성
    #createDBTable()

    # # (2) 입력 확인
    # imsi =['kosmo', '9999', '8888', 1000, '2022-12-08']
    # # print(datas)
    # header=next(datas,None)
    # print(header)
    # print('-'*50)
    #
    # file = open('supply.csv', 'r')
    # datas = csv.reader(file)
    # for row in datas:
    #     #print(row)
    #     saveDBTable(row)


    #3
    datas = viewDBTable('supply')