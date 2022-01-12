"""
elif: El switch es una herramienta que nos permite 
ejecutar diferentes secciones de código dependiendo 
de una condición. Su funcionalidad es similar a usar
 varios if, pero por desgracia Python no tiene un 
 switch propiamente dicho.

Una sentencia condicional puede contener a su vez 
otra sentencia anidada
"""

condicion = int(input("Ingrese el numero de menu: "))

if condicion == "milanesa":
  print("ingreso 1")
elif condicion == 2:
  print("ingreso 2")
elif condicion == 3:
  print("ingreso 3")
elif condicion == 4:
  print("ingreso 4")
elif condicion == 5:
  print("ingreso 5")
else:
  print("ingrese nuevamente")

#Es como poner muchos "IF"