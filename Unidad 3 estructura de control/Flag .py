"""
es un concepto, generalmente es booleando, se le da V o F
SOLUCIONA LA VIDA
Cambiar la condicion 
Se puede llamar FLAG o como quieras. 

"""

flag = True # mi flag
while flag:
  contraseña = input("ingrese la contraseña: ")
  if contraseña =="1234":
    flag = False
    print("contraseña CORRECTA")
  else:
    print("contraseña incorrecta")