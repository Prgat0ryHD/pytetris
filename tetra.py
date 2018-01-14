from mino import Mino

def Tetra(char):
	mino = []
	if char == 'I':
		mino.append(Mino(3, 0))
		mino.append(Mino(4, 0))
		mino.append(Mino(5, 0))
		mino.append(Mino(6, 0))
	if char == 'S':
		mino.append(Mino(4, 0))
		mino.append(Mino(5, 0))
		mino.append(Mino(3, 1))
		mino.append(Mino(4, 1))
	if char == 'Z':
		mino.append(Mino(3, 0))
		mino.append(Mino(4, 0))
		mino.append(Mino(4, 1))
		mino.append(Mino(5, 1))
	if char == 'J':
		mino.append(Mino(3, 0))
		mino.append(Mino(3, 1))
		mino.append(Mino(4, 1))
		mino.append(Mino(5, 1))
	if char == 'L':
		mino.append(Mino(5, 0))
		mino.append(Mino(3, 1))
		mino.append(Mino(4, 1))
		mino.append(Mino(5, 1))
	if char == 'T':
		mino.append(Mino(4, 0))
		mino.append(Mino(3, 1))
		mino.append(Mino(4, 1))
		mino.append(Mino(5, 1))
	if char == 'O':
		mino.append(Mino(4, 0))
		mino.append(Mino(5, 0))
		mino.append(Mino(4, 1))
		mino.append(Mino(5, 1))
	return mino