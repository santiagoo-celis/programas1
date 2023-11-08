#Programa para verificar si un número es divisible o no por 5 y 11
numero = int(input("Ingrese un número: "))
if numero % 55 == 0:
    print("Es divisible por 5 y 11.")
else:
    print("No es divisible por 5 y 11.")
#Se utiliza 55 para saber si es producto de 5 y 11, si es producto es divisible de los contrario no lo es