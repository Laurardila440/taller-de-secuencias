"""
entradas 
valor de venta al publico-->int-->pvp
valor final pagado--<int-->vf
salidas
descuento final--in-->d
""""
vf=int(input("Ingrese el valor del precio final: "))
pvp=int(input("Ingrese el valor del producto para PVP: "))
v=(vf-pvp)/vf
d= vf*100
print("El porcentaje del precio PVP es de: ""{:.2F}".format(d),("%"))