if 1:
    print ("hola, estoy dentro del if")
#Hay que poner el tab para que quede dentro de la condicion
#Si no hay una condicion Python lo toma como true

try:
    edad = int(input("digite su edad"))
    if edad >= 18 : 
        print("Usted es mayor")
except:
    print("La edad no es correcta")

if (1<2): #condicion entre parentesis
    print ("ok")

if 1<2: #condicion sin parentesis
    print("asi tabien se puede")

#El bloque puede tener muchas instruciones, SI todos tienen que estar dentro del tab
