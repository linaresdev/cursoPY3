## (1) Realizar un programa que solicite al usuario un número indeterminado de
## números (mientras se tecleen números que no sean cero). Al salir el programa
## debe dar en pantalla el total de números dados y la suma de ellos.

print("EJERCICIO # 1")
print("Le solitaremos un numero distinto de cero, si ingresa un cero el proceso se detiene")
print(" ")

acomulador = 0
row=0
counter=0

while True :
	row+=1
	number = int(input("Ingrese un numero : "))

	if number != 0 :
		counter+=1
		acomulador += number

	if number == 0 :
		break

print(" ")
print("Cantidad de numero ingresado :", row)
print("Cantidad de numero ingresado difente de cero :", counter)
print("Sumatoria de los numeros difernetes de cero :", acomulador)
print(" ")
print("FIN DEL PROGRAMA")