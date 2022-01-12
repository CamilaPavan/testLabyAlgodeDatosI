"""
Agregar frutas o verduras al correspondiente stock (verificando que que sean nuevas)
consultar el stock de frutas o verduras
Eliminar un elemento del stock
"""
frutas = [] #listas vacias
verduras = [] #listas vacias


def agregar_fruta_o_verdura (): #la confuncion le permite al usuario agregar un elemento, siempre y cuando este no se encuentre en la lista 
    while True:
        fruta_o_verdura= (input("""
        Que desea agregar al stock
            1. FRUTA
            2. VERDURA
        :__"""))
        if (fruta_o_verdura == "1") or (fruta_o_verdura == "2"):
            break
        else:
            print("Opcion incorrecta")
    while True:
        elemento = input ("Coloque el nombre de la fruta o verdura: ")
        if elemento.isalpha():
            break
        else: 
            print ("ERROR")
    if fruta_o_verdura == "1":
        if elemento not in frutas:
            frutas.append(elemento)
            print (frutas)
        else:
            print ("el elemento ya se encuentra en la lista")
    
    if fruta_o_verdura == "2":
        if elemento not in verduras:
            verduras.append(elemento)
            print (verduras)
        else:
            print ("el elemento ya se encuentra en la lista")


def consultar_stock(): #la funcion permite consultar el stock
    while True:
        stock_de = (input("""
        Que stock desea consultar:
            1. FRUTA
            2. VERDURA
        :__"""))
        if stock_de == "1":
            print (f"el stock de frutas es {frutas}")
            break
        elif stock_de == "2":
            print (f"el sctock de verduras es {verduras}")
            break
        else:
            print("Opcion incorrecta, intente nuevamente ")

def eliminar_del_stock(): #esta funcion permite eliminar un elemento de la lista
    while True:
        fruta_o_verdura= (input("""
        De que lista desea eliminar un elemento del stock:
            1. FRUTA
            2. VERDURA
        :"""))
        if (fruta_o_verdura == "1") or (fruta_o_verdura == "2"):
            break
        else:
            print("Opcion incorrecta")
    while True:
        elemento = input ("Coloque el nombre de la fruta o verdura a eliminar: ")
        if elemento.isalpha():
            break
        else: 
            print ("ERROR")
    if fruta_o_verdura == "1":
        if elemento in frutas:
            frutas.remove(elemento)
            print (frutas)
        else:
            print ("el elemento no se encuentra en la lista")
    if fruta_o_verdura == "2":
        if elemento in verduras:
            verduras.remove(elemento)
            print (verduras)
        else:
            print ("el elemento no se encuentra en la lista")


