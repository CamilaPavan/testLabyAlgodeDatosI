"""
Las definiciones de clases, al igual que las definiciones de funciones (instrucciones def) deben ejecutarse antes de que tengan efecto alguno.
    Es decir, la defino y despues las uso. ES IMPORTANTE EL ORDEN 
Para nombrar clases se deben utilizar la convención “CapWords” (palabras que comienzan con mayúsculas SeEmpiezaTodoConMayuscula
Instanciar un objeto es crear un objeto de la clase

"""

class Lapiz:
  pass
  
lapiz_1 = Lapiz() #creo una instancia o objeto de la clase, no darle mucha bola, ver ejemplo de abajo. 

"""
ATRIBUTOS: 
Existen dos tipos de atributos:
    Atributos de instancia u objeto: Pertenecen a la instancia de la clase o al objeto. 
    Son atributos particulares de cada instancia, en nuestro caso de cada perro.

    Atributos de clase: Se trata de atributos que pertenecen a la clase, por lo tanto serán COMUNES PARA TODOS LOS OBEJTOS.

Para crear atributos de instancia para nuestro objeto de la clase, por ejemplo el color y la longitud.    
Se crea un método __init__ que será llamado automáticamente cuando se crea un objeto. Se trata del constructor.

"""

class Lapiz:
    # El método __init__ es llamado al crear el objeto
    marca = "Faber Castel" #este atributo esta afuera del constructor porque aplica para todo, es un atributo de clase
    def __init__(self, color, longitud):
#es self representa la instacia de la clase, es decir, "YO" objeto que me estoy cambiando, esta SIEMPRE
        print(f"Creando un lapiz de color {color}, que mide {longitud} cm")
        # Atributos de instancia
        self.color = color
        self.longitud = longitud
        #self. #para agregar 
        #self. #para agregar 

lapiz_1 = Lapiz("rojo",25) #cuando llamo aca, llamo al constructor, que es la funcion ya con los parametros
print(type(lapiz_1))
#acceder a los atributos
print(lapiz_1.color) #si pongo el punto y el atributo me devuelve eso 



"""
El self se pasa como parámetro de entrada del método. Es una variable que representa la instancia de la clase, y deberá estar siempre ahí.

El uso de__init__ y el doble __ en un metodo es el constructor de la clase, es una metodo cuya misión es inicializar un objeto de una clase.
"""