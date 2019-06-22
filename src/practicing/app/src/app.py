#!/usr/bin/python3
#-*- coding: utf-8 -*-

## HELPERS


## LIBRARIES
from os import system
from core import Functions as fn
from core import Controller
from core import Database

## ROUTES
routes = {
	1: "newContact", 
	2: "listContact", 
	3: "searchContact"
}

while True:

	try:
		system("clear")

		## HEARDER
		header = "\n"
		header += "MENU DE CONTACTOS\n"
		header += fn.str_repeat('-', 20)+"\n"
		header += "1 - Nuevo\n"
		header += "2 - Listar\n"
		header += "3 - Buscar\n"
		header += "4 - Salir\n"
		
		print(header)

		OPT = int(input("Ingres una accion : "))

		if OPT == 4: # Close APP
			system("clear")
			break
		elif OPT in routes:
			Controller.Controller(routes[OPT])

	except Exception as e:

		system("clear")

		close = fn.str_repeat('-', 20)+"\n"
		close += " Exception Error \n"
		close += fn.str_repeat('-', 20)+"\n"

		print(close)

		print(e)

		break

