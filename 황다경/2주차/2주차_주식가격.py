from collections import deque

def solution(prices):
    q = deque(prices)
    answer = []
    
    while q:
        current = q.popleft()
        count = 0
        
        for next_price in q:
            count += 1
            if next_price < current:
                break
        
        answer.append(count)
    
    return answer
