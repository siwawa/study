# 방코스 2주차 1817번 

### 킹받아서 그냥 안 풀었음. 
### 포장을 닫은 박스를 다시 열어서 짐을 쌀 수 있다는 가정 하에 풀었음. 
### 백준 문제의 의의는 포장 닫은 박스를 다시 열 수 없다는 가정임.. ㅋㅋ 개짜치네; 나대로간닷  
first_line = input()
number, maximum_weight = map(int, first_line.split())  

if number == 0: 
    print(0) 
    exit()  

second_line = input() 
books = list(map(int, second_line.split()))

# 상자 최대 숫자는 책의 개수이다. 
boxes = [0] * number
for book in books: 
    boxes.sort(reverse=True) # 무거운 박스부터 책 넣기를 시도해본다!  
    for box_index, box in enumerate(boxes): 
        if (box + book) <= maximum_weight: 
            # box = box + book 는 리스트를 다시 바꿔주지 않는다! 
            # box는 boxes의 요소를 복제한 임시 변수일 뿐이다.  
            boxes[box_index] = box + book   
            break 

box_number = 0 
for box in boxes: 
    if box != 0: 
        box_number = box_number + 1         

print(box_number) 