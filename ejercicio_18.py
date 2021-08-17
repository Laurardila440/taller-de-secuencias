"""
entradas
cantidad prestada-->int-->cp
cantidad pagada-->int-->cc
deuda-->int-->d
salidas
tasa de interes-->t
"""
cp = int (input("Ingresem la suma de prestamo en bolivares: "))
cc = int (input("Ingrese la cantida pagada: "))
d=int(input)("ingrese el tiempo de pago de la deuda ")
d = cp-cc
t= (d/(cp*4))*100
print("El porncetaje de pagos anules es igaules a: ""{:.0F}".format(t),("%"))
