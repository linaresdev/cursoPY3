import sqlite3

db 		= sqlite3.connect("agenda.db")
query 	= db.cursor()

sql = """ 
CREATE TABLE IF NOT EXISTS contacts(
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	firstname VARCHAR(30),
	lastname VARCHAR(40),
	email VARCHAR(60) UNIQUE NOT NULL,
	phone INTEGER UNIQUE NOT NULL,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
"""

## EJECUTAMOS LA CONSULTA
if(query.execute(sql)): print("Tabla creada con exito!")
else: print("Ha ocurrido un error al crear la tabla")

## Terminamos la consulta
query.close()

## Guardamos los cambios en la base de datos
db.commit()

## Cerramos la Base de Datos
db.close()