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