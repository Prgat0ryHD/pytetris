import curses
import var
from curses    import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random    import shuffle
from scrRender import render
from tetromino import Tetromino

if __name__ == '__main__':
    shuffle(var.BAG)
    bag1  = [x for x in var.BAG]
    shuffle(var.BAG)
    bag2  = [x for x in var.BAG]
    level = 1
    score = 0
    curses.initscr()
    curses.start_color()
    curses.use_default_colors()
    nextWindow  = curses.newwin(6, 7, 1, 19)
    bagWindow   = curses.newwin(16, 7, 7, 19)
    mainWindow  = curses.newwin(22, 12, 1, 7)
    holdWindow  = curses.newwin(6, 7, 1, 0)
    lvlWindow   = curses.newwin(6, 7, 7, 0)
    lineWindow  = curses.newwin(5, 7, 13, 0)
    scoreWindow = curses.newwin(5, 7, 18, 0)
    mainWindow.keypad(1) 
    curses.noecho()
    curses.curs_set(0)
    render(nextWindow, "NEXT")
    render(holdWindow, "HOLD")
    render(lvlWindow, "LEVEL")
    render(lineWindow, "LINES")
    render(bagWindow, "BAG")
    render(scoreWindow, "SCORE")
    while True:
        if len(bag2) == 0:
            shuffle(var.BAG)
            bag2  = [x for x in var.BAG]
        tetromino = Tetromino(mainWindow, bag1.pop())
        bag1.insert(0, bag2.pop())
        while True:
            mainWindow.erase()
            mainWindow.border(0)
            tetromino.render()
            event = mainWindow.getch()
            if event in [KEY_LEFT, KEY_RIGHT]:
                tetromino.update(event)
            if event == curses.KEY_F4:
                break
        if mainWindow.getch() == curses.KEY_F4:
            break
    curses.endwin()
