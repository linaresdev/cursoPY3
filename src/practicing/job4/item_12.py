
def rm_from_key(keys=[], lists=[]):
	
	V = []
	for key in keys:
		V.append(lists[key])

	if len(V) > 0:
		for x in V:

			lists.pop(lists.index(x))
		
	return lists
	

print( rm_from_key([0, 4, 5], ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']) )