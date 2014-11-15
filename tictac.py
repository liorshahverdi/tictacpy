## My attempt at tic-tac-toe with python. (I don't know any Python)
print "Let's play Tic Tac Toe!"

class Grid:
	def __init__(self, tdList=0):
		self.tdList = [[0,0,0], [0,0,0], [0,0,0]]

	def dispList(self):
		print self.tdList

g1 = Grid()
g1.dispList()