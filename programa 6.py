#Escriba un programa que dado un número imprima la suma de sus dígitos
numero = input("Ingrese un número: ")
suma_digitos = sum(int(digito) for digito in numero if digito.isdigit())
print("La suma de los dígitos es:", suma_digitos)