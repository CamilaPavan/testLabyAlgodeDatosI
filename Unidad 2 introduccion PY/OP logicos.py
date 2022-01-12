pizza_tiene_queso = True
pizza_tiene_tomate = False

print (f"la pizza me va a gustar:{pizza_tiene_queso and pizza_tiene_tomate}")  
#Se tienen que complir las condiciones para que de TRUE
#En este caso hay que poner el corchete que "agrege el and" para que no lo pase como texto

print(f"la pizza me va a gusta: {pizza_tiene_tomate or pizza_tiene_queso}")
#Como se cumple 1 una condicion es TRUE

#NOT es mas confunso, tiene que asegurarme de que algo es FALSO. ej:
print (not pizza_tiene_queso) #Como el valor es TRUE da FALSE
print (not pizza_tiene_tomate) #Como es FALSE me da TRUE , porque me confirma que es FALSE