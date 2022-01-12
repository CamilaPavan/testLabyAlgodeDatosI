while True:
    palabra= input("Ingrese una palabra: ")
    if not palabra.isalpha():
        print("la palabra no es correcta")
    else:
        break

while True:
    numero = input ("ingrese un numero: ")
    if numero.isnumeric():
        print  ("ingreso un numero")
        break
    else: 
        print ("ingrese nuevamente un numero por favor el numero")