"""
Ejercicio 6.2
Crear una clase de Figura_Geometrica:

Cuyo constructutor debe inicializar los atributos tipo_de_figura, color, y tamaño (por defecto "pequeño")
Se deben crear 3 metodos en la clase:
Presentar la figura: Un {tipo_de_figura} de color {color} y tamaño {tamaño}
Cambiar color de figura e indicar nuevo color
verificar si la figura es tamaño pequeño, agrandar a tamaño grande

"""
import Clase as cl
while True:
    condicion=input(
    """ ------ MENU PRINCIPAL ------
    Por favor ingrese una opcion
            1. Presentar figura
            2. Cambiar color de figura
            3. cambiar tamano de pequeno a grande
            4. Salir
    Numero : """)
    if (condicion=="1"): 
        cl.presentarse()
    elif (condicion=="2"):
        cl.cambiar_color()
    elif (condicion=="3"):
        cl.verficar()
    elif (condicion=="4"):
            break
    else:
        print("ninguna opcion correcta")


