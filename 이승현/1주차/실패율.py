def solution(N, stages):
    result = {i : 0 for i in range(1, N + 2)}
    total = len(stages)
    for i in stages: result[i] += 1
    del result[len(result)]
    for i in range(1, N+1): result[i], total = (result[i] / total if total else 0), total - result[i]
    return sorted(result, key=lambda x : (-result[x], x) )