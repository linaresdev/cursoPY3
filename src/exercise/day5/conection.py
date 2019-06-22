import sqlite3

db = sqlite3.connect('prueba.db')

cursor 	= db.cursor()
## query 	=  'CREATE TABLE CURSO (CODIGO INTEGER, NOMBRE varchar(50))'

## query = "insert into CURSO values (1,'Python');"

#query = "select * from CURSO"

cursos = [
	(2, "SQL"),
	(3, "MYSQL"),
	(4, "HTML")
]

query = 'insert insto CURSO value (?,?)'

cursor.executemany(query, cursos)

cursor.execute(query)

#curso = cursor.fetchone()

print(curso)

db.commit()

db.close()