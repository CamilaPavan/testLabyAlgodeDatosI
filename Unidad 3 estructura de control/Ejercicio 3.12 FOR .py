"""
El programa debe:

Preguntar al usuario por una frase y una letra
mostrar por pantalla el número de veces que aparece la letra en la frase.
"""

frase = input ("por favor ingrese la frase ")
letra = input ("Digite la letra que desea saber cuantas veces se repite ")
contador = 0

for i in frase:
    if i == letra:
        contador += 1

print (f"la letra {letra} se repite {contador} de veces ")


