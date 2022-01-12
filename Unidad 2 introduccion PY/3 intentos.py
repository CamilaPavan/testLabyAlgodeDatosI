"""
El programa debe ser capaz de:
- solicitar dos argumentos al usuario
- verificar que los dos argumentos sean enteros y en caso contrario volver a solicitarlos
- dar al usuario 3 intentos para escribir los argumentos en total, (en caso de equivocarse en a o en b se resta un intento)
- imprimir por pantalla el resultado de la suma de ambos argumentos.
"""
def suma(a,b):
  resultado = int(a)+int(b)
  print (f"la suma de {a} y {b} es igual a: {resultado}")

i = 3
while i>0:
  try:
    print("Indique el argumento A")
    a = int(input())
    print("Indique el argumento B")
    b = int(input())
    suma(a,b)
    print("FIN")
    break
  except:
    print("ERROR: A o B no son numeros enteros")
    i=i-1
    print(f"quedan {i} intentos")