def sumaList(data=""):

	S = 0

	for row in data:
		S += row

	return S


print(sumaList([1,2]))