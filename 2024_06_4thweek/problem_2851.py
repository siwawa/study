# 방코스 1주차 2851 
scores = [] 
score = 0  
for i in range(10): 
    mushroom = int(input()) 
    score = score + mushroom 
    scores.append(score) 

# 마지막 문제라 가독성 개판 
costs = list(map(lambda x: abs(x-100), scores)) 

best_choice_indices = list(filter(lambda x: costs[x] == min(costs), range(len(costs))))  
best_scores = list(map(lambda x: scores[x], best_choice_indices))

print(max(best_scores))
