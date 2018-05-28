
#fuction to get absolute vaue of nombre

def absolute(number):
	return sqrt(pow(number, 2))

#returns highest number of list of 
def maximum(numberlist):
	numberlist.sort()
	#return numberlist[-1]
	numberlist.pop(-1)