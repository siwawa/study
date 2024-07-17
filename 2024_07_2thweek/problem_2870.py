# 방코스 2주차 2870번 
import re  
number = int(input()) 
number_list = []  

for _ in range(number): 
    line = str(input()) 
    new_number_list = re.split(r'[a-z]', line) 
    # remove는 맨 처음 하나만 없앤다. 
    while '' in new_number_list: 
        new_number_list.remove('')          

    new_number_list = list(map(int, new_number_list))  
    number_list = number_list + new_number_list
 
# sort와 같은 in_place 메소드는 값을 반환하지 않고 객체를 직접 수정, 
# 바로 print 때려버리면 화낸다. ^^!! 
number_list.sort() 
for sorted_number in number_list: 
    print(sorted_number) 
