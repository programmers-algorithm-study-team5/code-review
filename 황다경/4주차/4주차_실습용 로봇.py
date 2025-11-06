def solution(command):
    x, y = 0, 0
    direction = 0
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    for cmd in command:
        if cmd == 'R':
            direction = (direction + 1) % 4
        elif cmd == 'L':
            direction = (direction - 1) % 4
        elif cmd == 'G':
            x += dx[direction]
            y += dy[direction]
        else:
            x -= dx[direction]
            y -= dy[direction]
            
    return [x, y]