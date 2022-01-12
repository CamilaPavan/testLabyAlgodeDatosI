"""
El for es un tipo de bucle, similar al while pero con ciertas diferencias.
la sentencia for de Python itera sobre los ítems de cualquier secuencia (una lista o una cadenas de caracteres), en el orden que aparecen en la secuencia.
Diferencias con el bucle while

El número de iteraciones de un for esta definido de antemano, mientras que en un while no.
Otra diferencia con respecto al while es en la condición, mientras que en el while la condición era evaluada en cada iteración para decidir si volver a ejecutar o no el código, en el for no existe tal condición, sino un iterable que define las veces que se ejecutará el código.
Cosas importantes

el i (iterador) no hace falta declararlo antes (como en el while)
"""
for i in "federico":
  print (i, end=",") #me imprime todo en el mismo reglon, separdo por coma. 

for i in "federico":
  print (i) #imprime todas las letras una abajo de la otra 

for i in (0,1,2,3,4,5): #arreglo / vectores. 
  print(i)

lista = ["hola","como", "estas"] #arreglo
for i in lista:
  print (i) #imprimir una lista. 