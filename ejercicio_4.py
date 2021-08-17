"""
Entradas 
compra-->int-->c
salidas 
Descuento-->flot-->d
"""
c=float(input("digite compra"))
#caja negra
d=(c*0.15)
total=(c-d)
#Salidas 
print("el total a pagar es de :"+str(total))
