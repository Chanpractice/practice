# 집합  (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # 중복을 허용하지 않음

java = {"유재석", " 김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합( java & python)

print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합 ( java ok python no)
print(java - python )
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남 list 에선 append()
python.add("김태호")
print(python)
#값을 빼고 싶은 경우 리스트에선 pop
python.remove("박명수")
print(python)