#ejemplo funcion con variable global
dinero_disponible = 50000.0
"""Ingresa dinero al sistema y actualiza el saldo"""
def ingresar_y_actualizar():
    global dinero_disponible #aviso que es global, y lo tengo que hacer con todas las funciones. 
    while True:
        try:
            dinero_ingresar = float(input("Ingrese dinero a depositar: "))
            if dinero_ingresar > 0 :
                break
            else:
                print("Por favor ingrese una suma positiva")
        except:
            print("Error en los parametros")

#las globales se declaran en donde la vamos a usar con las funciones. 