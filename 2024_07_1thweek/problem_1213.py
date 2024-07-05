# 방코스 2주차 1213 
def make_one_hot(string): 
    one_hot_table = [0] * 26   
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    alphabet_dict = {alphabet: index for index, alphabet in enumerate(alphabets)}
    
    for alphabet in list(string): 
        index = alphabet_dict[alphabet] 
        one_hot_table[index] = one_hot_table[index] + 1  
    return one_hot_table 


def reverse(string): 
    temp = list(string) 
    reverse_string = ''

    for i in range(1, len(temp)+1): 
        reverse_string = reverse_string + temp[len(temp)-i]  
    return reverse_string 



name = input() 
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'   
 
# 원핫방식으로 1*26의 list에 각 위치에 해당하는 알파벳의 등장횟수를 기록한다. AA이면 [2,0,0,..]
one_hot_table = make_one_hot(string = name) 
palindrome_front = ''
palindrome_back = ''

# 총 길이 짝수일 때 홀수가 있으면 안된다. 
if len(name)%2 == 0: 
    for alphabet_number in one_hot_table: 
        if alphabet_number%2 != 0: 
            print("I'm Sorry Hansoo")
            exit() 
        
    for index, alphabet_number in enumerate(one_hot_table): 
        palindrome_front = palindrome_front + list(alphabets)[index] * (alphabet_number//2)  
        
    palindrome_back = reverse(palindrome_front) 
    print(palindrome_front + palindrome_back) 

# 총 길이 홀수일 때 홀수는 한번만 허용한다.  
if len(name)%2 != 0: 
    odd_number = 0 
    for alphabet_number in one_hot_table: 
        if alphabet_number%2 != 0: 
            odd_number = odd_number + 1 
        
        if odd_number > 2: 
            print("I'm Sorry Hansoo") 
            exit()
    
    for index, alphabet_number in enumerate(one_hot_table):
        if alphabet_number%2 == 0: 
            palindrome_front = palindrome_front + list(alphabets)[index] * (alphabet_number//2)  

        # 홀수 알파벳은 하나를 제외하고 짝수와 똑같이 취급한다. 차후에 가운데에 홀수 알파벳을 넣어준다. 
        if alphabet_number%2 != 0: 
            odd_alpahbet_index = index 
            palindrome_front = palindrome_front + list(alphabets)[index] * ((alphabet_number-1)//2)  
                    
    palindrome_back = reverse(palindrome_front)  
    print(palindrome_front + list(alphabets)[odd_alpahbet_index] + palindrome_back)

    

        
    