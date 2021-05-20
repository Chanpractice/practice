# # 리스트 []

# 지하철 칸별로 10명, 20명, 30명

# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10,20,30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# #조세호가 몇번째 칸에 타고있는가
# print(subway.index("조세호")) # 0부터 시작이므로 1이 맞다

# # 다음 정류장에서 하하가 탈경우
# subway.append("하하") # 뒤에 추가
# print(subway)

# #정형돈을 유재석  / 조세호 사이에 태워봄
# subway.insert(1, "정형돈") # index, data 삽입
# print(subway)

# #지하철에 있는 사람을 한 명 씩 뒤에서 꺼냄
# print(subway.pop()) # 꺼내는것
# print(subway)


# # 같은 이름의 사람이 몇명 있는지 확인하기
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석")) # 몇번 나오는지 count 가능

# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort() # 정렬하는 함수
# print(num_list)

# # 뒤집기도 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용 가능
# mix_list = ["조세호", 20 , True]
# # print(mix_list) 
# num_list = [5,2,4,3,1]

# num_list.extend(mix_list)
# print(num_list)  # 두 개의 리스트를 합치는 것

# # list 를 그대로 적기 가능 
# # append : 리스트 뒤에 태우기 insert : 원하는 위치에 삽입 가능
# # 사용 예시 function.insert(1, "data")
# # pop : 뒤에서 부터 list의 값을 빼는것
# # 리스트 정렬가능 -> sort() : 순서대로 정렬, reverse() : 거꾸로 정렬
# # clear() : 모든 리스트 지우기 가능
# # 자료형 2개를 삽입하는 방법 -> extend(next_list) 확장 가능하다!

