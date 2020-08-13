import board
import bot

class Game:
    def __init__(self):
        self.width = 7
        self.height = 6
        self.connect = 4
        self.bots = [False, True]
        self.score = [0, 0]
        self.grid = board.Board(self.width, self.height, self.connect)
    
    def legal(self):
        return self.connect <= self.width and self.connect <= self.height

    def setBoard(self, width, height, connect):
        self.width = width
        self.height = height
        self.connect = connect
        self.grid = board.Board(width, height, connect)
        return self.legal()

    def setFirst(self, isBot):
        self.bots[0] = isBot
    
    def setSecond(self, isBot):
        self.bots[1] = isBot
    
    def firstWins(self):
        self.score[0] += 1

    def secondWins(self):
        self.score[1] += 1

    def resetScore(self):
        self.score[0] = 0
        self.score[1] = 0

    def reset(self):
        self.grid = board.Board(self.width, self.height, self.connect)