import board
import bot
import game

players = ["X", "O"]
user = game.Game()

def printTraps(b):
    traps = bot.findTraps(user.grid)
    for c in [0, 1]:
        print(players[c] + " traps:")
        for x in range(user.grid.width):
            for y in range(user.grid.height):
                if traps[x][y][2 * c] >= 1:
                    print(" trap: ", x + 1, y + 1)
                if traps[x][y][2 * c + 1] >= 1:
                    print(" semi trap: ", x + 1, y + 1, " count: ", traps[x][y][2 * c + 1])

def jumpStart(start):
    for i in start:
        user.grid.play(i)


def querry(message, options):
    while True:
        print()
        print(message)
        for option in options:
            print(" * ", option)
        command = input()
        if command in options:
            return command
        print("To ni nobena od opcij.")

def main():
    print("ŠTIRI V VRSTO")
    command = ""
    while command != "izhod":
        print()
        command = querry("Kaj želiš storiti:", ["igraj", "nastavitve", "izhod"])
        if command == "igraj":
            play()
        elif command == "nastavitve":
            settings()
        

def settings():
    print()
    width = int(querry("Izberi željeno širino polja:", ["6", "7", "8"]))
    height = int(querry("Izberi željeno višino polja:", ["5", "6", "7"]))
    connect = int(querry("Izberi število zaporednih žetonov za zmago:", ["3", "4", "5"]))
    first = (querry("Kdo upravlja prvega igralca:", ["človek", "računalnik"]) == "računalnik")
    second = (querry("Kdo upravlja drugega igralca:", ["človek", "računalnik"]) == "računalnik")
    user.setBoard(width, height, connect)
    user.setFirst(first)
    user.setSecond(second)
    input("Uspešno nastavljeno. Pritisni enter za glavni meni...")

def play():
    user.reset()
    while user.grid.outcome() == 2:
        user.grid.print()
        column = 0
        color = user.grid.turns % 2
        print("Na potezi je", players[color] + ": ", end="")
        if user.bots[color]:
            column = bot.takeTurn(user.grid, color, 5)
            print(column + 1)
        else:
            command = input()
            if command == "undo":
                if user.grid.turns > 0:
                    user.grid.undo()
                    if user.bots[1 - color] and user.grid.turns > 0:
                        user.grid.undo()
                else:
                    print("Polje je prazno")
                continue
            if command == "ponastavi":
                user.reset()
            if command == "nazaj":
                return
            if not command.isdigit():
                print("Nepravilen ukaz")
                continue
            column = int(command) - 1
            if not user.grid.validColumn(column):
                print("Nepravilna poteza.")
                continue
        user.grid.play(column)
    user.grid.print()
    state = user.grid.outcome()
    if state in [0, 1]:
        print("Zmagal je", players[state])
    if state == 3:
        print("Izenačeno")
    input("Pritisni enter za glavni meni...")
    #print(b.history)

main()