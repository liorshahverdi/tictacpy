class mine:
	def __init__(self, name=None):
		self.name = "John Coogamelloncamp"

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name


m = mine()
string = "Steven Tyler"
m.setName(string)
print m.getName()