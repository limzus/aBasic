#Ex11_oracle_test

import cx_Oracle as oci # 에러떠도 냅둬! 그래도 구동될수있으니!

#
# [파이썬 + 디비 절차]
# 1.연결객체 얻어오기(Connection)
conn=oci.connect('scott/tiger@192.168.0.32:1521/xe')
print(conn.version)
# 2.sql 문장



sql = 'select * from emp'

# 3.cursor객체 얻어오기
cursor=conn.cursor()
c
