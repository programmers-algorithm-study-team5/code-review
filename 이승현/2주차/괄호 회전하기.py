from collections import deque
def solution(s):
    q, answer = deque(s), 0
    p = {']': '[', ')': '(', '}': '{'}
    for _ in range(len(s)):
        stack = []
        for ch in q:
            if ch in p:
                if not stack or stack.pop() != p[ch] : break
            else : stack.append(ch)
        else: answer += not stack
        q.rotate(-1)
    return answer