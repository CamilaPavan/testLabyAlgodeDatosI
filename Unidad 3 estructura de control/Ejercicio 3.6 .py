"""
Pedir un numero inicial
Pedir un numero 
imprimir desde el inicio al limitite
no debe generar errores
"""

flag = True
while flag:
  try: #solo chequeamos que ponga un entero
    numero_inicial=int(input("Ingrese un numero incial: "))
    numero_limite=int(input("Ingrese un numero limite: "))
  except:
    print("dije un numero")
  if (numero_inicial<numero_limite):
    while numero_inicial<=numero_limite:
      print(numero_inicial)
      numero_inicial+=1
    flag=False
  else:
    print("el numero incial debe ser menor que el limite")