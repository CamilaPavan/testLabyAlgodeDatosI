diccionario = {}

#la funcion permite a una persona crear su propio diccionario
def diccionario_por_usuario():
    while True:
        condicion = input("""Desea agregar informacion al diccionario?
                        1. SI
                        2. NO
                        """)
        if condicion == "1":
            dato= input ("escriba la KEY del dato a ingresar ")
            if dato in diccionario:
                print ("dicha KEY ya se encuentra en el diccionario, prube con otra")
            else:
                informacion = input (f"que desea guardar en {dato}?: ")
                diccionario.update({dato:informacion})
                print (diccionario)
        elif condicion == "2" :
            print (f"Gracias, su diccionario quedo con la siguiente informacion {diccionario}")
            break
        else:
            print("no ingreso una opcion correcta")

diccionario_por_usuario()

#Imprimir de manera linda un diccionario
def imprimir_diccionario(nombre,diccionario):
  print(f"--------{nombre}--------")
  print(f"--key \t   Valor--")
  for i in diccionario:
    print(f"  {i}\t{diccionario.get(i)}") 


#Otra forma de imprimir diccionario, ESTE MEJOR 
def imprimir_diccionario2(nombre,diccionario):
  print(f"--------{nombre}--------")
  print(f"--key\tValor--")
  for i,j in diccionario.items(): #i trae los key (tupla) j trae los valores (tupla), porque son estaticas. 
    print(f"  {i}\t{j}")

nombre = "diccionario de cami" #el nombre del diccionario que le quiero poner 
imprimir_diccionario(nombre,diccionario) #aca los parametros


#agregar cosas a la listas del diccionario:
def agregar_peliculas_series(base):
    while True:
        base_mostrar = input("""
-------------AGREGAR AL CATÁLOGO-------------
Ingrese si requiere:
    1. Agregar peliculas
    2. Agregar series 
    3. Salir
Opcion:   """
            )
        if base_mostrar =="1":
            while True:
                nombre_pelicula = input("Ingrese el nombre de la nueva pelicula: ").casefold().capitalize()
                if nombre_pelicula not in base.get("peliculas"):
                    base.get("peliculas").append(nombre_pelicula) #con el get lo vuelvo como a lista, como para tratarlo asi 
                    break
                else:
                    print("Esa pelicula ya se encuentra en la base de datos")

#agregar cosas con KEY DEFINIDAS
datos_persona = {}
def datos_de_persona():
  nombre = input("Por favor ingrese el nombre: ").capitalize()
  datos_persona.update({"Nombre":nombre})
  while True:
    try:
      edad = int(input("Por favor ingrese su edad: "))
      datos_persona.update({"Edad":edad})
      break
    except:
      print("Error de datos")
  direccion = input("Por favor su direccion: ").capitalize()
  datos_persona.update({"Dirección":direccion})

  while True:
    try:
      telefono = int(input("Por favor ingrese su telefono ej(351123456): "))
      datos_persona.update({"Telefono":telefono})
      break
    except:
      print("Error de datos")

#mulplicar por valores que tengo
frutas= {}
def venta_de_fruta():
    fruta=input("Ingrese la fruta que desea: ").capitalize()
    if fruta in frutas:
        while True:
            try:
                cantidad=float(input("Ingrese la cantidad de kilos: "))
                precio=(frutas.get(fruta))*cantidad
                print(f"Por {cantidad}Kg. de {fruta} debe pagar: {precio}")
                return
            except:
                print("Cantidad Erronea.")
    else:
        print("La fruta no existe")


#Que el usuario cree el diccionario completo
def diccionario_por_usuario():
    while True:
        condicion = input("""Desea agregar informacion al diccionario?
                        1. SI
                        2. NO
                        """)
        if condicion == "1":
            dato= input ("escriba la KEY del dato a ingresar ")
            if dato in diccionario:
                print ("dicha KEY ya se encuentra en el diccionario, prube con otra")
            else:
                informacion = input (f"que desea guardar en {dato}?: ")
                diccionario.update({dato:informacion})
                print (diccionario)
        elif condicion == "2" :
            print (f"Gracias, su diccionario quedo con la siguiente informacion {diccionario}")
            break
        else:
            print("no ingreso una opcion correcta")





