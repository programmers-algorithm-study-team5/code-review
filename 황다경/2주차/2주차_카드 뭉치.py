from collections import deque

def solution(cards1, cards2, goal):
    q1 = deque(cards1)
    q2 = deque(cards2)
    
    for word in goal:
        if q1 and word == q1[0]:
            q1.popleft()
        elif q2 and word == q2[0]:
            q2.popleft()
        else:
            return "No"
    
    return "Yes"
