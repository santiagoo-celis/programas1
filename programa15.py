#Dada una lista de números devolver el valor de la moda (asumir que es una sola)
def encontrar_moda(lista):
    if not lista:
        return None  # Devolver None si la lista está vacía
    frecuencias = {}
    for numero in lista:
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1
    moda = max(frecuencias, key=frecuencias.get)
    return moda
lista_numeros = [4, 8, 2, 10, 5, 8, 8, 2, 8]
resultado = encontrar_moda(lista_numeros)
print("La moda de la lista es:", resultado)
