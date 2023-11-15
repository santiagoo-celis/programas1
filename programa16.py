#Escriba una función que indique las dimensiones de una matriz.
def dimensiones_matriz(matriz):
    if not matriz:
        return 0, 0  # La matriz está vacía
    filas = len(matriz)
    columnas = len(matriz[0]) if matriz[0] else 0  # Asumimos que todas las filas tienen la misma longitud
    return filas, columnas
mi_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
filas, columnas = dimensiones_matriz(mi_matriz)
print(f"La matriz tiene {filas} filas y {columnas} columnas.")
