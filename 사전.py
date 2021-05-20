cabinet = {3:"유재석", 100:"김태호"} # key와 value
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) #.get을 써서 값을 넣고 가져오기 가능

#주의할점
# # print(cabinet[5]) #값이 없다고 하고 오류가 뜸
# print(cabinet.get(5))  #none 이하고 뜸
# print(cabinet.get(5,"사용가능")))
# print("hi")

print(3 in cabinet) #True
print(5 in cabinet) #False

cabinet = {"A-3":"유재석", "B-100":"조세호"}
print(cabinet["A-3"])
print(cabinet.get("A-3"))

# 새 손님이 온 경우
print(cabinet)
cabinet["A-3"] = "김종국" # 새 값으로 대체함
cabinet["C-20"] = "조세호" # 값을 추가하는 경우
print(cabinet)

# 간 손님

del cabinet["A-3"]
print(cabinet)

#key 들만 출력

print(cabinet.keys())
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)


# 사전에는 특정 key 와 value를 설정할 수 있어 
dic = {3:"value"}
dic[1] = "new"

print(dic)

dic[3] = "new2"
print(dic)

print(dic.get(3))
print(dic.get(2,"need data"))

dic[2] = "new3"

print(dic) 

print(dic.keys())
print(dic.values())
print(dic.items()) # keys, values 를 나타냄
print(dic.clear()) # 모든 key, values 를 지운다.