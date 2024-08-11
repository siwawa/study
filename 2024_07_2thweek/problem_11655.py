# 방코스 2주차 11655번
string = input() 

small_alphabets = list("abcdefghijklmnopqrstuvwxyz"+"abcdefghijklmn")  
big_alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"+"ABCDEFGHIJKLMN") 
kaisar_dict = {}

for i in range(26): 
    kaisar_dict[small_alphabets[i]] = small_alphabets[i+13] 
    kaisar_dict[big_alphabets[i]] = big_alphabets[i+13] 

encripted_string = ''     
for char in list(string): 
    if kaisar_dict.get(char) != None: 
        encripted_string = encripted_string + kaisar_dict[char]  

    if kaisar_dict.get(char) == None: 
        encripted_string = encripted_string + char 

print(encripted_string) 




