# 방코스 7월 3주차 1874번 
def push(original_stack, making_stack): 
    making_stack = [original_stack[0]] + making_stack 
    return original_stack[1:], making_stack 

def push_and_pop(original_stack): 
    moved_original_stack = original_stack[1:] + [original_stack[0]] 
    return moved_original_stack 


length = int(input()) 
# 둘다 왼쪽부터 나감 [1,2,3,4..], [4,3,2,1.. ]   
original_stack = [i for i in range(1,length+1)]
making_stack = []  
wanted_stack = []
for _ in range(length): 
    wanted_stack = [int(input())] + wanted_stack 

for index in range(length): 
    pushpop_counter = 0  
    while True:   
        if original_stack[0] == wanted_stack[index]: 
            original_stack, making_stack = push(original_stack, making_stack) 
            print("+") 
            break 

        if original_stack[0] != wanted_stack[index]: 
            original_stack = push_and_pop(original_stack) 
            pushpop_counter = pushpop_counter + 1  
            print("+") 
            print("-")

            if pushpop_counter > length: 
                print("NO") 
                exit() 






