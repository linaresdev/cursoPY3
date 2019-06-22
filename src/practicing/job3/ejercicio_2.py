## EJERCICIO #2
## Realizar una función que pida por pantalla un número del 1 al 10 y muestre por pantalla el número escrito en letras.
from os import system

def number_to_str(number=0):
	
	data = ["CERO","UNO","DOS","TRES","CUATRO","CINCO","SEIS","SIETE","OCHO","NUEVE","DIEZ"]
	
	return data[number]

while True:
	print("EJERCICIO # 2")
	print("Convertir nuemero a textos")
	print("--------------------------")

	N = int(input("Digite un número del 1 - 10 :"))

	print()
	print("Convirtiendo ...")
	print("Usted digito el número : ", number_to_str(N))
	print()

	out=0

	while True:	

		opt = input("Quiere convertir otro numero? Si / No : ")

		if opt == "Si":
			system("clear")
			break
		elif opt == "No":
			out = 1
			break

	if out > 0:
		system("clear")
		break;