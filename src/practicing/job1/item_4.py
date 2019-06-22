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
