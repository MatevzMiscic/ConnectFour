import board
import bot

b = board.Board(7, 6, 4)
bots = [True, False]
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

start = []
for i in start:
    b.play(i)

while b.outcome() == 2:
    b.print()
    column = 0
    color = b.turns % 2
    print(colors[color] + "'s turn: ", end="")
    if bots[color]:
        column = bot.takeTurn(b, color, 5)
        print(column + 1)
    else:
        command = input()
        if command == "undo":
            for i in range(2):
                if b.turns > 0:
                    b.undo()
            continue
        if not command.isdigit():
            print("Invalid move.")
            continue
        column = int(command) - 1
        if column < 0 or column >= b.width or b.ground[column] >= b.height:
            print("Invalid move.")
            continue
    b.play(column)
    print("Game value:", round(bot.simpleEvaluate(b), 2), round(bot.evaluate(b), 2))

b.print()
state = b.outcome()
if state == 0:
    print("Red player won.")
if state == 1:
    print("Blue player won.")
if state == 3:
    print("Draw")
#print(b.history)