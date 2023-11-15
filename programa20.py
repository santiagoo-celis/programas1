#Escriba una función para verificar si dos matrices son iguales o no.
def son_matrices_iguales(matriz1, matriz2):
    filas_matriz1, columnas_matriz1 = dimensiones_matriz(matriz1)
    filas_matriz2, columnas_matriz2 = dimensiones_matriz(matriz2)

    if filas_matriz1 != filas_matriz2 or columnas_matriz1 != columnas_matriz2:
        return False  # Las matrices tienen dimensiones diferentes y no pueden ser iguales

    for i in range(filas_matriz1):
        for j in range(columnas_matriz1):
            if matriz1[i][j] != matriz2[i][j]:
                return False  # Las matrices no son iguales en algún elemento

    return True  # Las matrices son iguales

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
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

if son_matrices_iguales(matriz1, matriz2):
    print("Las matrices son iguales.")
else:
    print("Las matrices no son iguales.")
