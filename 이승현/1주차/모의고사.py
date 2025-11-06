def solution(answers):
    num = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    answer = [0, 0, 0]
    for i in range(len(answers)):
        for j in range(3):
            if num[j][i % len(num[j])] == answers[i] : answer[j] += 1
    return [i + 1 for i in range(len(answer)) if answer[i] == max(answer)]