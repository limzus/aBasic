"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

     def 함수명(매개변수):
        수행할 문장들
"""

#(0) 인자도 리턴값도 없는 함수

def func():
    print('inside func')
func()
result = func() # None  (다른language에서는 불러오질못할텐데, 파이썬에서는 none값을 불러옴
print(result)

# 리턴값이 여러개 있는 함수
def func(arg):
    return arg+5, arg-5, arg*5 #파이썬에서는 리턴값이 여러개여도됨

result=func(10)
print(result)

a, b, c=func(10)
print(a, b, c)


# 위치인자 (positional argument)
def func(greeting, name):
    print(greeting, '!!!!', name, '님')

func('하이', '박길동')
func('홍길동','안녕')

#키워드인자
func(name='홍길동', greeting='안녕')

#인자의기본값
def func(greeting, name="홍길동"):
    print(greeting, '!!!!', name, '님')
func('하이', '박길동')
func('안녕', '김길동')



'''

#----------------------------------------------------------------
# (5) 위치 인자 모으기 (*)

첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다
'''
def func(a,b,c=0,*args): #*args는 변수명임 임의로정할수있음 *args는 튜플로받음 100이들어가든 몇이 들어가든 하나의 덩어리로 취급
    sum =a+b+c
    for i in args:
        sum+=i
    return

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))

# 키워드인자모으기
def func(a, b, c=100, *args,**kwargs):
    sum = a+b+c
    for i in args:
        sum += i
        for k in kwargs:
            sum+=kwargs[k]  #k는 키값
        return sum

print(func(10,20))
print(func(1, 2, 3))
print(func(1, 2, 3, 4, 5, 6))
print(func(1, 2, kor=10, eng=20))
print(func(1, 2, 3, 4, java=5, math=6, kor=7))
