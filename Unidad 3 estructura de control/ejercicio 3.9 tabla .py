"""
El programa debe:

pedir un dato numerico al usuario
imprimir la tabla del numero de 1 al 10
no deben aparecer errores.
"""


flag = True
while flag:
  try:
    dato_numerico = int(input("Ingrese un numero: "))
    flag = False #como ingreso el dato numerico, salgo del While. 
  except:
    print("error, ingrse de vuelta")

multiplicador=1  #este es mi "i" o contador, por eso no incremento. 

while multiplicador <= 10:
  print(f"{multiplicador} x {dato_numerico} = {multiplicador * dato_numerico}")
  multiplicador+=1