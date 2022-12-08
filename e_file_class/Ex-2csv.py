# Ex02_csv.py
# csv 파일 -> 엑셀에서 열림 + 일반 에디터에서 열림
#Common String Value 문자만 갖고있는 파일

data = [[1,'김','책임'],
        [2,'박','선임'],
        [3,'맹','연구원']]
import csv
# with open('./data/imsi.csv','wt',encoding='utf-8') as f: # t는 디폴트값이라 안 줘도됨 -> w
#     #f.write(data)
#     cout=csv.writer(f)    //writer는 통로 저장하는 수단
#     cout.writerows(data) # 자동으로 개행도 붙는구나옹

result=[]
with open('./data/imsi.csv','rt',encoding='utf-8') as f:
    cin=csv.reader(f)
    result=[row for row in cin if row]
    print(result)
