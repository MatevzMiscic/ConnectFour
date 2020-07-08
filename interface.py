import board
import bot

b = board.Board(7, 6, 4)
bots = [False, True]
colors = ["Red", "Blue"]

while b.outcome() == 2:
    column = 0
    color = b.moves % 2
    print(colors[color] + "'s turn: ", end="")
    if bots[color]:
        column = bot.takeTurn(b, color, 4)
        print(column + 1)
    else:
        column = int(input()) - 1
        if column < 0 or column >= b.width or b.ground[column] >= b.height:
            print("Invalid move.")
            continue
    b.play(column)
    b.print()

state = b.outcome()
if state == 0:
    print("Red player won.")
if state == 1:
    print("Blue player won.")

if state == 3:
    print("Draw")
