"""
Entradas
venta1-->int-->venta_1
venta2-->venta_2
venta3-->venta_3
salida
sueldo-->float-->s
comisiones-->float-->c
"""
s=float(input("digite el sueldo"))
venta_1=float(input("digite venta uno: "))
venta_2=float(input("digite venta dos: "))
venta_3=float(input("digite venta tres: "))
#caja negra 
c=(venta_1+venta_2+venta_3)*0.10
total=(s+c)
#salida
print("el sueldo del trabador es :"+str(s))
print("la comisiones del trabajador es :"+str(c))
print("el total del sueldo y comisiones es:"+str(s+c))