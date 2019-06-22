
class Padre():
	
	def __init__(self):
		print("Se ha instaciado un object")

class Hija(Padre):

	def metodo_clase_hija(self):
		print("Se ha instaciado el metodo de la clase hija")

class Nieta(Hija):

	def metodo_clase_nieta(self):
		print("Se ha instaciado el metodo de la clase nieta")