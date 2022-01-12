"""
Set (Conjuntos)
Los sets en Python son una estructura de datos usada para almacenar elementos.
Los set en Python son un tipo de estructura que permite almacenar varios elementos y acceder a ellos de una forma muy similar a las listas pero con ciertas diferencias:
Propiedades

Los elementos de un set son únicos, lo que significa que no puede haber elementos duplicados.
Los set son desordenados, lo que significa que no mantienen el orden de cuando son declarados.
Sus elementos deben ser inmutables, por lo que no pueden ser ni un diccionario ni una lista.
Usos

Los usos básicos de éstos incluyen verificación de pertenencia y eliminación de entradas duplicadas.
Los conjuntos también soportan operaciones matemáticas como la unión, intersección, diferencia, y diferencia simétrica.


Creacion de un set
Las llaves {} o la función set() pueden usarse para crear conjuntos.
IMPORTANTE!! para crear un conjunto vacío tenés que usar set(), no {}; esto último crea un diccionario vacío.
"""

conjunto_1 = {1,2,3,4,4,3,4,2}  #no lo importa si estan repetidos 
print(conjunto_1)
print(len(conjunto_1))
print(type(conjunto_1))

#Se itera con los numeros, for i in conjunto_1

 
conjunto_1 = {1,2,3,4,4} 
print(conjunto_1)
conjunto_1.add(2)
print(conjunto_1)
conjunto_2 = {5,6,7,4,3,8} 
#EDADES UNICAS, los elementos del conjuto 2 que estan en el 1 los elimina. DIFFERENCES 
print(conjunto_1.difference(conjunto_2))