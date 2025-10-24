def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        sub=array[i-1:j]
        sub.sort()
        answer.append(sub[k-1])
        
    return answer
