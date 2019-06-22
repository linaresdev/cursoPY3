## EJERCICIO # 1
## Hacer una función que potencie un número x a la y
print("EJERCICIO # 1")
print("Potencia de X a la Y")
print("-------------------------")

def potenciador(init, end):
	for X in range(init,end):
		print("-------------------------")
		for Y in range(1,10):
			print("Potencia de ", X, "^", Y, " = ", X ** Y)
	
potenciador(1, 6)