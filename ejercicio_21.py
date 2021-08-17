"""
entradas 
precio del contenido-->int-->pc
precio de cada cuenta-->int-->cc
salidas
recargo de cuota-->int-->r
porcentaje-->int-->p
total-->int-->t
"""
pc=int(input("Precio de la compuatdora: "))
cc= int(input("Costo de las cuotas de la computadora: "))
r= pc*0.01
p= cc+r
t=(p/pc)*100
print("El total de procentaje cobrado por cada cuota es de: ""{:.0F}".format(t),("%"))