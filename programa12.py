#Dada una lista de números retornar el número menor y su posición en la lista
def encontrar_menor_y_posicion(lista):
    if not lista:
        return None, None  # Devolver None si la lista está vacía
    
    menor = lista[0]
    posicion = 0

    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            posicion = i
    
    return [menor, posicion]

lista_numeros = [4, 8, 2, 10, 5]
resultado = encontrar_menor_y_posicion(lista_numeros)

print("El número menor y su posición en la lista son:", resultado)
