## EJERCICIO # 5
## Un número palindrómico se lee igual en ambos sentidos. 
## El palíndromo más grande hecho del producto de dos números 
## de 2 dígitos es 9009 = 91 × 99. Cree una función que encuentre 
## el palíndromo más grande hecho del producto de dos números de 
## 3 dígitos.
from os import system

def is_palidromo(N):
	if str(N) == str(N)[:: -1]:
		return True
	else:
		return False

def iteratodor_palidromico():
	
	data = 0

	for N1 in range(100,999):
		for N2 in range(100,999): 
			M = N1*N2
			if is_palidromo( M ):
				P1 = N1
				P2 = N2
				data =  M

	return "{}{}{}{}{}".format(P1, " X ", P2," = ", M)

print("EJERCICIO # 5")
print("Calculador del palindrómo mas grande de 3 digitos")
print("-------------------------------------------------")
print("El palindrómo mas grande de 3 digito es :", iteratodor_palidromico());
	