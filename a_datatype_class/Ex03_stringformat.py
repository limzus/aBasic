
# -----------------------------------------
#  문자열 포맷
#       0- 문자열 포맷팅
#               print('내가 좋아하는 숫자는 ', 100 )
#       1- format() 이용
#               print('내가 좋아하는 숫자는 {0:d} 이다'.format(100) )
#       2- % 사용
#               print('내가 좋아하는 숫자는 %d 이다' % 100 )
#       성능(속도)는 %이 더 빠르다고는 하지만 코드가 깔끔하게 하는 것이 더 중요하다고 하고는
#       어느 것으로 선택하라고는 안 나옴


# format()이용


# [참고] http://pyformat.info

# % 이용 - printf() 역할
name = '홍길동'
age = 22
height = 170.456
print('이름: {0}, 나이 : {1}, 키:{2:.1f}'.format(name,age,height))

print('이름: %s 나이 : %d, 키 : %.1f' % (name,age, height))



#--------------------------------------------------
# 실수인 경우



a=11
b=9

print('a' + 'b')


fact="python is funny"

class_name = 'introduction programming with python'

for i in class_name:

    if i == 'python':
        i = i.upper()

print(class_name)

input('나이를 입력하세요')

age = int(input('나이를 입력->'))
age +=1
print('나이:',age)

# eval
height = int(input('키를입력->'))
print('키 :',height)
print(type(height))


cal = int(input('원하는 단을 입력'))
for i in range(10):
#for i in range(1:9):
    print(' {0} * {1} = {2}'.format(cal, i, cal*i))
    """
# print() 함수
print('안녕'+'친구')

for i in range(5):
    print(i)

for i in range(5):
    print(i, end= '/')

for i in range(5):
    print(i, end='/')

print()
for i in range(5):
    print(i, end='/' if i<4 else "")

    # --------------------------------
    # 명령행 매개변수 받기 - java의 main() 함수의 인자
    # java 클래스명 문자열 1 문자열 2
    #                      [0]  [2]

    # [콘솔에서 실행
    # python Ex10_stdio.py ourserver scott tiger
                    0       1          2    3
    # 1. 사용자로부터 5개의숫자를읽어서리스트에저장하고숫자들의평균을계산하여출력한다.
# 또숫자중에서평균을출력하여보자.
# 정수를입력하세요: 10
# 정수를입력하세요: 20
# 정수를입력하세요: 30
# 정수를입력하세요: 40
# 정수를입력하세요: 50
# 평균= 30.0

number='정수를 입력하세요'

number=int(input('정수를입력하세요'))
for i in range(5)


print(number/4)

# 2. 사용자에게서받은문자들을 역순으로 출력한다.
# 문자열입력: abcde
# 결과 :edcba

# 3. 사용자에게서받은정수들의평균과표준편차를계산하여출력한다.
# 평균과표준편차를프로그램을 작성하세요
# 정수리스트입력: 10 20 30 40 50
# 평균= 30.0
# 표준편차 15.81

"""



