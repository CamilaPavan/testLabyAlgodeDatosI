#el sino, si no se cumple la condicion entra al otro

"""
El programa debe:

pedir el ingreso de un número positivos al usuario 
y almacenar la respuesta en la variable numero.

Verificar que se trate de un numero entero y 
sino mostrar un error
Comprobar si el número es negativo. Si lo es, 
el programa debe avisa que no era eso lo que se había pedido. (si no hay error)
SI ES POSITIVO INDICARLO 
Finalmente imprimir siempre el valor introducido por el usuario.(si no hay error)
"""

try:
    numero = int(input("Ingrese un numero "))
    if numero < 0:
        print ("El numero no debe ser negativo ")
    else:
        print ("El numero es positivo")
    print (f"El valor ingresado es:  {numero}")
        
except:
    print("no ingresu un valor valido ")

#el ELSE entra cuando no entra el IF si o si, 