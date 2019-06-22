
## (1) Escriba un programa de Python para sumar todos los elementos 
##     de una lista. Iral editor
def sumaList(data=""):

	S = 0

	for row in data:
		S += row

	return S


print(sumaList([1,2]))


## (2) Escriba un programa de Python para multiplicar todos los 
##     elementos de unalista.
def productoList(data=""):

	for row in data:
		row *= row
	return row


print(productoList([1,2]))

## (3) Escriba un programa de Python para obtener el número más 
##     grande de una lista.
def get_last_key(lists=[]):

	return lists[(len(lists) - 1)]


print(get_last_key(["arroz", "guandules", "frijoles", "tomates", "molondrones"]))

## (4) Escriba un programa de Python para obtener el número más 
##     pequeño de una lista.
def get_first_key(lists=[]):

	for row in lists:
		return row

print(get_first_key(["arroz", "guandules", "frijoles", "tomates", "molondrones"]))

## (5) Escriba un programa de Python para contar el número de cadenas 
##     en las que la longitud de la cadena es 2 o más y el primer y 
##     último carácter son los mismos de una lista dada de cadenas
##     Lista de muestra: ['abc', 'xyz', 'aba', '1221']
##     Resultado previsto: 2
def is_palidromo(N):
	if str(N) == str(N)[:: -1]:
		return True
	else:
		return False

def count_lists_str(lists=[]):

	X = 0

	if len(lists) >= 2:

		for row in lists:
			if is_palidromo(row):
				X += 1

	return X


print(count_lists_str(['abc', 'xyz', 'aba', '1221']))

## (6) Escriba un programa de Python para obtener una lista, ordenada 
##     en orden creciente por el último elemento en cada tupla de una
##     lista dada de tuplas no vacías.
##     Lista de muestras: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
##     Resultado esperado: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
lists = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lists.sort(key=lambda x: x[1])

print(lists)

## (7) Escriba un programa de Python para eliminar los duplicados de 
##     una lista.
def rm_reflection(lists=[]):

	newlist = []

	for item in lists:

		if item not in newlist:
			newlist.append(item)

	return newlist	

print(rm_reflection(["hola", 22, "que tal", "hola", "que tal", 22]))

## (8) Escribir un programa de Python para verificar si una lista está 
##     vacía o no.
def is_empty_lists(lists=[]):

	return (len(lists) > 0)

print(is_empty_lists(["hola"]))

## (9) Escriba un programa Python para clonar o copiar una lista. 
##     Ir al editor
lists = [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

clone_lists = lists.copy()

print(clone_lists)

## (10) Escriba un programa de Python para encontrar la lista de palabras 
##      que son más largas que n de una lista de palabras dada.
def max_count_item(N=0, lists=[]):

	out = []

	for row in lists:		
		if len(row) > N:
			out.append(row)

	return out
	

print(max_count_item(4, ["hola", "que tal", "hola mundo"]))

## (11) Escribe una función de Python que toma dos listas y devuelve True 
##      si tienen almenos un miembro común.
def is_in_lists(lists1=[], lists2=[]):

	for row in lists1:
		if (row in lists2):
			return True

	return False

print( is_in_lists(["A","b", "C"], ["X", "b", "Z"]) )

## (12) Escriba un programa de Python para imprimir una lista específica 
##      después de eliminar los elementos 0, 4 y 5.
##      Lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
##      Salida esperada: ['Verde', 'Blanco', 'Negro']
def rm_from_key(keys=[], lists=[]):
	
	V = []
	for key in keys:
		V.append(lists[key])

	if len(V) > 0:
		for x in V:

			lists.pop(lists.index(x))
		
	return lists
	

print( rm_from_key([0, 4, 5], ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']) )