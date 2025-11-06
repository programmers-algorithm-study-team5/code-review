from collections import deque

def solution(n, m, hole):
    traps = set((x, y) for x, y in hole)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    visited = [[[False] * (m + 1) for _ in range(n + 1)] for _ in range(2)]
    
    queue = deque([(1, 1, 0, 0)])
    visited[0][1][1] = True
    
    while queue:
        x, y, time, shoe_used = queue.popleft()
        
        if x == n and y == m:
            return time
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            

            if 1 <= nx <= n and 1 <= ny <= m and (nx, ny) not in traps:
                if not visited[shoe_used][nx][ny]:
                    visited[shoe_used][nx][ny] = True
                    queue.append((nx, ny, time + 1, shoe_used))
        

        if shoe_used == 0:
            for dx, dy in directions:
                nx, ny = x + 2 * dx, y + 2 * dy
                
                if 1 <= nx <= n and 1 <= ny <= m:
                    if (nx, ny) not in traps and not visited[1][nx][ny]:
                        visited[1][nx][ny] = True
                        queue.append((nx, ny, time + 1, 1))
    
    return -1
