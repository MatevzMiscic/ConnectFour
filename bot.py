import board

def minimax(board, color, depth):
    outcome = board.outcome()
    if depth == 0 or outcome <= 1:
        if outcome == color:
            return 100
        elif outcome == 1 - color:
            return -100
        return 0
    value = -100
    for col in range(board.width):
        if board.ground[col] >= board.height:
            continue
        board.play(col)
        value = max(value, -minimax(board, 1 - color, depth - 1))
        board.undo()
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