while True:
    try:
        while True:
            cantidad_tramos = int(input("Ingrese la cantidad de tramos: "))
            if(cantidad_tramos<=0):
                print("Por favor ingrese un numero mayor a cero")
            else:
                break

        tiempo_total_viaje=0
        for i in range(cantidad_tramos):
            while True:
                tiempo_tramo=int(input(f"Ingrese la duracion del tramo {i+1}: "))
                if(tiempo_tramo<0):
                    print("Por favor ingrese un numero mayor o igual a cero")
                else:
                    tiempo_total_viaje +=tiempo_tramo
                    break
        print(f"El tiempo total del viaje fue de: {round(tiempo_total_viaje/60,2)} horas")
        break
        
    except:
        print("error en las variables")