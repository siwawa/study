# 방코스 2주차 9625번 

number = int(input()) 
# 버튼을 number번 누를 시 A와 B의 개수는 number index의 [A,B]. 순서 상관없음 
table = [[0,0] for _ in range(number+1)]  
table[0][0] = 1 
table[0][1] = 0 

for i in range(1,number+1): 
    # A_n+1 = B_n  
    # B_n+1 = B_n + A_n
    table[i][0] = table[i-1][1] 
    table[i][1] = table[i-1][1] + table[i-1][0]

print(table[number][0], table[number][1])

