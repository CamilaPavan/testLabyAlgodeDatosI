"""
Crear una funcion que debe: (usar diccionario)

Guardar en un diccionario los precios de las frutas de la tabla.
Preguntar al usuario por una fruta, un número de kilos y mostrar por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando ERROR.
Fruta	Precio
banana	50
manzana	80
pera	100
naranja	30
"""

frutas = {
    "banana" : 50,
    "manzana": 80,
    "pera" : 100,
    "naranja":30,
}

def precio_final(stock_frutas):
    fruta = input("Ingrese la fruta a comprar: ").casefold()
    valor = stock_frutas.get(fruta,'La fruta no está en el stock')
    while True:
        if valor == "La fruta no está en el stock":
            print(valor)
            break
        else: 
            try:
                kilos = int(input("Ingrese la cantidad de Kilos a comprar: "))
                precio = valor*kilos
                print(f"{kilos} kilos de {fruta} es: {precio}")
                break
            except:
                print("Reintentar, valor erroneo.")

def valor_a_pagar():
    while True:
        frutas=input("Ingrese la fruta: ")
        if frutas in frutas:
            kilos = int(input("Ingrese numero de kilos: "))
            print(f"El precio de {frutas} es de {(frutas.get(frutas)*kilos)} ")
            break
        else:
            print("Error")


def venta_de_fruta():
    fruta=input("Ingrese la fruta que desea: ").capitalize()
    if fruta in frutas:
        while True:
            try:
                cantidad=float(input("Ingrese la cantidad de kilos: "))
                precio=(frutas.get(fruta))*cantidad
                print(f"Por {cantidad}Kg. de {fruta} debe pagar: {precio}")
                return
            except:
                print("Cantidad Erronea.")
    else:
        print("La fruta no existe")
venta_de_fruta()
