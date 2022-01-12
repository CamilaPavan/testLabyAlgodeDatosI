#deportes en el polideportivo
futbol = True
basket = True
voley = False 
#condiciones de los amigos
condicion_amigo1 = futbol
condicion_amigo2 = basket or voley
condicion_amigo3 = not voley #si hubiera Voley este amigo no iria.

van_los_amigos = (condicion_amigo1) and (condicion_amigo2) and (condicion_amigo3)

#Cuando a una variable, le pongo varias variables conectadas con conectores logicos, la respuerta es T o F dependiendo. 


print(f"Los amigos van a ir? {van_los_amigos}")