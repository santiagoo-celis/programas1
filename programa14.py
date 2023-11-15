#Dada una lista de números hallar la mediana
def ordenar_burbuja(lista):
    n = len(lista)   
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
def encontrar_mediana(lista):
    if not lista:
        return None  # Devolver None si la lista está vacía
    # Ordenar la lista usando el algoritmo de burbuja (puedes usar otro algoritmo)
    ordenar_burbuja(lista)
    n = len(lista)
    if n % 2 == 1:
        # La longitud de la lista es impar
        mediana = lista[n // 2]
    else:
        # La longitud de la lista es par
        mediana = (lista[n // 2 - 1] + lista[n // 2]) / 2
    return mediana
lista_numeros = [4, 8, 2, 10, 5]
resultado = encontrar_mediana(lista_numeros)

print("La mediana de la lista es:", resultado)
