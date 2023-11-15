#Escriba una función para multiplicar dos matrices.
def multiplicar_matrices(matriz1, matriz2):
    filas_matriz1, columnas_matriz1 = dimensiones_matriz(matriz1)
    filas_matriz2, columnas_matriz2 = dimensiones_matriz(matriz2)

    if columnas_matriz1 != filas_matriz2:
        return None  # No se pueden multiplicar las matrices

    resultado = []

    for i in range(filas_matriz1):
        fila_resultado = []
        for j in range(columnas_matriz2):
            producto_parcial = 0
            for k in range(columnas_matriz1):
                producto_parcial += matriz1[i][k] * matriz2[k][j]
            fila_resultado.append(producto_parcial)
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

resultado = multiplicar_matrices(matriz1, matriz2)

print("La matriz resultante de la multiplicación es:")
for fila in resultado:
    print(fila)
