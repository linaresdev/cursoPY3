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

			



