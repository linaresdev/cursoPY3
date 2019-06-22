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

		
