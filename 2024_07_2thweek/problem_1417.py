# 방코스 2주차 11655번 
def steal_votes(dasom, candidate_list):  
    best_candidate_index = candidate_list.index(max(candidate_list))  
    dasom = dasom + 1 
    candidate_list[best_candidate_index] = candidate_list[best_candidate_index] - 1 
    
    return dasom, candidate_list 



number = int(input())
candidate_list = []

for i in range(number): 
    candidate_list.append(int(input()))  

stealing = 0 
dasom = candidate_list[0] 
candidate_list = candidate_list[1:] 

if number == 1: 
    print(0) 
    exit()

while True:     
    if max(candidate_list) < dasom: 
        print(stealing) 
        break 

    stealing = stealing + 1
    dasom, candidate_list = steal_votes(dasom, candidate_list) 
   
 





