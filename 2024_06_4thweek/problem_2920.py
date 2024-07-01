# 방코스 1주차 2920 
songs = list(map(int, input().split())) 
ascending = True
descending = True 
mixed = False 
print(songs)

for i in range(8): 
    if songs[0] != max(songs): 
        descending = False 
    if songs[0] != min(songs): 
        ascending = False 
    del songs[0] 


if ascending == True: 
    print("ascending") 
elif descending == True: 
    print("descending")
elif ascending == False & descending == False: 
    mixed = True 
    print("mixed")


# if input() == "1 2 3 4 5 6 7 8": 
#     print("ascending") 이왜진???  

