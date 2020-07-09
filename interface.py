import board
import bot

b = board.Board(7, 6, 4)
bots = [False, True]
colors = ["Red", "Blue"]

def printTraps(b):
    traps = bot.findTraps(b)
    for c in [0, 1]:
        print(colors[c] + " traps:")
        for x in range(b.width):
            for y in range(b.height):
                if traps[x][y][2 * c] >= 1:
                    print(" trap: ", x + 1, y + 1)
                if traps[x][y][2 * c + 1] >= 1:
                    print(" semi trap: ", x + 1, y + 1, " count: ", traps[x][y][2 * c + 1])

#start = [4, 4, 4, 4, 4, 4, 5, 3, 6, 7, 5, 3, 5, 5, 5, 5, 3, 3, 3, 3, 7, 2, 7, 1, 7, 7, 7, 1, 2, 2, 2, 6, 2]
start = []
for i in start:
    b.play(i - 1)
if start != []:
    b.print()

while b.outcome() == 2:
    column = 0
    color = b.turns % 2
    print(colors[color] + "'s turn: ", end="")
    if bots[color]:
        column = bot.takeTurn(b, color, 6)
        print(column + 1)
    else:
        column = int(input()) - 1
        if column < 0 or column >= b.width or b.ground[column] >= b.height:
            print("Invalid move.")
            continue
    b.play(column)
    printTraps(b)
    b.print()

state = b.outcome()
if state == 0:
    print("Red player won.")
if state == 1:
    print("Blue player won.")
if state == 3:
    print("Draw")