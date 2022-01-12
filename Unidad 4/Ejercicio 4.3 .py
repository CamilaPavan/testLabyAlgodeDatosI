"""
El programa debe:

Contar con 3 funciones:
    1.Contador de letras (letra,palabra): Debe contar la cantidad de letras que tiene una palabra o frase (Ambos parametros)
    2.Comparador de palabras (palabra1 vs palabra2): debe comparar que palabra tiene mas letra.IMPORANTE:deben ser palabras y no frases (verificar)
    3.Quitador de vocales(palabra a retirar las vocales): debe recibir una palabra o frase y quitar todas las vocales
Contar con un menu donde debe pedir al usuario que operacion realizar
Pedir los parametros y devolver el resultado al usuario
Gestionar posibles errores
"""

def contador_de_letras(letra,palabra_o_frase):
    palabra_o_frase
    contador = 0
    for i in palabra_o_frase:
        if i == letra:
            contador += 1
    return contador

letras = contador_de_letras("a", "la casa tiene muchas a")

print (f"cantidad de letras a en la frase es {letras}")
print (contador_de_letras("a","la casa tiene aaaaa muchas a "))

def comparador_de_palabras(palabra1,palabra2):
    contador1= 0
    contador2= 0
    for i in palabra1:
        contador1+= 1
        if i == " ":
            print ("ingreso una frase, no una palabra")
        
    for i in palabra2:
        contador2 += 1
        if i == " ":
            print ("ingreso una frase, no una palabra")
            break
    if contador1 < contador2:
        print (f"la palabra {palabra1} es mas corta que {palabra2}")
    else:
        print (f"la palabra {palabra1} es mas larga que {palabra2}")

comparacion = comparador_de_palabras("calculadora","helicoptero")
print (comparacion)

print(comparador_de_palabras("casa","casas"))

def quitador_de_vocales(palabra_o_frase):
    palabra_auxiliar = ""
    for i in palabra_o_frase:
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            palabra_auxiliar= palabra_auxiliar + i

    return palabra_auxiliar

print (quitador_de_vocales("una frase que tenga todas las vocalis"))

        






