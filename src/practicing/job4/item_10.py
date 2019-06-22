

def max_count_item(N=0, lists=[]):

	out = []

	for row in lists:		
		if len(row) > N:
			out.append(row)

	return out
	

print(max_count_item(4, ["hola", "que tal", "hola mundo"]))