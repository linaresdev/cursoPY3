
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

