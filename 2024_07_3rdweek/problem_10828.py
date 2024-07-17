# 방코스 7월 3주차 10828번 
class Stack:
    def __init__(self): 
        self.name = []         

    def push(self, string):
        x = int(string.split()[1])
        self.name = self.name + [x]    

    def size(self): 
        print(len(self.name))

    def pop(self):
        result = self.name.pop(len(self.name)-1) 
        print(result)  

    def empty(self): 
        if self.name == []: 
            print(1)
        else: 
            print(0)  

    def top(self): 
        print(self.name[len(self.name)-1])  

number = int(input()) 
stack = Stack() 

for _ in range(number): 
    stack.input() # ??? 



