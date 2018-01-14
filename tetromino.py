import curses
import var
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from mino   import Mino
from tetra  import Tetra

class Tetromino:
    def __init__(self, window, char):
        self.mino     = Tetra(char)
        self.window   = window
        self.char     = char
        self.rotation = 0
        self.direction_map = {
            KEY_UP:    self.hard_drop,
            KEY_DOWN:  self.soft_drop,
            KEY_LEFT:  self.move_left,
            KEY_RIGHT: self.move_right
            }

    def render(self):
        for m in self.mino:
            self.window.addstr(m.y, m.x, '@')

    def update(self, event):
        self.direction_map[event]()

    def move_left(self):
        for m in self.mino:
            if m.x - 1 < 1:
                return
        for m in self.mino:
            m.x -= 1

    def move_right(self):
        for m in self.mino:
            if m.x + 1 > 10:
                return
        for m in self.mino:
            m.x += 1

    def rotate_cw(self):
        pass

    def rotate_ccw(self):
        pass

    def hard_drop(self):
        pass

    def soft_drop(self):
        pass

    def collide(self, field):
        pass
