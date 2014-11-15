## My attempt at tic-tac-toe with python. (I don't know any Python)
print "Let's play Tic Tac Toe!"

class Grid:
	def __init__(self, tdList=0):
		self.tdList = [[0,0,0], [0,0,0], [0,0,0]]

	def setTile(self, locn, player):
		if locn == 1:
			self.tdList[0][0] = player
		elif locn == 2:
			self.tdList[0][1] = player
		elif locn == 3:
			self.tdList[0][2] = player
		elif locn == 4:
			self.tdList[1][0] = player
		elif locn == 5:
			self.tdList[1][1] = player
		elif locn == 6:
			self.tdList[1][2] = player
		elif locn == 7:
			self.tdList[2][0] = player
		elif locn == 8:
			self.tdList[2][1] = player
		elif locn == 9:
			self.tdList[2][2] = player
		elif locn == 0:
			return False

	def dispList(self):
		print self.tdList[0]
		print self.tdList[1]
		print self.tdList[2]

	def isNotAValidTile(self, tile):
		if tile <= 0 or tile >= 10:
			return True
		else:
			return False

	def isAlreadyOccupied(self, locn):
		if locn == 1:
			return self.tdList[0][0] > 0
		elif locn == 2:
			return self.tdList[0][1] > 0
		elif locn == 3:
			return self.tdList[0][2] > 0
		elif locn == 4:
			return self.tdList[1][0] > 0
		elif locn == 5:
			return self.tdList[1][1] > 0
		elif locn == 6:
			return self.tdList[1][2] > 0
		elif locn == 7:
			return self.tdList[2][0] > 0
		elif locn == 8:
			return self.tdList[2][1] > 0
		elif locn == 9:
			return self.tdList[2][2] > 0
		elif locn == 0:
			return False

	def ifPlayerJustWon(self, p):
		if self.tdList[0][0] == p and self.tdList[0][1] == p and self.tdList[0][2] == p:
			return True
		elif self.tdList[1][0] == p and self.tdList[1][1] == p and self.tdList[1][2] == p:
			return True
		elif self.tdList[2][0] == p and self.tdList[2][1] == p and self.tdList[2][2] == p:
			return True
		
		elif self.tdList[0][0] == p and self.tdList[1][0] == p and self.tdList[2][0] == p:
			return True
		elif self.tdList[0][1] == p and self.tdList[1][1] == p and self.tdList[2][1] == p:
			return True
		elif self.tdList[0][2] == p and self.tdList[1][2] == p and self.tdList[2][2] == p:
			return True

		elif self.tdList[0][0] == p and self.tdList[1][1] == p and self.tdList[2][2] == p:
			return True
		elif self.tdList[2][0] == p and self.tdList[1][1] == p and self.tdList[0][2] == p:
			return True
	
		return False

def startGame():
	g = Grid()
	g.dispList()
	lcv = 1
	pnum = 0
	gameOver = False
	pl_1 = "Player1"
	pl_2 = "Player2"
	while not gameOver:
		##determine which player's turn it is
		if lcv%2 == 0:
			player = pl_2
			pnum = 2
		else:
			player = pl_1
			pnum = 1
		print "\n", player,"'s turn"
		string_io = raw_input("select a tile (1-9) ")

		while g.isNotAValidTile(int(string_io)):
			string_io = raw_input("The tile you selected is not valid.\nselect a tile (1-9) ")
		while g.isAlreadyOccupied(int(string_io)):
			string_io = raw_input("The tile you selected has already been occupied.\nselect a tile (1-9) ")

		g.setTile(int(string_io),pnum)
		g.dispList()
		if g.ifPlayerJustWon(pnum):
			if pnum ==1:
				print "Player 1 has won!"
			else:
				print "Player 2 has won!"
			gameOver = True
		lcv += 1
		if lcv == 10:
			gameOver = True 

keepPlay = True

while keepPlay:
	res = raw_input("Ready? (y/n) ")
	if res == 'y':
		startGame()
		continue_play_response = raw_input("Play again? (y/n) ")
		if continue_play_response != 'y':
			keepPlay = False