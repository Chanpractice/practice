# 자료구조의 변경 
menu = {"커피", "우유", "주스"}

print(menu, type(menu)) # 세트로 바꿈

menu = list(menu) #리스트로 바꿈
print(menu, type(menu)) 

menu = tuple(menu)
print(menu,type(menu))

menu = set(menu)
print(menu, type(menu))