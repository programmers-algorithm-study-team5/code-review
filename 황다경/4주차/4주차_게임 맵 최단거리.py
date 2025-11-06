from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    visited = [[False] * m for _ in range(n)]
    queue = deque([(0, 0, 1)])
    visited[0][0] = True
    
    while queue:
        x, y, distance = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return distance
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))
    
    return -1