def suma(a,b): #Definir la funcion
  try:
    suma= int(a)+int(b)
    print(f"la suma de {a} y {b} es: {suma}") #Puedo llamarla dentro del print
  except:
    print("argumentos malos")
    
suma("hola",5) #Le pongo los parametro con los que quiero que ejecute. 
suma(3,5)

#QUE DEVUELVE UN RETURN: El return SIEMPRE DEVUELVE una bariable, no hace falta declararla como en Jave por ejemplo. 
#

def suma(a,b):
  return a+b
    
print(f"la suma de {2} y {3} es: {suma(2,3)}")