def solution(maps):
    n, m = len(maps), len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    results = []
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                stack = [(i, j)]
                visited[i][j] = True
                total = 0
                
                while stack:
                    x, y = stack.pop()
                    total += int(maps[x][y])
                    
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny <m and not visited[nx][ny] and maps[nx][ny] != 'X':
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                
                results.append(total)
                
    return sorted(results) if results else [-1]