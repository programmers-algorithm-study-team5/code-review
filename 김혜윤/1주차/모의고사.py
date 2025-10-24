def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    patterns = [student1, student2, student3]
    scores = [0, 0, 0]

    for i, a in enumerate(answers):
        if patterns[0][i % len(patterns[0])] == a: scores[0] += 1
        if patterns[1][i % len(patterns[1])] == a: scores[1] += 1
        if patterns[2][i % len(patterns[2])] == a: scores[2] += 1

    max_score = max(scores)
    return [i + 1 for i, s in enumerate(scores) if s == max_score]
