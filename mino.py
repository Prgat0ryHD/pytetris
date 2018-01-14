class Mino(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	@property
	def coor(self):
		return self.x, self.y