import curses

def render(scr, txt):
	x = 1
	if len(txt) == 3:
		x = 2
	scr.border(0)
	scr.addstr(0, x, txt)
	scr.refresh()