import board

b = board.Board(7, 6, 4)
b.print()

while b.outcome() == 2:
    if b.moves % 2 == 0:
        print("Red's turn: ", end="")
    else:
        print("Blue's turn: ", end="")
    col = int(input())
    b.play(col - 1)
    b.print()

state = b.outcome()
if state == 0:
    print("Red player won.")
if state == 1:
    print("Blue player won.")
if state == 3:
    print("Draw")
