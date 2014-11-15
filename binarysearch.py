print 'Think of a number from 0 to 100.'

reply = 0
low = 0
high = 101
while reply != 3:
	res = int((low + high)/2)
	print 'My guess is ', res
	print 'Higher? Press 1 Lower? Press 2 Correct? Holy shit! press 3: '
	reply = int(raw_input())
	while reply <= 0 or reply >=4:
		reply = int(raw_input("Not valid try again: "))

	if reply == 1:
		low = res
		print 'HIGHER'
	elif reply == 2:
		high = res
		print 'LOWER'
	elif reply == 3:
		print 'COOORECT!'