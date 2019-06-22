## EJERCICIO # 1
## Hacer una función que potencie un número x a la y
print("EJERCICIO # 1")
print("Potencia de X a la Y")
print("-------------------------")

def potenciador(init, end):
	for X in range(init,end):
		print("-------------------------")
		for Y in range(1,10):
			print("Potencia de ", X, "^", Y, " = ", X ** Y)
	
potenciador(1, 6)

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

## EJERCICIO #4
## Crear una función que evalúe dos números y retorne 
## verdadero si ambos números son iguales.

def compara_neumber(num1=0, num2=0):
	return (num1 == num2)

while True:
	print("COMPARADOR")
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

## EJERCICIO # 5
## Un número palindrómico se lee igual en ambos sentidos. 
## El palíndromo más grande hecho del producto de dos números 
## de 2 dígitos es 9009 = 91 × 99. Cree una función que encuentre 
## el palíndromo más grande hecho del producto de dos números de 
## 3 dígitos.
from os import system

def is_palidromo(N):
	if str(N) == str(N)[:: -1]:
		return True
	else:
		return False

def iteratodor_palidromico():
	
	data = 0

	for N1 in range(100,999):
		for N2 in range(100,999): 
			M = N1*N2
			if is_palidromo( M ):
				P1 = N1
				P2 = N2
				data =  M

	return "{}{}{}{}{}".format(P1, " X ", P2," = ", M)

print("EJERCICIO # 5")
print("Calculador del palindrómo mas grande de 3 digitos")
print("-------------------------------------------------")
print("El palindrómo mas grande de 3 digito es :", iteratodor_palidromico());
	