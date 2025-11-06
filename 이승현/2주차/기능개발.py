def solution(progresses, speeds): 
    answer, day = [], 0
    for d in [abs((p - 100) // s) for p, s in zip(progresses, speeds)]: 
        if( d > day ): 
            answer += [1] 
            day = d 
        else: answer[-1] += 1 
    return answer