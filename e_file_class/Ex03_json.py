f= open('./data/temp.json','rt',encoding='utf-8')
data=f.read()
f.close()

print(data)
print(type(data))

import json
items = json.loads(data)

print(items)
print(type(items))

for k,val in items.items():
        print(k,'>',val)
        print(k,'>>',val['Job']) #이해안되옹 이따 설명이 필요하당

