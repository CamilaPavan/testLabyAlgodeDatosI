#por POSICION, es que usamos generalmente: 
def suma(a,b):
  return a+b
    
print(f"la suma de {2} y {3} es: {suma(2,3)}")



#POR NOMBRE: Genera confusiones, mejor no usarlo pero saber que existe
def resta(numero_mayor,numero_menor):
  return numero_mayor-numero_menor
 
print(f"{resta(numero_menor=3 , numero_mayor=5)}") #no importa el orden en que se lo pase, los acomoda segun la funcion. 
#Se suele usar cuando tenes muchos parametros, por si no te acordas cual es cual. 



#POR DEFECTO: cuando tenemos un parametro opcional. 
def suma(a, b, c=0): #se le da un valor 0 para que no de error cuando no la use. 
    return a+b+c

print(suma(5,5))

print(suma(5,5,3))
print("hola")