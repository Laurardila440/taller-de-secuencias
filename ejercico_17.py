"""
entrdadas
cantidad e dinero-->cd
ginecologo-->a
traumatologia-->b
pediatra-->c
salidas
40% del dinero-->int-->d
30% del dienro-->int-->e
"""
cd=int(input("Ingresar el presupuesto :  "))
#caja negra 
a= cd*0.40
b = cd*0.30
c = cd*0.30
#salida
print("El porcentaje de presupueto del Ginecología es de: " "{:.0F}".format(a),("COP"))
print("El porcentaje de presupueto del Traunatología es de: " "{:.0F}".format(b), ("COP"))
print("El porcentaje de presupueto del Pediatría es de: " "{:.0F}".format(c), ("COP"))