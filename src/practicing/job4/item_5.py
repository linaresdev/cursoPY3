
def is_palidromo(N):
	if str(N) == str(N)[:: -1]:
		return True
	else:
		return False

def count_lists_str(lists=[]):

	X = 0

	if len(lists) >= 2:

		for row in lists:
			if is_palidromo(row):
				X += 1

	return X


print(count_lists_str(['abc', 'xyz', 'aba', '1221']))