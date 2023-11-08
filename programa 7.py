#Escriba un programa para imprimir el Triángulo de Floyd
n = int(input("Ingrese el número de filas del Triángulo de Floyd: "))
numero = 1
for fila in range(1, n + 1):
    print(*range(numero, numero + fila))
    numero += fila