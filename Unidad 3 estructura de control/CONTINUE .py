"""
mostrar todos los numero del 1 al 10, exceptuando el 1
"""


i=0
while True:
  i+=1
  if i==5:
    continue #no va a hacer lo que esta abajao, pero vuelve el bucle. 
  print(i)
  if i == 10:
    break