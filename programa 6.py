#Programa para encontrar el máximo entre dos números.
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
# Compara los tres números
if numero1 > numero2:
    maximo = numero1
if numero2 > numero3:
    maximo = numero2
else:
    maximo = numero3
print("El número máximo es:", maximo)
