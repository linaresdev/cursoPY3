
## (3) Hacer un programa que genere las tablas de multiplicar de los números
##     múltiplos de 5 que hay entre 1 y 1000

for row in range(1,1000):

	if (row % 5) == 0:

		print("")
		print("La tabla del ", row)

		for x in range(1,9):
			print(row, "X", x, "= ", row*x)

