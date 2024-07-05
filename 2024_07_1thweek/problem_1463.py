# 방코스 2주차 1463 
number = int(input()) 
table = [0] * (number + 1) 
table[1] = 0 # 1은 아무 시행도 안해도 된다.  

for i in range(2, number+1): 
    if (i%3 == 0) and (i%2 == 0): 
        table[i] = min(table[i//3], table[i//2], table[i-1]) + 1   
    elif i%2 == 0:  
        table[i] = min(table[i//2], table[i-1]) + 1  
    elif i%3 == 0: 
        table[i] = min(table[i//3], table[i-1]) + 1   
    else: 
        table[i] = table[i-1] + 1 


print(table[number])  

    


