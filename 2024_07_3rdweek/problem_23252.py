# 방코스 7월 3주차 23252번 
first_line = input().split()
book_number, stack_number = map(int, first_line) 

stacks = []  
# 입력된 책 더미들을 표현하는 2차원 배열을 만든다. [[더미],[더미]..]
for stack in range(stack_number): 
    unused_variable = input() 
    line_per_stack = input().split()
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
            print("No") 
            exit()

    if next_book == book_number: 
        print("Yes") 
        exit()
                     
        

