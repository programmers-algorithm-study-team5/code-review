def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    scores = [0, 0, 0]
    result = []
    
    for i, answer in enumerate(answers):
        for j in range(3):
            if answer == patterns[j][i%len(patterns[j])]:
                scores[j] += 1
    
    max_score = max(scores)
    
    for i in range(3):
        if scores[i] == max_score:
            result.append(i + 1)
    
    return result
