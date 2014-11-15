def my_factorial(number):
	if number == 0 or number == 1:
		return 1
	else:
		return my_factorial(number-1) * number

print 'factorial of 3 is', my_factorial(3)