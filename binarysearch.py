print 'Think of a number from 1 to 100.'

reply = 0
while reply != 3:
	low = 1
	high = 100
	res = int((low + high)/2)
	print 'My guess is ', res
	reply = int(raw_input("Higher? Press 1 Lower? Press 2 Correct? Holy shit! press 3: "))
	while reply <= 0 or reply >=4:
		reply = int(raw_input("Not valid try again: "))
