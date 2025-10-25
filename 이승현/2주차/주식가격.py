def solution(prices):
    stack, answer = [], [0]*len(prices)
    for i, p in enumerate(prices):
        while stack and p < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    for j in stack:
        answer[j] = len(prices) - j - 1
    return answer