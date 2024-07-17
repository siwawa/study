# 방코스 2주차 2002번
number = int(input()) 
before_list = [] 
after_list = [] 

for _ in range(number): 
    # 터널에 들어간 순서의 list 
    before_list.append(input()) 
for _ in range(number): 
    # 터널에서 나온 순서의 list 
    after_list.append(input()) 



illegal = 0 
while True: 
    for index in range(number): 
        before_index = index
        after_index = after_list.index(before_list[index]) 

        # index가 줄어들면(순위가 앞으로 갔다는 뜻은) 이유불문 차선 변경이다. 불법!!! 
        # 차선변경을 한 차를 두개 list에서 모두 제외하고, 터널에 들어간 순서의 list와 나온 순서 list가 같을때까지 반복한다.  
        if after_index < before_index: 
            illegal = illegal + 1 

            # pop del 차이 복습해야 한다.  
            before_list.pop(before_index) 
            after_list.pop(after_index)  
            break 
    
    if before_list == after_list: 
        break

print(illegal) 

        


 
