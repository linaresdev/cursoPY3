## EJERCICIO #4
## Crear una función que evalúe dos números y retorne 
## verdadero si ambos números son iguales.

from os import system


def compara_neumber(num1=0, num2=0):
	return (num1 == num2)

while True:
	system("clear")
	print("EJERCICIO # 4")
	print("Compare dos numero para saber si son iguales o no")
	print("-------------------------------------------------")

	N1 = int(input("Ingrese el primer número : "))
	N2 = int(input("Ingrese el segundo número : "))

	print()
	print("Evaluando ...")
	print("Lo numeros ", N1, " y ", N2, " son iguales? :", compara_neumber(N1, N2))
	print()

	out = 0

	while True:	

		opt = input("Quiere realizar otra operación?  Si / No : ")
		
		if opt == "Si":
			system("clear")
			break
		elif opt == "No":
			out = 1			
			break

	if out > 0:
		system("clear")
		break;