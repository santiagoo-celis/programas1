#Dada una lista de números hallar la media
def encontrar_media(lista):
    if not lista:
        return None  # Devolver None si la lista está vacía
    suma = 0
    cantidad = 0
    for numero in lista:
        suma += numero
        cantidad += 1
    media = suma / cantidad
    return media
lista_numeros = [4, 8, 2, 10, 5]
resultado = encontrar_media(lista_numeros)

print("La media de la lista es:", resultado)
