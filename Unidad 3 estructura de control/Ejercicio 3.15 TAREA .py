"""
El programa debe:
*    Pedir al usuario una cantidad de tramos de un viaje
*    Pedir al usuario la duración en minutos de cada tramo
*    Calcular el tiempo total de viaje
*    No deben generar errores
"""
while True:
    acum = 0
    try:
        tramos = int(input("Ingrese la cantidad de tramos "))
        for i in range (1, tramos+1):
            minutos = float (input(f"cuando minutos dura el tramo {i}: "))
            acum += minutos
        print (f"El tiempo final de {tramos} tramos es de {round(acum/60,2)} horas")
        break
    except:
        print ("error")