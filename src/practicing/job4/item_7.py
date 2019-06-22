
def rm_reflection(lists=[]):

	newlist = []

	for item in lists:

		if item not in newlist:
			newlist.append(item)

	return newlist
	

print(rm_reflection(["hola", 22, "que tal", "hola", "que tal", 22]))


		
