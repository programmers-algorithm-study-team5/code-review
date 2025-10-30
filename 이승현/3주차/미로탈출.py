from collections import deque
def solution(maps):
    visit = {maps[r][c]: (r, c) for r in range(len(maps)) for c in range(len(maps[0])) if maps[r][c] in "SEL"}
    d, R, C =  [(-1, 0), (0, -1), (1, 0), (0, 1)], len(maps), len(maps[0])
    def bfs(start, end):
        q, visited =deque([(*start, 0)]), set(start)
        while q:
            r, c, time = q.popleft()
            for dr, dc in d:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited and maps[nr][nc] != "X":
                    if maps[nr][nc] == end: return time + 1
                    visited.add((nr, nc))
                    q.append((nr, nc, time + 1))
        return 0
    return (a + b) if (a := bfs(visit["S"], "L")) and (b := bfs(visit["L"], "E")) else -1