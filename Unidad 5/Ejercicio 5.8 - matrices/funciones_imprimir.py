
def imprimir_matriz(matriz):
    print ("cod  - produc -  $ - stck")
    for i in range(len(matriz)-1): #pongo menos 1 porque sino empieza en 1 y da error
        print(f"{matriz[0][i]} - {matriz[1][i]} - {matriz[2][i]} - {matriz[3][i]}")

base_productos = [[1,2,3],["producto1","producto2","producto3"],[300,400,500],[5,4,7]]

#imprimir_matriz(base_productos)



def  imprimir_matriz2(matriz):
  print (f"-------------- PRODUCTOS --------------")
  print (f"C \t PRODUCTO \t Pr $ \t Stock")
  for  i  in range (len(matriz)- 1 ):
    if i != 0:
      print("") #para que no imprima el espacio
    for  j in range(len(matriz)):
      print (f"{ matriz [ j ] [ i ] } " , end = '\t' ) #\t hace tabulacion y da como cuadro 
  print ("")

#imprimir_matriz2 (base_productos)

def  imprimir_codigo_producto(matriz):
  print (f"-------------- PRODUCTOS --------------")
  print (f"C \t PRODUCTO \t")
  for  i  in range (len(matriz)- 1 ):
    if i != 0:
      print("") #para que no imprima el espacio
    for  j in range(2):
      print (f"{ matriz [ j ] [ i ] } " , end = '\t' ) #\t hace tabulacion y da como cuadro 
  print ("")



def consultar_productos_y_stock(matriz):
  print(f"--------------PRODUCTOS--------------")
  print(f"PRODUCTO \tstock ")
  for i in range(len(matriz)-1):
    if i !=0:
      print("")
    for j in range(1,3+1,2):
      print(f"{matriz[j][i]}",end='\t')
  print("")

consultar_productos_y_stock(base_productos)