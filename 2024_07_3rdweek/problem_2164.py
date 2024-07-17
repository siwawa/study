# 방코스 7월 3주차 2164번
number = int(input()) 
card_list =  [i for i in range(1,number+1)]

def destroy(card_list): 
    return card_list[1:]

def move(card_list): 
    moved_card_list = card_list[1:] + [card_list[0]]
    return moved_card_list 


while True: 
    if len(card_list) == 1: 
        print(card_list[0])
        break 

    card_list = destroy(card_list)
    card_list = move(card_list) 





