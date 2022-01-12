taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3", "4to elemento"],[45,50,30]]

"""
print(len(taxis)) #te dice cuantas listas tiene
print(len(taxis[1])) #te cuenta cuantas variablas hay en fila "1" que en este caso es la 2
"""

#impirmir toda la matriz de manera ordenada
def listar():
    print(f"AUTO \t CHOFER \t RECORRIDO") #nombre de lo de abajo
    for i in range(len(taxis[0])): #pongo la lista cero porque recorro la longitud de autos
        print(f"{taxis[0][i]} \t {taxis[1][i]} \t{taxis[2][i]}")


#modificar un valor en la matriz
def modificar_nombre_chofer():
    listar()
    while True:
        indicar_auto = input("Nombre del auto a modificar: ")
        if indicar_auto in taxis[0]: #en la posicion cero, porque solo ahi busco el nombre del auto 
            taxis[1][taxis[0].index(indicar_auto)] = input("Nuevo nombre del chofer: ") #al poner = le cambio el valor 
            #voy a la lista 1 que estan los nombres de los chofes, y 
            #La segunda posicion es la que indico en el index, y lo igualo con el nuevo nombre
            listar()
            break
        else:
            print("no existe ese auto")


#consulta cantidad de km e indica que taxi puede hacer el recorrido 
def nuevo_viaje(): 
    while True:
        try:
            while True:
                distancia = float(input("Ingrese la distancia del viaje:"))
                if(distancia <= 0):
                    print("La distancia debe ser mayor que cero")
                else:
                    print("Posibles autos que podrían realizar el viaje:")
                    for columnas in range(len(taxis[2])): #los kilometros que hacen 
                        if(distancia <= taxis[2][columnas]):
                            print(f"Auto: {taxis[0][columnas]} - Chofer: {taxis[1][columnas]}")
                    return
        except:
            print("Debe ingresar una distancia válida")



#Chequear que se encuentre y dar la informacion
def info_del_chofer():
    chofer=input("por favor ingrese el nombre del chofer")
    if chofer.isalpha():
        if chofer in taxis[1]:
                        print (f"El chofer maneja el {taxis[0][taxis[1].index(chofer)]} y hace {taxis[2][taxis[1].index(chofer)]} kilómetros.")
        else:
            print("Este chofer no trabaja en esta empresa")

#Agregar algo / alguien
def nuevo_trabajador(Taxis):
    while True:
        nuevo_auto = input("Por favor ingrese un nuevo auto: ")
        Taxis[0].append(nuevo_auto)
        nuevo_chofer = input("Por favor ingrese el nombre del nuevo chofer: ")
        if nuevo_chofer.isalpha():
            Taxis[1].append(nuevo_chofer)
        else:
            print("Por favor ingrese un nombre que no contenga numeros ni caracteres.")
        nuevo_recorrido = int(input("Por favor ingrese el recorrido máximo que hará: "))
        Taxis[2].append(nuevo_recorrido)
        print({f"{Taxis}"})
        break
    return Taxis

