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
    for col in range(board.width):
        if board.ground[col] >= board.height:
            continue
        board.play(col)
        value = max(value, -minimax(board, 1 - color, depth - 1, -beta, -alpha))
        board.undo()
        alpha = max(alpha, value)
        if alpha >= beta:
            break
    return value

def takeTurn(board, color, depth):
    value = -200
    move = 0
    for col in range(board.width):
        if board.ground[col] >= board.height:
            continue
        board.play(col)
        val = -minimax(board, 1 - color, depth - 1)
        board.undo()
        if val > value or val == value and abs(2 * col - board.width) < abs(2 * move - board.width):
            value = val
            move = col
    return move