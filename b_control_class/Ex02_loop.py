
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112                  # 숫자형
b = ['1','2','3']       # 리스트
c = '987'                # 문자열
d = tuple(b)# 튜플
#d= tuple(['1','2','3'])
e = dict(k=5, j=6)       # 딕셔너리

for entry in a: # a는 반복이 안되지만 b부터 e까지는 반복된다.
#    print(entry)


#딕셔너리인 경우
for entry in e:
    print(entry, e[entry])
else:print(end)




"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
