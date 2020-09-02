from collections import deque
import board

win = 100

def sign(color1, color2):
    if color1 == color2:
        return 1
    return -1

def findTraps(b):
    directions = 6
    dx = [-1, -1, 0, 1, 1, 1]
    dy = [1, 1, 1, 1, 1, 0]
    X = [b.connect - 1, b.width - 1, 0, b.width - b.connect, 0, 0]
    Y = [0, 1, 0, 0, 1, 0]
    dX = [1, 0, 1, -1, 0, 0]
    dY = [0, 1, 0, 0, 1, 1]
    L = [b.width - b.connect + 1, b.height - b.connect, b.width - b.connect + 1, b.width - b.connect + 1, b.height - b.connect, b.height - b.connect + 1]
    length = max(b.width, b.height)
    traps = [[[0, 0, 0, 0] for y in range(b.height)] for x in range(b.width)]
    for d in range(directions):
        x = X[d]
        y = Y[d]
        for k in range(L[d]):
            number = [0, 0, 0]
            last = -1
            deq = deque()
            for i in range(b.connect):
                color = b.board[x + i * dx[d]][y + i * dy[d]]
                number[color] += 1
                if color == board.empty:
                    deq.append(i)
            for c in [board.red, board.blue]:
                if number[1 - c] == 0:
                    if number[c] == b.connect - 1:
                        traps[x + deq[0] * dx[d]][y + deq[0] * dy[d]][2 * c] = 1
                    elif number[c] == b.connect - 2 and last != deq[0]:
                        last = deq[0]
                        for place in deq:
                            traps[x + place * dx[d]][y + place * dy[d]][2 * c + 1] += 1
            for i in range(b.connect, length):
                if not b.validIndex(x + i * dx[d], y + i * dy[d]):
                    break
                color = b.board[x + (i - b.connect) * dx[d]][y + (i - b.connect) * dy[d]]
                number[color] -= 1
                if color == board.empty:
                    deq.popleft()
                color = b.board[x + i * dx[d]][y + i * dy[d]]
                number[color] += 1
                if color == board.empty:
                    deq.append(i)
                for c in [board.red, board.blue]:
                    if number[1 - c] == 0:
                        if number[c] == b.connect - 1:
                            traps[x + deq[0] * dx[d]][y + deq[0] * dy[d]][2 * c] = 1
                        elif number[c] == b.connect - 2 and last != deq[0]:
                            last = deq[0]
                            for place in deq:
                                traps[x + place * dx[d]][y + place * dy[d]][2 * c + 1] += 1
            x += dX[d]
            y += dY[d]
    return traps

def simpleEvaluate(b):
    points = [0.0, 0.0]
    traps = findTraps(b)
    for c in [0, 1]:
        for x in range(b.width):
            for y in range(b.height):
                if traps[x][y][2 * c] == 1:
                    points[c] += 1
                elif traps[x][y][2 * c + 1] >= 1:
                    points[c] += (1 - 0.5 ** traps[x][y][2 * c + 1]) / 2
    return points[0] - points[1]

def evaluate(b):
    value = 0.0
    points = [0.0, 0.0]
    traps = findTraps(b)
    color = b.turns % 2
    groundTraps = [0, 0]
    for x in range(b.width):
        if b.ground[x] < b.height:
            groundTraps[board.red] += traps[x][b.ground[x]][2 * board.red]
            groundTraps[board.blue] += traps[x][b.ground[x]][2 * board.blue]
    if groundTraps[color] >= 1:
        return sign(color, 0) * win
    if groundTraps[1 - color] >= 2:
        return sign(1 - color, 0) * win
    doubleTrapHeight = [b.height, b.height]
    lateGame = 0
    for x in range(b.width):
        winner = [board.empty, board.empty]
        for y in range(b.ground[x] + 1, b.height):
            for c in [0, 1]:
                index = (b.height - y + c - 1) % 2
                factor = 1.5 - 0.5 * (y / b.height)
                if traps[x][y - 1][2 * (1 - c)] == 1:
                    factor *= 0.3
                elif traps[x][y - 1][2 * c] == 1:
                    factor *= 2.0
                if winner[index] == board.empty:
                    factor *= 2.0
                value += sign(c, 0) * factor * max(traps[x][y][2 * c], (1 - 0.5 ** traps[x][y][2 * c + 1]) / 2)
                if traps[x][y][2 * c] == 1:
                    if traps[x][y - 1][2 * c] == 1 and winner[0] != 1 - c and winner[1] != 1 - c:
                        doubleTrapHeight[c] = min(doubleTrapHeight[c], y - b.ground[x] - 1)
                    if winner[index] == board.empty:
                        winner[index] = c
            if traps[x][y][0] == 1 and traps[x][y][2] == 1:
                break
        if winner[0] == board.red and winner[1] != board.blue:
            lateGame += 1
        elif winner[1] == board.blue and winner[0] != board.red:
            lateGame -= 1
        value += (2 + 2 * b.turns / (b.width * b.height)) * lateGame
    if doubleTrapHeight[0] < b.height or doubleTrapHeight[1] < b.height:
        if doubleTrapHeight[color] <= doubleTrapHeight[1 - color]:
            return sign(color, 0) * (win - doubleTrapHeight[color])
        return sign(1 - color, 0) * (win - doubleTrapHeight[1 - color])
    return value

def minimax(b, color, depth, alpha=-win, beta=win):
    outcome = b.outcome()
    if outcome <= 1:
        return sign(color, outcome) * win
    elif outcome == board.draw:
        return 0
    if depth == 0:
        return sign(color, 0) * evaluate(b)
    value = -win
    for move in b.moves:
        if b.ground[move] >= b.height:
            continue
        b.play(move)
        value = max(value, -minimax(b, 1 - color, depth - 1, -beta, -alpha))
        b.undo()
        alpha = max(alpha, value)
        if alpha >= beta:
            break
    return value

def takeTurn(board, color, depth):
    value = -2 * win
    move = 0
    for col in board.moves:
        if board.ground[col] >= board.height:
            continue
        board.play(col)
        val = -minimax(board, 1 - color, depth - 1)
        board.undo()
        if val > value:
            value = val
            move = col
    return move
