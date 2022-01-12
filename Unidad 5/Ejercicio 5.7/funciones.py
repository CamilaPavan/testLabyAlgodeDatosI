

def pedido_numeros():
    lista_numeros = []
    contador=1
    while True:
        entrada = input(f"ingrese el {contador}° numero (entre el 1 y 10) o fin: ")
        if entrada == "fin":
            break
        else:
            try:
                if int(entrada)>0 and int(entrada)<=10:
                    lista_numeros.append(int(entrada))
                    contador+=1
                else:
                    print("Dato incorrecto!")
            except:
                print("Dato incorrecto!")
    
    return lista_numeros

def promedios(lista_principal):
    suma_total = sum(lista_principal)
    total_numero = len(lista_principal)
    return round(suma_total/total_numero,2)


#la funcion verifica cuantos numeros de la lista son menores que el indicado
def cantidad_numeros_menores (lista_principal):

    while True:
        try:
            numero_a_comparar=int(input("ingrese el numero a comparar"))
            break
        except:
            print ("por favor ingrese un numero")
    contador = 0
    for i in lista_principal:
        if i <= numero_a_comparar:
            contador +=1
    return contador

#La funcion verifica la cantidad de numeros mayores en la lista. 
def cantidad_numeros_mayores (lista_principal):
    while True:
        try:
            numero_a_comparar=int(input("ingrese el numero a comparar"))
            break
        except:
            print ("por favor ingrese un numero")
    contador = 0
    for i in lista_principal:
        if i >= numero_a_comparar:
            contador +=1
    return contador


#Verificar si un numero que desee el usuario esta en la lista
def numero_en_lista(lista_principal):
    while True:
        try:
            numero_comparar = int(input("Indique el numero a buscar: "))
            break
        except:
            print("Dato Incorrecto!")
    
    if numero_comparar in lista_principal:
        contador=True
    else:
        contador=False
    
    return contador


