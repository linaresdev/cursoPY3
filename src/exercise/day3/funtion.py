## FUNCIONES

## Funcion saludar sin parametro
def saludar():
	print("Hola Mundo")

## Funcion saludar con parametro
def hello(nombre):
	print("Hola ", nombre)

## Crear una funcion que le permita ingresar un numero y que retorne su tabla
def verTabla(numero):
	for row in range(1,10):
		print(row, "X", numero, "=", (row*numero) )

def duplicar(n):
	resul = n*2
	return resul

def operation(x, y, opt):
	if opt == 1:
		return x+y
	elif opt == 2:
		return x-y
	elif opt == 3:
		return x*y
	elif opt == 4:
		return x/y

while True:

	print("1 - Sumar")
	print("2 - Restar")
	print("3 - Multiplicar")		
	print("4 - Dividir")

	out = ""
	opt = int(input("Ingrese el numero de la opcion requerida : "))
	print()

	
		
		
print("Resultado: ", menu(4, 2) )