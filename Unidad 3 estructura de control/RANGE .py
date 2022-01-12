"""
Si se necesita iterar sobre una secuencia de números, es apropiado utilizar la función integrada range(), la cual genera progresiones aritméticas

Entonces el range() genera una secuencia de números que van desde 0 por defecto hasta el número que se pasa como parámetro menos 1.

Se pueden pasar hasta tres parámetros separados por coma, donde: SIEMPRE ENTRE PARENTESIS. 

El primero es el inicio de la secuencia
El segundo el final
El tercero el salto que se desea entre números.
    Por defecto se empieza en 0 y el salto es de 1. NO SE PUEDE HACER EN FLOAT EL SALTO. 
    Cuando el inicio es mas alto que el fin, porque quiero ir de menor a mayor, en el salto tengo que pone "-1" 

range(inicio, fin, salto)

Si llamamos a range() con (1,20,5), se generarán números de 1 a 20 de cincoo en cinco.

"""


for i in range(6): #empieza de 0 y va a ir hasta 5 .. Es como que digo "lo quiero 6 veces"
  print (i)

for i in range (3): #se imprime 3 veces lo que tengo en el print. 
    print ("hola")

for i in range (2,10,2):
    print (i)

for i in range(8,0,-1): #Cuando quiero hacer una cuenta regresiva. 
    print (i)

variable = 2
for i in range(1,variable+1,1): #para usar de parametro una variable. Le ponemos el "+1" para que incluya el valor, sino en este caso imprime solo el 1
  print(i)