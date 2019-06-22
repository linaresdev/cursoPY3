## EJECRCICIO
## Hacer una función que reciba un año como argumento y retorne
## verdadero si es bisiesto

from os import system

def is_lead_year(year):
	return ( (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 )

while True:
	print("EJERCICIO # 3")
	print("Consultor de año bisiesto")
	print("-------------------------")

	out = 0

	year =  int(input("Ingrese el año a consultar? : "))

	print()
	print( "El año ", year, "es bisiesto : ", is_lead_year(year) )
	print()

	while True:	

		opt = input("Quiere evaluar otro año Si / No : ")

		if opt == "Si":
			system("clear")
			break
		elif opt == "No":
			out = 1
			break

	if out > 0:
		system("clear")
		break;