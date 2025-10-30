def is_valid(s):
    stack = []
    pair = {')':'(', ']':'[', '}':'{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or stack[-1] != pair[char]:
                return False
            stack.pop()
    return len(stack) == 0

def solution(s):
    n = len(s)
    count = 0
    
    for i in range(n):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            count += 1
    
    return count
