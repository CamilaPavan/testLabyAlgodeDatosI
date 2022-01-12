"""
pedir en orden el Nombre, apellido, edad y numero de calzado

verificar que cada uno sea el tipo de variable correcto (IMPORTANTE)
en caso verdadero imprimir de la siguiente manera el resultado:
ejemplo
Nombre: Lionel
Apellido: Messi
Edad: 34
Numero de Calzado: 42.5

en caso contrario imprimir error
"""

try:
    nombre = str (input("coloque su nombre "))
    apellido = str (input("coloque su apellido "))
    edad= int (input("coloque su edad"))
    calsado = float(input("coloque nu numero de calsado"))
    print (f"Nombre {nombre} \n Apellido {apellido} \n \
    Edad {edad} \n Numero de calsado {calsado}")

except:
    print ("los datos ingresados no son correctos")