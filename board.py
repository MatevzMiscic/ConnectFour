empty = 2
red = 0
blue = 1

inProgress = 2
draw = 3

class Board:

    def __init__(self, width, height, connect):
        self.width = width
        self.height = height
        self.connect = min(width, height, max(connect, 3))
        self.board = [[empty for y in range(height)] for x in range(width)]
        self.ground = [0 for x in range(width)]
        self.history = []
        self.turns = 0
        self.moves = []
        move = width // 2
        for i in range(width):
            move += ((-1) ** i) * i
            self.moves.append(move)

    def play(self, column):
        assert self.turns < self.width * self.height
        assert 0 <= column < self.width
        assert self.ground[column] < self.height
        color = self.turns % 2
        self.board[column][self.ground[column]] = color
        self.ground[column] += 1
        self.history.append(column)
        self.turns += 1

    def undo(self):
        assert self.turns > 0
        column = self.history.pop()
        self.turns -= 1
        self.ground[column] -= 1
        self.board[column][self.ground[column]] = empty

    def validIndex(self, x, y):
        return 0 <= x and x < self.width and 0 <= y and y < self.height

    def validColumn(self, col):
        return 0 <= col and col < self.width and self.ground[col] < self.height

    def outcome(self):
        dx = [1, 1, 0, -1]
        dy = [0, -1, -1, -1]
        directions = 4
        for X in range(self.width):
            for Y in range(self.height):
                color = self.board[X][Y]
                if color == 2:
                    continue
                for d in range(directions):
                    number = 1
                    x = X
                    y = Y
                    for i in range(self.connect - 1):
                        x += dx[d]
                        y += dy[d]
                        if self.validIndex(x, y) and self.board[x][y] == color:
                            number += 1
                        else:
                            break
                    if number == self.connect:
                        return color
        if self.turns == self.width * self.height:
            return draw
        return inProgress

    def print(self):
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                color = self.board[x][y]
                char = ''
                if color == empty:
                    char = ' '
                elif color == red:
                    char = 'X'
                elif color == blue:
                    char = 'O'
                print(' ' + char, end = "")
            print()