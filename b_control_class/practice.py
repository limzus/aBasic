#1. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?

mylist = ['apple' ,'banana', 'grape']
result = list(enumerate(mylist))
print(result)
"""
➀ [('apple', 1), ('banana', 2), ('grape', 3)]
➁ [(1, 'apple'), (2, 'banana'), (3, 'grape')]
➂ [(0, 'apple'), (1, 'banana'), (2, 'grape')]
➃ [('apple', 0), ('banana', 1), ('grape', 2)]
➄ [('grape',0), ('banana',1), ('apple',2)]
"""

#2. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
"""cat_song = "my cat has blue eyes, my cat is cute"
print({i:j for j,i in enumerate(cat_song.split())})
➀ {0: 'my', 1: 'cat', 2: 'has', 3: 'blue', 4: 'eyes,', 5: 'my', 6: 'cat', 7: 'is', 8: 'cute'}
➁ {'my': 0, 'cat': 1, 'has': 2, 'blue': 3, 'eyes,': 4, 'my': 5, 'cat': 6, 'is': 7, 'cute': 8}
➂ {0: 'my', 1: 'cat', 2: 'has', 3: 'blue', 4: 'eyes,', 5: 'is', 6: 'cute'}
➃ {'my': 5, 'cat': 6, 'has': 2, 'blue': 3, 'eyes,': 4, 'is': 7, 'cute': 8}
➄ 오류
"""
