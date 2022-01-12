"""
El programa debe:

pedir al usuario que ingrese la cant de dinero que dispone.
verificar que la cantidad ingresada sea un numero y sino mostrar error
verificar la cantidad de ingresada e indicar que auto o autos puede comprar
"""
Ford = 10000
Renault = 11000
Chevrolet = 15000

try:
    dinero_disponible= float (input("ingrese el importe del dinero con el que dispone "))
    if dinero_disponible >= 10000 and dinero_disponible <11000:
        print ("Puedes comprar un ford")
    if dinero_disponible >=11000 and dinero_disponible < 15000:
        print ("Puedes comprar un Ford o un Ranault") 
    if dinero_disponible >15000:
        print ("Puedes comprar la marca de autos que quieras")
    if dinero_disponible < 10000:
        print ("No puedes comprar un auto")

except:
    print("ingrese el importe en numeros")