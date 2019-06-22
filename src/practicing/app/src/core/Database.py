#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sqlite3

class Db():

	db 			= None
	query 		= None

	def __init__(self):

		self.db 	= sqlite3.connect("sqlite3/agenda.db")
		self.query 	= self.db.cursor()

	def insert(self, data):

		SQL = """
			INSERT INTO contacts(firstname, lastname, email, phone) 
			VALUES (?,?,?,?)
		"""

		if(self.query.execute(SQL, data)): print("Registro guardado con exito!")
		else: print("Ocurrio un error al intentar realizar el registro")

	def update(self, data):

		SQL = """
		UPDATE contacts
		SET firstname=?,lastname=?,email=?
		WHERE id=?
		"""

		if(self.query.execute(SQL, data)): print("Contacto actualizado correctamente!")
		else: print("Error al tratar de actualizar el contacto")

	def delete(self, ID):

		if(self.query.execute("DELETE FROM contacts WHERE id=?", (ID, ))):
			print("El contacto fue eleiminado correctamente")
		else:
			print("Error al tratar de eliminar el contacto")

	def countRow(self):

		self.query.execute("SELECT COUNT(*) FROM contacts")

		row = self.query.fetchone()

		return row[0]

	def all(self):

		self.query.execute("SELECT * FROM contacts")

		return self.query.fetchall()


	def searchID(self, ui):

		self.query.execute("SELECT * FROM contacts WHERE id=?", (ui, ))

		return self.query.fetchall()

	def searchFromName(self, search):

		SQL = """
			SELECT * 
			FROM contacts
			WHERE firstname LIKE ?
		"""

		self.query.execute(SQL, ('%'+search+'%', ))

		return self.query.fetchall()

	def __del__(self):
		
		## Cerramos la Consulta
		self.query.close()
		## Guardamos en la Base de Datos
		self.db.commit()
		## Cerramos la Base de Datos
		self.db.close()
			
