def solution(board, moves):
    board = [list(filter(None, row[::-1])) for row in zip(*board)]
    answer, stack = 0, []
    for m in moves:
        if not board[m-1]: continue
        curr = board[m-1].pop()
        if stack and stack[-1] == curr: 
            stack.pop(); 
            answer += 2
        else : stack.append(curr)
    return answer