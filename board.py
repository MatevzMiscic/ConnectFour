empty = 2
red = 0
blue = 1

class Board:

    def __init__(self, width, height, connect):
        self.width = width
        self.height = height
        self.connect = min(width, height, connect)
        self.board = [[empty for y in range(height)] for x in range(width)]
        self.ground = [0 for x in range(width)]
        self.history = []
        self.moves = 0

    def play(self, row):
        assert self.moves < self.width * self.height
        assert 0 <= row < self.height
        assert self.ground[row] < self.height
        self.board[row][self.ground[row]] = self.moves % 2
        self.ground[row] += 1
        self.history.append(row)
        self.moves += 1

    def print(self):
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                print(str(self.board[x][y]), end = "")
            print()

b = Board(7, 6, 4)
b.play(3)
b.print()