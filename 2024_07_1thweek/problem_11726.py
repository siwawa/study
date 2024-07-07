# 방코스 2주차 11726 
# 2*n의 직사각형은  
# 가장 왼쪽의 직사각형이 | 인 경우는 2*(n-1) 직사각형을 채우는 경우와 같다. 
# 가장 왼쪽의 직사각형이 = 인 경우는 2*(n-2) 직사각형을 채우는 경우와 같다. 

import time 
start_time = time.time() 

number = int(input())
table = [0] * (number + 1) 

# 이 if문이 없다면 number = 1일때 인덱스에러가 뜬다. 킹받네. 
if number == 1: 
    print(1) 

if number > 1: 
    table[1] = 1  # n=1 일때는 1가지이다.  
    table[2] = 2  # n=2 일때는 2가지이다. 
    for i in range(3, number+1): 
        table[i] = table[i-1] + table[i-2] 

    print(table[number]%10007)  

end_time = time.time()
execution_time = end_time - start_time
print(execution_time) 

