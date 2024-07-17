# 방코스 2주차 9996번
def reverse(string): 
    reverse_string = ""
    for char in string: 
        reverse_string = char + reverse_string 
    return reverse_string 



number = int(input()) 
pattern = input().split('*') 
front_pattern = pattern[0]
back_pattern = pattern[1]  

for _ in range(number): 
    file = input() 
    reversed_file = reverse(file) 
    reversed_back_pattern = reverse(back_pattern)

    if file.find(front_pattern) != 0: 
        print("NE") 

    elif reversed_file.find(reversed_back_pattern) != 0: 
        print("NE") 

    else: 
        print("DA") 


    
     






