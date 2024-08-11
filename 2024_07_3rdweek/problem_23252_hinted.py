# 방코스 7월 3주차 23252번 
from sys import stdout 
from sys import stdin

first_line = stdin.readline().rstrip().split()
book_number, stack_number = map(int, first_line)  
possible = True 

for _ in range(stack_number): 
    unused_input = stdin.readline()  
    line_per_stack = stdin.readline().rstrip().split()  
    stack = list(map(int, line_per_stack)) 

    # "가능한지" 만 확인하면 되기 때문에 문제를 바꾸어 생각한다. 
    # 각 stack가 내림차순인지 [5, 4, 3, 2, 1] 확인하는 것과 같다. 
    descending_stack = sorted(stack, reverse = True)   

    # 파이썬에서 "="는 해당 객체를 복제하지 않고, 해당 객체를 가리키는 포인터를 하나 더 만든다. 
    # 따라서 내가 아래 방법으로 복제 & sort를 때리면 무조건 yes 뜬다. 
    # descending_stack = stack
    # descending_stack.sort(reverse = True)      
    # remind: is는 주소를 비교하는 연산, ==가 값을 비교하는 연산 
    if descending_stack != stack: 
        possible = False  
         
# print 결과는 True/False로 나오면 안된다.. 나쁜사람들이다.. 
print("Yes" if possible else "No") 

"""
first_line = stdin.readline().rstrip().split()
book_number, stack_number = map(int, first_line) 

stacks = []  
# 입력된 책 더미들을 표현하는 2차원 배열을 만든다. [[더미],[더미]..]
for stack in range(stack_number): 
    unused_input = stdin.readline() # 책 list로 저장, 필요없는 input 
    line_per_stack = stdin.readline().rstrip().split() 
    stacks.append(list(map(int, line_per_stack))) 


top_books = []
next_book = 1  

while True: 
    # 더미들의 가장 위에(배열상에서 뒤에)있는 책을 pop으로 꺼내 없애고, 
    # top_books list로 만든다. 
    for stack in stacks: 
        top_book = stack.pop(len(stack)-1)     
        top_books.append(top_book)   
    
    # top_books list에서 순서에 맞는(next_book) 책을 하나씩 뺀다. 
    for top_book in top_books: 
        try: 
            top_books.remove(next_book)   
            next_book = next_book + 1  
        # pop는 list안에서 못 찾으면 -1 리턴, remove는 못 찾으면 valueerror. 
        except: 
            stdout.write("No") 
            exit()

    if next_book == book_number: 
        stdout.write("Yes") 
        exit()
"""                     
        

