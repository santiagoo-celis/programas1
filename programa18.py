#Escriba una función para multiplicar una matriz por un escalar.
def multiplicar_matriz_por_escalar(matriz, escalar):
    filas, columnas = dimensiones_matriz(matriz)

    resultado = []
    for i in range(filas):
        fila_resultado = []
        for j in range(columnas):
            producto = matriz[i][j] * escalar
            fila_resultado.append(producto)
        resultado.append(fila_resultado)

    return resultado

# Función auxiliar para obtener las dimensiones de una matriz
def dimensiones_matriz(matriz):
    if not matriz:
        return 0, 0  # La matriz está vacía

    filas = len(matriz)
    columnas = len(matriz[0]) if matriz[0] else 0  # Asumimos que todas las filas tienen la misma longitud

    return filas, columnas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

escalar = 2

resultado = multiplicar_matriz_por_escalar(matriz, escalar)

print("La matriz resultante de la multiplicación por escalar es:")
for fila in resultado:
    print(fila)
