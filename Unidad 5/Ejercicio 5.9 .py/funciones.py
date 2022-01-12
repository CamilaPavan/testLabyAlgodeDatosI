taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]

#la funcion preugnta el recorrido, y muestra que chofer puede hacer el viaje. 
def recorrido_del_viaje():
    while True:
        try: 
            recorrido = float(input("indique la cantidad de kilomentros que desea recorer"))
            if recorrido > 0:
                break
        except:
            print("error, por favor coloque nuevamente los kilometros")
    if recorrido <= 30:
        print (f"el recorrido lo puede realizar con el \t{taxis [1][0]}\t {taxis [1][1]}\t{taxis[1][2]} ")
    elif recorrido >30 and recorrido <=45:
        print (f"el recorrido lo puede realizar con el \t{taxis [1][1]}\t{taxis[1][2]} ")
    elif recorrido >45 and recorrido <= 50:
        print (f"el recorrido lo puede realizar con el \t{taxis[1][2]} ")
    else:
        print("Lamentablemente ningun chofer recorre esa cantidad de kilometros")


# Modificar nombre chofer segun el nombre del auto. auto_1 -> "federico"

def modificar_nombre_chofer_mal():
    while True:
        eleccion = input(""" A que auto desea modificarle el nombre del chofer :
                            1. auto_1
                            2. auto_2
                            3. auto_3
                            Opcion: """)
        if eleccion == "1":
            nombre = pedir_nombre()


            break
        if eleccion == "2":
            pass
            break
        if eleccion == "3":
            pass
            break
        else:
            print ("no ingreso ninguna opcion correcta")

def pedir_nombre():
    nombre_nuevo = input ("por favor coloque el nombre del chofer")
    return nombre_nuevo

def listar():
    print("AUTO   -   CHOFER    -    RECORRIDO")
    for i in range(len(taxis[0])):
        print(f"{taxis[0][i]} \t {taxis[1][i]} \t{taxis[2][i]}")


def modificar_nombre_chofer():
    listar()
    while True:
        indicar_auto = input("Nombre del auto a modificar: ")
        if indicar_auto in taxis[0]:
            taxis[1][taxis[0].index(indicar_auto)] = input("Nuevo nombre del chofer: ")
            listar()
            break
        else:
            print("no existe ese auto")

def nuevo_viaje():
    while True:
        try:
            while True:
                distancia = float(input("Ingrese la distancia del viaje:"))
                if(distancia <= 0):
                    print("La distancia debe ser mayor que cero")
                else:
                    print("Posibles autos que podrían realizar el viaje:")
                    for columnas in range(len(taxis[2])):
                        if(distancia <= taxis[2][columnas]):
                            print(f"Auto: {taxis[0][columnas]} - Chofer: {taxis[1][columnas]}")
                    return
        except:
            print("Debe ingresar una distancia válida")


#    6. Observar informacion de un chofer, verificando su existencia previamente
def info_del_chofer():
    chofer=input("por favor ingrese el nombre del chofer")
    if chofer.isalpha():
        if chofer in taxis[1]:
                        print (f"El chofer maneja el {taxis[0][taxis[1].index(chofer)]} y hace {taxis[2][taxis[1].index(chofer)]} kilómetros.")
        else:
            print("Este chofer no trabaja en esta empresa")

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


