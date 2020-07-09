from collections import deque
import board

win = 100

def minimax(board, color, depth, alpha=-win, beta=win):
    outcome = board.outcome()
    if depth == 0 or outcome <= 1:
        if outcome == color:
            return win
        elif outcome == 1 - color:
            return -win
        return 0
    value = -win
    for move in board.moves:
        if board.ground[move] >= board.height:
            continue
        board.play(move)
        value = max(value, -minimax(board, 1 - color, depth - 1, -beta, -alpha))
        board.undo()
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