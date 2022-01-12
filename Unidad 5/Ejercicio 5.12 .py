"""
Ejercicio 5.12
Crear una funcion que debe: (usar diccionario)

Preguntar al usuario su nombre, edad, dirección y teléfono 
y lo guardar en un diccionario.
Mostrar por pantalla el mensaje: "nombre" tiene "edad" años, vive en "direccion" 
y su número de teléfono es "telefono".
"""

datos_persona = {}
def dato_de_personas_mal():
    nombre = input("ingrese su nombre: ").capitalize()
    datos_persona.update({"Nombre":nombre}) #tengo que poner la key entre comillas y el valor despues de los dos puntos
    while True:
        try:
            edad=int("por favor coloque su edad")
            datos_persona.update({"Edad" : edad})
            break
        except:
            print("error en la edad")
    direccion= input("por favor ingrese su direccion").capitalize
    datos_persona.update({direccion})
    while True:
        try:
            telefono = int(input("Por favor ingrese su telefono ej(351123456): "))
            datos_persona.update({"Telefono":telefono})
            break
        except:
            print("Error de datos")

#print(datos_persona)


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

datos_de_persona()
print(datos_persona.items())
print(f"{datos_persona.get('Nombre')} tiene {datos_persona.get('Edad')} vive en {datos_persona.get('Direccion')} su telefono es {datos_persona.get('Telefono')}")
