flag1 = True
while flag1:
  primer_color=input("ingrese el 1° color (rojo o azul): ")
  if not primer_color.isalpha(): # verificamos q se haya escrito un string, el not lo niega.
    print("ingrese un string")
  elif primer_color=="rojo":
    while flag1:
      segundo_color=input(f"ingrese el 2° color (azul o verde) para mezclar el {primer_color}: ")
      if not segundo_color.isalpha(): # verificamos q se haya escrito un string
        print("ingrese un string")
      elif segundo_color=="azul":
        print(f"el color formado entre {primer_color} y {segundo_color} es Magenta")
        flag1 = False
      elif segundo_color=="verde":
        print(f"el color formado entre {primer_color} y {segundo_color} es Amarillo")
        flag1 = False
      else:
        print("Ingrese por favor azul o verde")
  elif primer_color=="azul":
    while flag1:
      segundo_color=input(f"ingrese el 2° color (verde o rojo) para mezclar el {primer_color}: ")
      if not segundo_color.isalpha(): # verificamos q se haya escrito un string
        print("ingrese un string")
      elif segundo_color=="verde":
        print(f"el color formado entre {primer_color} y {segundo_color} es Cian")
        flag1 = False
      elif segundo_color=="rojo":
        print(f"el color formado entre {primer_color} y {segundo_color} es Magenta")
        flag1 = False
      else:
        print("Ingrese por favor rojo o verde")
  else:
    print("Ingrese por favor azul o rojo")