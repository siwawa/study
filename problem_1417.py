# 방코스 2주차 11655번 
number = int(input())
candidate_list = []

for i in range(number): 
    candidate_list.append(int(input())) 


candidate_list = list(map(lambda x: x)) 

candidate_list - [candidate_list[0]]*number 
print(candidate_list) 





