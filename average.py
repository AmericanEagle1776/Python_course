def average(liste):
	if type(liste) is list and liste:
		return sum(liste)/len(liste)

print(average([1, 2, 3, 4, 5, 6, 7, 8]))