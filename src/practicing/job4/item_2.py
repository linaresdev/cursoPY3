def productoList(data=""):

	for row in data:
		row *= row
	return row


print(productoList([1,2]))
