#Programa para verificar si un caracter está en mayúsculas o en minúscula
caracter = input("Ingrese un carácter: ")
if 'A' <= caracter <= 'Z':
    print("Mayúscula.")
if 'a' <= caracter <= 'z':
    print("Minúscula.")
else:
    print("No es una letra.")
