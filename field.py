import curses
from tetromino import Tetromino

class Field:
    def __init__(self, window, mino):
        self.mino   = mino
        self.window = window
        self.field  = []
        for i in range(20):
            self.field.append([])
            for j in range(10):
                self.field[i].append(False)

    def addTetromino(self, tetromino):
        for m in tetromino.mino:
            self.field[m.y][m.x] = True

    def render(self):
        for i in range(20):
            for j in range(10):
                if self.mino[i][j]:
                    self.window.addstr(i, j, '@')
