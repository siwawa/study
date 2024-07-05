# 방코스 2주차 11057 [!힌트사용!]  
# table[i][j]로 사용. i는 length, j는 마지막 자리(가장 큰 수)로 한다. 

length = int(input())
 
### table = [[0]*10]*(length+1) 로 하면, 각 행이 동일한 리스트 객체를 참조하게 된다. 
### 따라서 한 행을 변경하게 되면 모든 행이 동일하게 변경된다. 
table = [[0]*10 for i in range(length+1)] 

# 한 자리 오르막 수s는 10개, 모든 마지막 자리수에 대해 1개이다.     
table[1] = [1]*10  

for ith_length in range(2,length+1): 
    for digit in range(10): 
        for smaller_digit in range(digit+1): 
            table[ith_length][digit] = table[ith_length][digit] + table[ith_length-1][smaller_digit] 

print(sum(table[length])%10007) 




