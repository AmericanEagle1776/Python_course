import math
#fuction to get absolute vaue of nombre

def absolute(number):
	#return math.sqrt(pow(number, 2))
	if number < 0:
		return -number
	else:
		return number

#print(absolute(-3))
#returns highest number of list of 
def maximum(numberlist):
	numberlist.sort()
	return numberlist[-1]
	#numberlist.pop(-1)

#print(maximum([1, 2, 3, 4, 300]))