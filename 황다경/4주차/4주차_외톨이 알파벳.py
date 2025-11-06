def solution(input_string):
    result = []
    seen_chars = set()
    
    for idx, char in enumerate(input_string):
        if idx == 0:
            seen_chars.add(char)
        elif char in seen_chars:
            if char != input_string[idx - 1]:
                result.append(char)
        else:
            seen_chars.add(char)
    
    if result:
        return ''.join(sorted(set(result)))
    return 'N'