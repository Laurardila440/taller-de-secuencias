"""
entradas
nombre del trabajador-->int-->nm
horas trabajadas-->int-->ht
pago de una hora normal-->int-->pn
horas extras-->in-->he
valor minimo-->int-->val
cantidad de hijos-->int-->nh
salidas
salario final-->int-->sf
"""
nm= str(input("Nombre del trabjador: "))
ht=int(input("ingrese el numero de horas trabajdas: "))
pn=int(input("Ingrese el numero de horas normales trabajadas: "))
he =int (input("Ingrese el número de horas extras trabajadas: "))
val= int (input("El valor minimo de la hora de acuerdo al SMLV:  "))
nh=int(input("Ingrese el número de hijos: "))
he = val*0.25
valorhe = val+he
sht = (valorhe*he)+(val*pn)
cp= sht*0.05
sp= sht*0.07
dp= sht* 0.02
st1 = sht-(cp+sp+dp) 
dc= 250000
co= 180000
cstt=nh*173000
tts=(dc+co+cstt)+st1
print("El descuento de 5% por para forsozo es de: -""{:.0F}".format(cp))
print("El descuento de 7% por caja de ahorros es de: -""{:.0F}".format(sp))
print("El descuento de 2% por politica habitacional es de: -""{:.0F}".format(dp))
print("El abono de 250 mil COP por actualización academica es de: +"+str(dc))
print("El abono de 180 mil COP por la prima de hogar: +"+str(co))
print("El abono de 173 mil por cada hijo es de: +"+str(cstt))
print("Sueldo sin descuentos no abonos: ""{:.0F}".format(sht))
print("El suerldo neto mas descuentos y otros conceptos es de: ""{:.0F}".format(tts))