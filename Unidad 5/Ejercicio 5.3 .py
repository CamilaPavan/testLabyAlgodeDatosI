"""
Crear una funcion que debe:

Pedir al usuario 5 materias 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
Verficiar que sea un nombre correcto
Almacenar los nombres en una lista
Mostrar las materias en orden alfabetico
No deben aparecer y se deben tener en cuenta todos los posibles errores
"""

def ordenamiento_palabras ():
    lista_materias=[]
    for i in range(5):
        while True:
            materia=input(f"ingrese la materia {i+1}: ")
            if materia.isalpha():
                lista_materias.append(materia)
                break
            else:
                print ("error en el nombre de la materia,")
                
    lista_materias.sort()
    print(lista_materias)
    

ordenamiento_palabras()
