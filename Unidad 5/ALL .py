"""
all sirve para conocer si TODOS los elementos de una 
coleccion cumplen un determiando criterio
"""


frutas = ['manzana', 'naranja', 'frutilla','123']

palabras = all(c.isalpha() for c in frutas)  #c es iterador 

print(f"son todas palabras: {palabras}")