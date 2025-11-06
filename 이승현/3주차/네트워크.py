def solution(n, computers):
    p = list(range(n))
    def union_find(i):
        if p[i] != i : p[i] = union_find(p[i])
        return p[i]
    for r in range(n):
        for c in range(n):
            if computers[r][c]: p[union_find(c)] = union_find(r)
    return len({union_find(i) for i in range(n)})