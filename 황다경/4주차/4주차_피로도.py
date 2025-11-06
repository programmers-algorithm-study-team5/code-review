def solution(k, dungeons):
    max_count = 0
    n = len(dungeons)
    visited = [False] * n
    
    def dfs(current_fatigue, count):
        nonlocal max_count
        max_count = max(max_count, count)
        
        for i in range(n):
            if not visited[i]:
                min_required, consumption = dungeons[i]
                
                if current_fatigue >= min_required:
                    visited[i] = True
                    dfs(current_fatigue - consumption, count + 1)
                    visited[i] = False
    
    dfs(k, 0)
    return max_count