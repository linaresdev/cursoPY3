
def is_in_lists(lists1=[], lists2=[]):

	for row in lists1:
		if (row in lists2):
			return True

	return False

print( is_in_lists(["A","b", "C"], ["X", "b", "Z"]) )