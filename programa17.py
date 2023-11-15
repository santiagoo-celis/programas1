#Escriba una función para sumar dos matrices.
def sumar_matrices(matriz1, matriz2):
    if dimensiones_matriz(matriz1) != dimensiones_matriz(matriz2):
        return None  # No se pueden sumar matrices con dimensiones diferentes
    
    filas, columnas = dimensiones_matriz(matriz1)

    resultado = []
    for i in range(filas):
        fila_resultado = []
        for j in range(columnas):
            suma_elemento = matriz1[i][j] + matriz2[i][j]
            fila_resultado.append(suma_elemento)
        resultado.append(fila_resultado)

    return resultado

# Función auxiliar para obtener las dimensiones de una matriz
def dimensiones_matriz(matriz):
    if not matriz:
        return 0, 0  # La matriz está vacía

    filas = len(matriz)
    columnas = len(matriz[0]) if matriz[0] else 0  # Asumimos que todas las filas tienen la misma longitud

    return filas, columnas

matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

resultado = sumar_matrices(matriz1, matriz2)

print("La matriz resultante de la suma es:")
for fila in resultado:
    print(fila)
