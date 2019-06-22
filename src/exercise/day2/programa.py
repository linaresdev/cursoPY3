# Hacer un progrma que resiva 5 valores por teclado y sume solo los valores que sean multiplos de 5.

V1 = int(input("Ingrese el valor 1 : "))
V2 = int(input("Ingrese el valor 2 : "))
V3 = int(input("Ingrese el valor 3 : "))
V4 = int(input("Ingrese el valor 4 : "))
V5 = int(input("Ingrese el valor 5 : "))

resultado = 0

if (V1 % 5) == 0 :
	resultado +=  V1

if (V2 % 5) == 0 :
	resultado = resultado + V2

if (V3 % 5) == 0 :
	resultado = resultado + V3

if (V4 % 5) == 0 :
	resultado = resultado + V4

if (V5 % 5) == 0 :
	resultado = resultado + V5

print("La suma del los numeros multiplos de 5 es : ", resultado)
