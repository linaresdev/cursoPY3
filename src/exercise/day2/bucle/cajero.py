# Limpiamos la pantalla
from os import system
system("clear")

while True:

	monto = int(input("Ingrese el monto :"))

	if(monto == 0)
		print("Debe escribir un momto")
	else:
		if monto%100 == 0:
