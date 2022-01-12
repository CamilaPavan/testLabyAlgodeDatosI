"""
El programa debe:

pedir al usuario una palabra
pedir un numero al usuario
mostrar la palabra por pantalla la cantidad de veces que diga el numero
no debe generar errores
"""

i = 1
flag = True
while flag:

    try: 
        palabra = str(input("Ingrese por favor una palabra: "))
        cantidad = int (input("ingrese la cantidad de veces que desea que se repita "))
        while i <= cantidad:
            print (f"{palabra}")
            i += 1
        flag = False
    except:
        print ("no ingreso correctamente la informacion")
