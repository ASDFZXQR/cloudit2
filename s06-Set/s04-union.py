# 세트의 합집합
# 연산자 : |
# 메소드 : set.union(...)

s1 = set("13579")
s2 = set("12468")

# 합집합 : |
# 중복되는 요소는 하나만 선택
s3 = s1 | s2

print(s1) # {'1', '7', '9', '5', '3'}
print(s2) # {'1', '4', '2', '6', '8'}
print(s3) # {'1', '4', '7', '2', '6', '9', '5', '3', '8'}

#%%

s4 = s1.union(s2)
print(s4) # {'1', '4', '7', '2', '6', '9', '5', '3', '8'}