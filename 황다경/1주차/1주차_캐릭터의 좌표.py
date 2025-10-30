def solution(keyinput, board):
    x, y = 0, 0
    
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    for key in keyinput:
        if key == "left":
            x = x - 1
        elif key == "right":
            x = x + 1
        elif key == "up":
            y = y + 1
        elif key == "down":
            y = y - 1
            
        if x < -max_x:
            x = -max_x
        if x > max_x:
            x = max_x
        if y < -max_y:
            y = -max_y
        if y > max_y:
            y = max_y
    
    return [x, y]
