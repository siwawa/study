# 7월 2주차 방코스 9655번 
number = int(input()) 

# 4n+1, 4n+3을 만들면 먼저 하는 사람이 이긴다.  
# 가장 먼저 1이나 3을 가져가면 4의배수가 되는데, 상대가 1개나 3개 가져갈때마다 3개나 1개를 가져가는 것으로 응수한다.  
# 4n+2, 4n을 만들면 나중에 하는 사람이 이긴다. 4n+1, 4n+3의 형태를 만들수있기 때문이다. 
remains = number%4 
if (remains == 1) or (remains == 3): 
    print("SK") 
if (remains == 2) or (remains == 0): 
    print("CY") 
