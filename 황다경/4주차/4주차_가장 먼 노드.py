from collections import deque, defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    distances = [-1] * (n + 1)
    queue = deque([1])
    distances[1] = 0
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    
    max_distance = max(distances)
    return distances.count(max_distance)
