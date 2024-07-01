# 방코스 1주차 1292 
minnum, maxnum = map(int, input().split())
minnum = minnum - 1 # 합 구할때 포함, 마지막에 빼줄때 제외해야함  

# 1+2+3+4.. 
def add_up_to(number): 
    sum = 0 
    for i in range(number+1): # number 자기자신 포함 
        sum = sum + i 
    return sum  

# 1+2+2+3+3+3.. 
def sum_up_to(number): 
    sum = 0 
    for i in range(number+1): 
        sum = sum + i*i
    return sum 


minnum_sum = 0
maxnum_sum = 0

# 50 * 50 = 2500 > 2000 > maxnum 
for i in range(1,50): 
    before_ith_interval = add_up_to(i) 
    after_ith_interval = add_up_to(i+1) 

    if before_ith_interval <= minnum < after_ith_interval: 
        minnum_sum = sum_up_to(i) + (i+1)*(minnum-before_ith_interval)
        
    if before_ith_interval <= maxnum < after_ith_interval: 
        maxnum_sum = sum_up_to(i) + (i+1)*(maxnum-before_ith_interval)

print(maxnum_sum-minnum_sum)

        













