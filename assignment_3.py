import math
#fuction to get absolute vaue of nombre

def absolute(number):
	if number < 0:
		return -number
	else:
		return number

def absolute2(number):
	return math.sqrt(pow(number, 2))

def absolute3(number):
	abs(number)

#print(absolute(-3))
#returns highest number of list of 
def maximum(numberlist):
	numberlist.sort()
	return numberlist[-1]
	#numberlist.pop(-1)

def maximum2(numberlist):
	"""get max of lis"""
	max = numberlist[0]
	for x in numberlist:
		if x > max:
			max = x
	return max

def maximum3(numberlist):
	return max(numberlist)

#print(maximum([1, 2, 3, 4, 300]))
#print(maximum2([1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 2]))