# 방코스 문제선정테스트 27160번  
card_number = int(input()) 
fruit_dict = {}
 
for i in range(card_number): 
    line = input()
    fruit, fruit_number = line.split()[0], int(line.split()[1])   
    
    if fruit_dict.get(fruit) != None: 
       fruit_dict[fruit] = fruit_dict.get(fruit) + fruit_number 

    else: 
        fruit_dict[fruit] = fruit_number 

fruit_numbers = list(fruit_dict.values()) 
if 5 in fruit_numbers: 
    print("YES")
else: 
    print("NO") 



