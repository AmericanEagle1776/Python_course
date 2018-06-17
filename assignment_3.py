import math
#fuction to get absolute vaue of nombre
print('prints absolute value of number')
print('number is ', str('3'))
print('solutions:')
def absolute(number):
	if number < 0:
		return -number
	else:
		return number

def absolute2(number):
	"""absolute value by square then squareroot"""
	return math.sqrt(pow(number, 2))

def absolute3(number):
	return abs(number)

print(absolute(-3))
print(absolute2(-3))
print(absolute3(-3))

#returns highest number of list of 
print('prints max of list')
print('list is', str('[1, 2, 3, 4, 300]'))
print('solutions:')
def maximum(numberlist):
	numberlist.sort()
	return numberlist[-1]
	#numberlist.pop(-1)

def maximum2(numberlist):
	"""get max of list with for loop"""
	max = numberlist[0]
	for x in numberlist:
		if x > max:
			max = x
	return max

def maximum3(numberlist):
	return max(numberlist)

print(maximum([1, 2, 3, 4, 300]))
print(maximum2([1, 2, 3, 4, 300]))
print(maximum3([1, 2, 3, 4, 300]))
#print(maximum2([1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 2]))