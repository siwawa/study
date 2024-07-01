# 방코스 1주차 10250 
questions = int(input())

for question in range(questions): 
    height, width, number = map(int, input().split()) 

    # 나누기 /는 진짜 나누기, float 줌. 나누기 //는 몫만 준다.  
    quotient = number//height
    remains = number%height 

    # 5명에 5층이면 나누어 떨어질때 몫이 1, 나머지가 0 나온다. 
    # 그러나 5층 1호가 되어야 하기에 예외처리해줘야 한다.   
    if remains == 0: 
        print(f"{height * 100 + quotient}")
    
    # 5명에 3층이면 나누어 떨어질때 몫이 1, 나머지가 2 나온다. 
    # 따라서 2층 2호가 된다. 
    else: 
        print(f"{remains * 100 + quotient + 1}")    

     

