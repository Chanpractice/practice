from random import *
# Way 1
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(lst)
# A = sample(lst,1)
# print(A[0])
# lst.remove(A[0])
# print(lst)
# print("-- 당첨자 발표--")
# print("치킨 당첨자 : " , A[0])
# print("커피 당첨자 : ", sample(lst,3))
# print("-- 축하합니다 --")
# Way 2
lst = range(1,21)
lst = list(lst)
shuffle(lst)
A = sample(lst,4)
print("chicken : ", A[0])
print("chicken : ", A[1:])
# Teacher sol

users = range(1,21) # 1부터 20까지 숫자를 생성
users = list(users)
shuffle(users)

winners = sample(users,4) # 4명 중 1명은 치킨, 3명은 커피

print("-- 당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")
