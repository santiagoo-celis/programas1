lista_numeros = [4, 8, 2, 10, 5]

if not lista_numeros:
    print("La lista está vacía.")
else:
    mayor = lista_numeros[0]

    for numero in lista_numeros:
        if numero > mayor:
            mayor = numero

    print("El número mayor es:", mayor)
