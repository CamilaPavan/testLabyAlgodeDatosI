"""
Crear un prgrama que debe:

Contar con un stock de frutas y otro de verduras (El stock indica si venden o no esa fruta o verdura, no la cantidad) - 
dos listas que inician vacias

Contar con un menu y 3 funciones
    Agregar frutas o verduras al correspondiente stock (verificando que que sean nuevas)
    Consultar el stock de frutas o verduras
    Eliminar un elemento del stock
"""

import funciones as fn

while True:
    condicion=input(
"""Por favor ingrese una opcion
        1. Agregar frutas / verduras.
        2. Consultar stock de frutas o verduras.
        3. Eliminar un elemnto del stoclk.
        4. Salir
Numero : """)
    if (condicion=="1"): 
        fn.agregar_fruta_o_verdura()
    elif (condicion=="2"):
        fn.consultar_stock()
    elif (condicion=="3"):
        fn.eliminar_del_stock()
    elif (condicion=="4"):
        break
    else:
        print("ninguna opcion correcta")

