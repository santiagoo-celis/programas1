#Programa para encontrar el máximo entre dos números.
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
# Compara los dos números
if numero1 > numero2:
    maximo = numero1
else:
    maximo = numero2
print("El número máximo es:", maximo)