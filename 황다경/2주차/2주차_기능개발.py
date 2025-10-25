from collections import deque

def solution(progresses, speeds):
    days = [-((p-100) // s) for p, s in zip(progresses, speeds)]
    queue = deque(days)
    result = []
    
    while queue:
        current_day = queue.popleft()
        count = 1
        
        while queue and queue[0] <= current_day:
            queue.popleft()
            count += 1
            
        result.append(count)
    
    return result
