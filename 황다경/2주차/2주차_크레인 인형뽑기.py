from collections import deque

def solution(board, moves):
    n = len(board)
    columns = [deque() for _ in range(n)]
    
    for j in range(n):
        for i in range(n):
            if board[i][j] != 0:
                columns[j].append(board[i][j])
    
    basket = []
    count = 0
    
    for move in moves:
        col_idx = move - 1
        if columns[col_idx]:
            doll = columns[col_idx].popleft()
            if basket and basket[-1] == doll:
                basket.pop()
                count += 2
            else:
                basket.append(doll)
    
    return count
