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

##------------------------------------------------------------------------------------------------------------------
## (2) Realizar un programa que presente un menú con las siguientes opciones
#### 1- Convertir grados a celcius a Fahrenheit
#### 2- Convertir dólar a pesos
#### 3- Convertir metros a pies
#### 4- Salir

## Limpiamos la pantalla
from os import system
system("clear")

## Header
print("EJERCICIO # 2")
print("Proma de conversiones")
print(" ")

while True :
	## MENU DE OPCIONES
	print("MENU")
	print("---------------------------------------------")
	print("1- Convertir de grados Celcius a Fahrenheit")
	print("2- Convertir de dólar a pesos Dominicanos")
	print("3- Convertir de metros a pies")
	print("4- Salir")
	print(" ")

	option = int(input("Ingrese una de la opciones del 1-4 : ") )

	if option == 4:
		## Limpiamos la consola
		from os import system
		system("clear")
		## ROmpemos el flujo
		break

	if option == 1 :
		print(" ")
		print("OPT 1 : CONVERSIÓN DE GRADOS CELCIUS A GRADOS FAHRENHEIT")
		print("--------------------------------------------------------")

		while True :
			out=0

			celsius = int(input(" - Introduzca el valor en Celsius a convertir : "))

			if out > 0:
				from os import system
				system("clear")

				break
			
			print(" ")
			print(" - Valor ingresado en Celsius : ", celsius, " grados")
			print( " - Resultado en Fahrenheit   :", ((celsius*1.8)+32 ), "grados")
			print(" ")

			while True:

				opt=input("Desea realizar otra conversión Si/No : ")

				if opt == "Si":
					## Limpiamos consola
					from os import system
					system("clear")
					## Destruimos el flujo
					break

				if opt == "No":
					## Limpiamos consola
					from os import system
					system("clear")
					## DETEMOS EL CICLO
					out+=1
					## Destruimos el flujo
					break

				print("")
				print(" --- Error:: Opción ", opt," desconocida ---")
				print("")

			if out > 0:
				## Limpiamos consola
				from os import system
				system("clear")
				## Destruimos el flujo
				break

	if option == 2:

		print(" ")
		print("OPT 2 : CONVERSIÓN DE DOLLAR A PESOS DOMINICANOS")
		print("------------------------------------------------")

		current_dollar = 50.54;

		while True:

			out=0
			if out > 0:
				from os import system
				system("clear")
				break
			
			print("- Costo dollar : ", current_dollar, "$RD")
			dollar 		= input("  Si decea actualizar su costo puede hacerlo de lo contrario dejelo en blanco : ")
			inp_dollar 	= float(input("- Ingrese la cantidad que desea consultar : "))

			if dollar == "":
				dollar = current_dollar
			else:
				dollar = float(dollar)

			print(" ")
			print(" -- Costo del dollar en peso dominicanos : ", dollar,"$US")
			print(" -- Uste ha ingresado : ", inp_dollar, "$US")
			print(" -- EL valor en peso dominicanos es : ", (dollar*inp_dollar), "$RD")
			print(" ")

			while True:
				opt = input("Desea realizar otra consulta Si/No : ")

				if opt == "Si":
					break

				if opt == "No":
					out+=1
					break

			if out > 0:
				from os import system
				system("clear")
				break

	if option == 3:
		## Limpiamos pantalla
		from os import system
		system("clear")

		out=0
		if out>0:
			break

		while True:
			
			## Header
			print(" ")
			print("OPT 3 : CONVERSIÓN DE METROS A PIE LINEAL")
			print("-----------------------------------------")

			unidades = float(input("Ingrese las unidades en Metros a convertir : "))

			print("Usted ingresó : ", unidades, "Mts")
			print("Resultado : ", (unidades*3.281), "pies")

			while True:
				opt = input("Desea realizar otra conversión Si/No : ")

				if opt == "Si":
					from os import system
					system("clear")

					break

				if opt == "No":
					from os import system
					system("clear")

					out+=1
					break

				print("Error:: Opción ", opt, " desconocida.")

			if out > 0:
				from os import system
				system("clear")

				break

##------------------------------------------------------------------------------------------------------------------
## (3) Hacer un programa que genere las tablas de multiplicar de los números
##     múltiplos de 5 que hay entre 1 y 1000

## Limpiamos la pantalla
from os import system
system("clear")

## Header
print("EJERCICIO # 3")
print("Tabla de multiplos de 5 entre 1 - 1000")
print(" ")

for row in range(1,1000):

	if (row % 5) == 0:

		print("")
		print("La tabla del ", row)

		for x in range(1,9):
			print(row, "X", x, "= ", row*x)
			
##------------------------------------------------------------------------------------------------------------------
## (4) Realizar un programa que reciba por teclado el sueldo de un empleado y le
## 	   aplique los cálculos de ISR (ver tabla DGII), ARS, y AFP (investigar porcentajes)

while True:
	## Limpiamos la pantalla
	from os import system
	system("clear")

	out = 0	

	while True:

		## Header
		print("EJERCICIO # 2")
		print("-------------------------------")
		print("Devitaciones del ISR, ARS y AFP")
		print(" ")	

		__SFS 		= 3.04/100
		__AFP 		= 2.87/100

		bruto 	= float( input(" Ingrese el sueldo bruto devengar : ") )

		SFS 	= bruto * __SFS
		AFP 	= bruto * __AFP
		SFSAFP 	= SFS + AFP

		neto 	= round( (bruto - SFSAFP) )
		anual 	= neto * 12

		if anual < 416220:
			ISR = 0

		if (anual > 416220) and (anual <= 624329):
			base = anual - 416220
			AISR = base * (15/100)
			ISR  = round(base/12)

		if (anual > 624329) and (anual <= 867123):
			base = anual - 624329
			AISR = base * (20/100)
			ISR  = round( ((base + 31216) / 12) )

		if anual > 867123:
			base = anual - 867123
			AISR = base * (25/100)
			ISR  = round( ((base + 79776) / 12) ) 


		print()
		print("  -- Seguro Familias de Salud [SFS] : ", SFS,"$RD")
		print("  -- Aseguradora de Fondo de Pensiones [AFP] : ", AFP,"$RD")
		print("  -- Impuesto sobre la renta [ISR] : ", ISR,"$RD")
		print()

		while True:
			
			opt = input("Desea realizar otra operación Si/No : ")

			if opt == "Si":
				system("clear")
				break

			if opt == "No":
				out+=1
				break

		if out > 0:
			system("clear")
			break

##------------------------------------------------------------------------------------------------------------------		
## (5) Cree una aplicación de cajero automático para el banco ABC. El cajero tendrá un
##     límite de billetes descrito a continuación: 9 de 1000, 19 de 500, 99 de 100
##
##     El cajero debe solicitar Banco y monto a retirar. Si el banco es ABC el limite de
##     retiro son 10,000 y 2000 pesos por transacción en caso contrario.
##
##     El cajero debe informar si el monto solicitado no puede ser dispensado o si
##     excede el límite de transacción. Y debe hacer la distribución de los billetes de
##     acuerdo al monto.

## Limpiamos la pantalla
from os import system
system("clear")

import time
out=0

while True:

	## Header
	print("EJERCICIO # 5")
	print("Cajero Automatico")
	print(" ")

	print("CAJERO AUTOMÁTICO")
	print("-----------------")

	print("1 - Banco ABC")
	print("2 - Banco PEPIN")	
	print("3 - Salir")

	print()
	banco = int(input("Selecciones su banco : "))

	if banco == 3:
		system("clear")
		break

	if (banco == 1) or (banco == 2) :
		
		## Contenedores de la información del banco seleccionado
		name	= ""
		slogan	= ""

		## Contenedores del limite y transaciones
		limite	= 0
		trans 	= 0		

		if banco == 1:
			name 	= "ABC"
			slogan 	= "Nuestra prioridad es servirle"
			limite 	= 10000
			trans 	= 2000

		if banco == 2:
			name 	= "PEPIN"
			slogan 	= "Banco afiliado a la red bancaria más grande del mundo."					  
			limite 	= 6000
			trans 	= 2000

		__b1000 	= (9*1000)
		__b500 		= (19*500)
		__b100 		= (99*100)			

		while True:

			## Bienvenido (a)
			system("clear")
			print( " BIENVENIDO AL BANCO ", name )
			print( "------------------------------------------------------" )
			print( slogan )
			print()

			print("  -- Usted cuenta con límite de ", limite, " pesos ")
			print("  -- Puede realizar tranzaciones de ", trans, " pesos")
			print()

			b1000 	= 0
			b500 	= 0
			b100 	= 0

			monto = int(input(" Por Favor ingrese un monto a debitar : "))

			if ((monto % 100) == 0) and (monto < limite):

				## PROCEDIMIENTO

				out = 0

				while True:			

					if monto <= trans:
						if monto == 0:

							break
						else:

							if monto >= 1000:

								monto 	-= 1000
								b1000 	+= 1

							if monto >= 500:

								monto 	-= 500
								b500 	+= 1

							if monto >= 100:

								monto 	-= 100
								b100 	+= 1

					else:

						print()
						print("  -- Solo se permiten tranzaciones de ", trans, " pesos")

						break
						

				## END

				print()

				total = 0

				if b1000 != 0:
					print("  -- Billetes de 1000 : ", b1000)
					total += 1000*b1000

				if b500 != 0:
					print("  -- Billetes de 500  : ", b500)
					total += 500*b500

				if b100 != 0:
					print("  -- Billetes de 100  : ", b100)
					total += 100*b100

				if (b1000 != 0) or (b500 != 0) or (b100 != 0) :
					print("  -- Debitacion total : ", total, " $RD")
					print()

				out = 0

				while True:
					opt = input(" Desea realizar otra transacción Si/No : ")

					if opt == "Si":
						system("clear")
						break

					if opt == "No":
						out+=1
						break
				if out > 0:
					system("clear")
					break

			else:
				out=0

				while True:				

					print()

					if debito > limite:
						print("El monto solicitado excede la cantidad permitida.")

					if (debito < limite) and (debito > 100):
						print("Lo sentimos mucho pero no podemos despachar el monto solicitado.")

					if debito < 100:
						print("El billete más pequeño permitido es de 100 pesos")

					print()

					opt = input("Desea realizar otra transacción Si/No : ")

					if opt == "Si":
						system("clear")
						break

					if opt == "No":
						out+=1
						break

				if out > 0:
					system("clear")
					break

	else:
		while True:

			print()
			print("ERROR :: ", "Seleccione un banco válido")
			print()

			print("Regresando a la pantalla de inicio ...")

			time.sleep(5)
			system("clear")
			break

			



