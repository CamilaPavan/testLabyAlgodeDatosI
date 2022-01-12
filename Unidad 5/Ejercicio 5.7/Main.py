"""
El programa debe:

Simular un programa que calcule estadisticas
Pedir al usuario una serie de numeros enteros el 1 al 10 (verificar) y guardarlos en una lista, hasta que el usuario ingrese "fin"
Luego mostrar un menu con 4 opciones
Calcular promedio
Verificar cuantos numeros son menores que el numero indicado por el usuario
Verificar cuantos numeros son mayores o igual que el numero indicado por el usuario
Verificar si un numero que desee el usuario esta en la lista
Gestionar posibles errores
Estructurar el programa a criterio propio
"""
import funciones as fn
lista_principal=[]
while True:
    condicion=input(
"""Por favor ingrese una opcion
        1. Agregar numeros a lista.
        2. calcular promedio
        3. cantidad de numeros mayores o iguales.
        4. Cantidad de numeros menores o iguales. 
        5. Chequear si esta en la lista o no. 
        6. Salir
Numero : """)
    if (condicion=="1"): 
        lista_principal = fn.pedido_numeros()
        print (lista_principal)
    elif (condicion=="2"):
        promedio_n_ingresados = fn.promedios(lista_principal)
        print (f"el promedio de los numeros ingresados a la lista es {promedio_n_ingresados}")
        print (lista_principal)
    elif (condicion=="3"):
        cantidad_mayores= fn.cantidad_numeros_mayores()
        print (f"la cantidad de numeros mayores es {cantidad_mayores}")
    elif (condicion=="4"):
        cantidad_menores=fn.cantidad_numeros_menores()
        print (f"la cantidad de numeros menoreses {cantidad_menores}")
    elif (condicion == "5"):
        chequar = fn.chequear_numero()
        print(chequar)
    elif (condicion == "6"):
        break
    else:
        print("ERROR")
    
