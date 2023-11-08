#Programa para ingresar ángulos de un triángulo y verifique si es válido o no
angulo1 = int(input("Primer ángulo: "))
angulo2 = int(input("Segundo ángulo: "))
angulo3 = int(input("Tercer ángulo: "))
if angulo1 + angulo2 + angulo3 == 180:
    print("Triángulo válido.")
else:
    print("Triángulo no válido.")