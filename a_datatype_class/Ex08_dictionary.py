"""
    [ dictionary 형 ]

    1- 키와 값으로 구성 ( 자바의 map 와 유사 )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호 {} 사용
    4- 변경가능

    ` 사전.keys() : key만 추출 (임의의 순서)
    ` 사전.values() : value만 추출 (임의의 순서)
    ` 사전.items() : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1:'one', 2:'two', '3':'three'}
print(dt)
print(dt[1])
#print(dt[3])   #오류
print(dt['3'])


# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의  값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스트는 안된다
dt2 = {1:'one', 2:'two', (3,4):'turple'}
#print(dt[(3,4)]) ###################### 이따 한번 더 보자 아직 못해결했다.
# 'turple' -> 'pythin'
dt2[(3,4)] = 'python'
print(dt2)

print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
# 딕셔너리에 값 추가 및 수정
dt2['korea'] = 'seoul'
print(dt2)
dt2['korea'] = '한국'
# 'seoul' ->'한국'



# 여러개 추가할 때
dt2.update({5:'five',6:'six'})
print(dt2)


print('--------- 3. Key로 Value값 찾기  --------------- ')
print(dt2.keys())
print(dt2.values())
print(dt2.items()) # items는 키값을 리스트로 여러개의값으로 뽑는녀석.





# Key와 Value만 따로 검색
#자료형정리문제1:나
#자료형정리문제2:
a = [3, "apple", 2016, 4]
b = a.pop(0)
c = a.pop(1)
print(b + c)

#3
dict_1 = {2:1, 4:2, 6:3, 8:4, 10:6}
dict_keys = list(dict_1.keys())
dict_values = list(dict_1.values())
dict_2 = dict()
for i in range(len(dict_keys)):
	dict_2[dict_values[i]] = dict_keys[i]

print(dict_2[2])

#4
animal = ['cat', 'snake', 'monkey', 'ant', 'spider']
legs= [4, 0, 2, 4, 8]
animal_legs_dict = {}
for i in range(len(animal)):
	animal_legs_dict[legs[i]] = animal[i]
	animal_legs_dict['ant'] = 6
**-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print(animal_legs_dict)
