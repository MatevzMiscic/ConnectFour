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