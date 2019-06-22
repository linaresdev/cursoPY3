#!/usr/bin/python3
#-*- coding: utf-8 -*-

from os import system
from core import Database
from core import Functions as fn

class Controller():	

	db = None

	def __init__(self, method):

		self.db = Database.Db()

		if method == "newContact":
			self.newContact()
		elif method == "listContact":
			self.listContact()
		elif method == "searchContact":
			self.searchContact()

	def newContact(self):

		while True:

			out = 0

			system("clear")

			header = "CREAR CONTACTO\n"
			header += "----------------------------\n"

			print(header)

			## GET NAME
			firstname = input("Ingrese su primer nombre : ")
			lastname = input("Ingrese sus apellidos : ")

			## email
			email = input("Ingrese su correo electronico : ")

			## CELL OR PHONE
			phone = input("Ingrese un numero de contacto : ")

			self.db.insert( (firstname,lastname, email, phone) )

			while True:
				opt 	= input("Quiere registrar otro contacto? N/S : ")

				if(opt == "S"): 
					break
				elif(opt == "N"):
					out = 1
					break

			if(out > 0): break
			

	def listContact(self):

		while True:
			out = 0

			system("clear")

			data = self.db.all()
			
			header = "LISTA DE CONTACTO REGISTRADOS\n\n"

			print(header)
			print("# de registros : ", self.db.countRow(), "\n")
			

			print(fn.str_repeat("-", 95))
			print(" ID ",fn.str_cover("NOMBRE COMPLETO", 30),fn.str_cover("CORREO ELECTRONICO", 30),"CREATE_DATE")
			print(fn.str_repeat("-", 95))

			for row in  data:

				ID 			= row[0]
				fullname 	= row[2].upper()+" "+row[1].upper()
				fullname 	= fn.str_cover(fullname, 30, 10)
				email 		= row[3]
				email		= fn.str_cover(email, 30)
				created_at 	= row[5]

				print("",ID,"", fullname, email, created_at)

				
			print("\n")

			opt = input("Para salir pulse la tecla de ENTER")
			
			break

	def searchContact(self):

		while True:
			out = 0

			system("clear")

			header = "\n"
			header += "BUSCAR CONTACTO\n"
			header += fn.str_repeat("-", 30)+"\n\n"

			header += "Filtro de busqueda\n"
			header += "1 - Buscar por Numero\n"
			header += "2 - Buscar por Nombre\n"
			header += "3 - Salir\n"


			print(header)

			opt = int( input("Ingrese el filtro de busqueda : ") )

			if(opt == 3):

				out = 1
				break

			elif(opt == 1):

				ID 		= input("Ingrese el ID del contacto : ")
				data 	= self.db.searchID(int(ID))
				print()

				if(len(data) > 0):
					while True:
						system("clear")

						head = "\n"
						head += "RESUTADO DE LA BUSQUEDA\n\n"
						head += "ACCIONES :: "
						head += "1 - Actualizar | "
						head += "2 - Eliminar | "
						head += "3 - Salir\n"

						print(head)

						print(fn.str_repeat("-", 95))
						print(" ID ",fn.str_cover("NOMBRE COMPLETO", 30),fn.str_cover("CORREO ELECTRONICO", 30),"CREATE_DATE")
						print(fn.str_repeat("-", 95))

						for row in data:
							ID 			= row[0]
							fullname 	= row[2].upper()+" "+row[1].upper()
							fullname 	= fn.str_cover(fullname, 30, 10)
							email 		= row[3]
							email		= fn.str_cover(email, 30)
							created_at 	= row[5]

							print("",ID,"", fullname, email, created_at)

						print('\n')						

						opt = int(input("Ingrese una la accion : "))

						if(opt == 3 ):
							out = 1
							break
						if(opt == 2):
							self.db.delete(ID)
							input("Presione ENTER para Salir")
							break
						if(opt == 1):

							''' BUSCAR POR ID '''

							for row in data:
								__fname 	= row[1]
								__lname 	= row[2]
								__email 	= row[3]

							fname = input("Nombre : ")
							if(fname == ""): fname = __fname

							lname = input("Apellidos : ")
							if(lname == ""): lname = __lname

							email = input("Correo Electronico : ")
							if(email == ""): email = __email

							data = (fname,lname,email,ID)

							self.db.update(data)

							break

				if(out > 0 ): break

			elif(opt == 2):
				''' BUSCAR POR NOMBRE '''

				print()
				srname = input("Ingrse el nombre del contacto que decea buscar : ")
				print()

				resuls = self.db.searchFromName(srname)

				if(len(resuls) > 0):

					print(fn.str_repeat("-", 95))
					print(" ID ",fn.str_cover("NOMBRE COMPLETO", 30),fn.str_cover("CORREO ELECTRONICO", 30),"CREATE_DATE")
					print(fn.str_repeat("-", 95))

					for row in resuls:
						ID 			= row[0]
						fullname 	= row[2].upper()+" "+row[1].upper()
						fullname 	= fn.str_cover(fullname, 30, 10)
						email 		= row[3]
						email		= fn.str_cover(email, 30)
						created_at 	= row[5]

						print("",ID,"", fullname, email, created_at)

					print()

				input("Presione ENTRE para salir")

			if(out > 0 ): break



		