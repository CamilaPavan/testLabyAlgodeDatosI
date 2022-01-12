
def minutos_a_hora(minutos):
    horas_finales = 0
    while  minutos > 60:
        minutos = minutos - 60
        horas_finales+=1

    #print(f"los {minutos_iniciales} son {horas_finales} hs:{minutos} min")
    return horas_finales,minutos

cantidad_de_minutos = 800
horas,minutos = minutos_a_hora(cantidad_de_minutos)
print(f"La duracion de todo el viaje es: {horas}hs: {minutos}min")

#Ejercicio de viaje completo, 5.4 