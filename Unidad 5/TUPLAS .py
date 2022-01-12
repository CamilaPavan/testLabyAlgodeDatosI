"""
Las tuplas son un tipo o estructura de datos que permite almacenar datos de una manera muy parecida a las listas, 
con la diferencia de:
    Son inmutables: No pueden ser modificadas una vez declaradas
    Se inicializalizan con parentesis ()
    Dependiendo de lo que se quiera hacer, las tuplas pueden ser más rápidas.
"""

lista=[1,2,3]
tupla2=(lista,4,5,6) #puedo meter una lista dentro de la Tupla. 
lista.append(4)
print(tupla2 [0][3]) #asi accedo a los elementos dentro de la lista, es decir, en el espacio cero, el elemento 3, 
#En este caso es el 4 que agrege con el append. 


#castear una tupla a lista para modificar. 
tupla=(1,2,3) 
print(type(tupla))
print(tupla)  
#castear una lista a tupla 
lista = list(tupla)
print(type(lista))
print(lista)