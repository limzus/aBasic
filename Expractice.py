'''1. 사용자로부터 5개의숫자를읽어서리스트에저장하고숫자들의평균을계산하여출력한다.
또숫자중에서평균을출력하여보자.
정수를입력하세요: 10
정수를입력하세요: 20
정수를입력하세요: 30
정수를입력하세요: 40
정수를입력하세요: 50
평균= 30.0
'''

numbers = input('정수리스트입력:')     #입력값 받아오기
nums = numbers.split()              #list로 변환
sum = 0.0                           #총합변수 선언
for i in range(len(nums)):          #총합 계산 #len:배열의원소개수 구하는 함수
    sum = sum + float(nums[i])

avg=sum/len(nums)                   #평균수 계산
'''
표준편차계산(수학문제)
aa = 0.0
for i in range(len(nums)):
    aa = aa + abs(float(nums[i])-avg)**2
bb = aa/(len(nums)-1)
bb=math.sqrt(bb)
print('평균= {}'.format(avg))
print('표준편차{:.2f}'.format(bb))
*
'''

2. 사용자에게서받은문자들을 역순으로 출력한다.
문자열입력: abcde
결과 :edcba



'''
3. 사용자에게서받은정수들의평균과표준편차를계산하여출력한다.
평균과표준편차를프로그램을 작성하세요
정수리스트입력: 10 20 30 40 50
평균= 30.0
표준편차 15.81


'arr = input('정수리스트 입력 : ').split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
d = int(arr[3])
e = int(arr[4])
sum = a+b+c+d+e
avg = sum / 5
print('평균 : ', avg)
bunsan = ( (a-avg)**2 + (b-avg)**2 + (c-avg)**2 + (d-avg)**2 + (e-avg)**2 )/5
print(bunsan)
pyuncha = bunsan ** (1/2)
print('표준편차 : ', pyuncha)

4. 전화 키패드에는 각 숫자키마다 3개의 문자가 적혀있다. 사용자가 입력한 문자열을 전화기의 숫자키로 변환하는 프로그램을 작성해보자.

문자열을입력하시오: NUMBER
686237
'''