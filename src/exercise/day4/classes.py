
class Persona:
	def __init__( self, codigo, nombre, apellidos, telefono ):
		self.codigo 	= codigo
		self.nombre 	= nombre
		self.apellidos 	= apellidos
		self.telefono 	= telefono

	def Saludar(self):
		print("Hola Mundo")


class Cliente(Persona):
	pass

class Suplidor(Persona):	
	pass
		

class Empleados(Persona):
	def __init__( self, codigo, nombre, apellidos, telefono, salario ):
		self.salario = salario
		return super().__init__(codigo, nombre, apellidos, telefono)


E = Empleados(1, "Juan", "Doe", "809-220-1111", 50000)
E.Saludar()