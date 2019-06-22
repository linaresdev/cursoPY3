# PRIMERA PRACTICA DEL CURSO DE PYTHON
# Esctudiante : Ramon A Linares Febles
# Email : rlinares4381@gmail.com



# (1)
# Hacer un programa que solicite una edad y responda la siguinete pregunta.
# Es menor de edad? (TRUE o FALSE)

print("Item # 1")
print("Para proceder devemos validar su edad ...")

edad = int(input("Introdusca su edad porfavor : ")) >= 18

print("Es menor de edad? ", edad )

# (2)
## Hacer un programa en python que convierta grado Celsius a Fahrenheit

print("Conversor de Cersius a Fahrenheit")
celsius = int(input("Porfavor intrudusca el valor en Cersius a converti: "))

print( "El valor en Fahrenheit es:", ((celsius*1.8)+32 ), "grados")

#(3)
# Realizar un programa en Python que calcule el peso molecular (peso por cantidad de atomos solicitado 
# por teclado) de una molecula compuesta de dos elementos

print("CARCULADORA DE PESO MOLECULAR");

peso = ( float(input("Introdusca peso del elemento a calcular:")) * int(input("Indique la cantidad del elemento espesificado:")) )

print("Peso total de la cantidad del elemento espesificado es:", peso, "g/mol" )

# (4)
# Realizar un programa en Python que pida por teclado las componentes de dos vectores de tres
# dimensiones y muestre su producto escalar. (el producto vectorial resulta de la suma de la 
# multiplicacion de cada componente correspondiente)

A1 = int(input("Ingrese la priema componente del vector A :"))
A2 = int(input("Ingrese la segunda componente del vector A :"))
A3 = int(input("Ingrese la tercera componente del vector A :"))

B1 = int(input("Ingrese la priema componente del vector B :"))
B2 = int(input("Ingrese la segunda componente del vector B :"))
B3 = int(input("Ingrese la tercera componente del vector B :"))

escalar = (A1*B1)+(A2*B2)+(A3*B3)

print("El producto escalar de los dos vectores en R3 es :", escalar)

# (5)
# Realizar un programa que solicite 4 notas por teclado, la promedie y responda las siguientes preguntas:
# Es Sumacumlauder?
# Es Magnacumlauder?
# Es Cumlauder?
# Es ChepaCumlauder?

N1 = float(input("Intrudusca la primera nota:"))
N2 = float(input("Intrudusca la segunda nota:"))
N3 = float(input("Intrudusca la tercera nota:"))
N4 = float(input("Intrudusca la cuarta nota:"))

premedio = (N1+N2+N3+N4) / 4

print("Es Sumacumlauder?", (premedio > 95))
print("Es Magnacumlauder?", (premedio > 85 and premedio <= 95))
print("Es Cumlauder?", (premedio > 78 and premedio <= 85))
print("Es ChepaCumlauder?", (premedio > 70 and premedio <= 78))