from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    maps = [list(row) for row in maps]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit_ = (i, j)
        
    def bfs(start, target):
        visited = [[False]*m for _ in range(n)]
        q = deque([(start[0], start[1], 0)])
        visited[start[0]][start[1]] = True
        
        while q:
            y, x, dist = q.popleft()
            
            if(y, x) == target:
                return dist
        
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and maps[ny][nx] != 'X':
                    visited[ny][nx] = True
                    q.append((ny, nx, dist + 1))
                
        return -1
    
    to_lever = bfs(start, lever)
    if to_lever == -1:
        return -1
    
    to_exit = bfs(lever, exit_)
    if to_exit == -1:
        return -1

    return to_lever + to_exit
