import curses
from mino  import Mino
from tetra import Tetra

class Tetromino:
    def __init__(self, window, char):
    	self.mino   = Tetra(char)
    	self.window = window
    	self.char   = char

    def render(self):
    	for m in self.mino:
    		self.window.addstr(m.y, m.x, '@')