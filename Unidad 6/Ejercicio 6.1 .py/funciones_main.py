import clases_presentarse as clp

lista_personas=[]

def crear_personas():
    while True: #pide DNI 
        dni= str(input("por favor ingrese su DNI"))
        if dni.isdigit():
            flag_agregar = True
            for persona in lista_personas:
                if dni == persona.dni:
                    print ("ese DNI ya existe")
                    flag_agregar = False
                    break
            if flag_agregar == True:
                break #el DNI Es valido 
        else:
            print("el DNI no es correcto")
    while True: #pido nombre
        nombre= str(input("por favor ingrese su nombre: "))
        if not nombre.isalpha():
            print("El nombre no puede tener numeros")
        else:
            break
    while True:#pido apeliido
        apellido = str(input("por favor ingrese su apellido: "))
        if not apellido.isalpha():
            print("El nombre no puede tener numeros")
        else:
            break
    while True: #edad
        try:
            edad = int(input("por favor ingrese su edad: "))
            if edad <= 0:
                print ("la edad debe ser positiva o mayor a cero: ")
            else:
                break
        except:
            print ("Error de argumentos")

    residencia= input("ingrese su domicilio: ")
    nombre_instacia = dni
    nombre_instacia = clp.Persona (nombre, dni, apellido,edad,residencia)
    lista_personas.append(nombre_instacia)

def listar_personas():
    for persona in lista_personas:
        persona.presentarse()


def consultar_rango():
    print("------ Lista de personas------")
    for persona in lista_personas:
        print(f"{persona.dni}\t{persona.nombre}\t{persona.apellido}\t{persona.edad}\t")
    while True: #pide dni
        dni_consultar = input("ingrese el dni a consultar")
        if dni_consultar.isdigit():
            for persona in lista_personas:
                if dni_consultar == persona.dni:
                    persona.rango_edad()
                    return
