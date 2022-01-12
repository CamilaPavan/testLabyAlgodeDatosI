i=1
while True: #como no tengo bandera, directamente al while le pongo TRUE. 
  print(i)
  i+=1
  if i==10:
    break#me voy del while

while True:
  try:
      dato1 = input("Ingrese la palabra clave: {python} ")
      if dato1 == "python":
        print("usted ingreso la palabra python")
        break #como si hizo lo que necestirabamos, TUKI se rompe. 
      else:
        print("no ingreso la palabra clave")
  except:
    print("se ha encontrado un error")