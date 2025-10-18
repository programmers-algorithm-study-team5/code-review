def solution(keyinput, board):
    move = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
    x, y = 0, 0
    max_x, max_y = board[0] // 2, board[1] // 2
    for k in keyinput:
        dx, dy = move[k]
        x = max(-max_x, min(max_x, x + dx))
        y = max(-max_y, min(max_y, y + dy))
    return [x, y]