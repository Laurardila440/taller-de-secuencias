"""
Entrada 
edad1-->int-->edad_uno
edad2-->edad_dos
edad3-->edad_tres
salidas
promedio-->float-->p
"""
edad_uno=int(input("digite edad uno: "))
edad_dos=int(input("digite edad dos: "))
edad_tres=int(input("digite edad tres: "))
#caja negra 
p=(edad_uno+edad_dos+edad_tres)/3
#salidas
print("promedio es: "+str(p))