# 방코스 2주차 2748  
number = int(input()) 
fib = [0] * (number + 1)

fib[0] = 0 
fib[1] = 1 

# 0번1번2번...   
# 0, 1, 1, 2, 3, 5, 8, 13... 
for i in range(2,number+1): 
    print(i, i-1, i-2)
    fib[i] = fib[i-1] + fib[i-2]

print(fib[number]) 