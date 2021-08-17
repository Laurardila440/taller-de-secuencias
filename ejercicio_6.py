"""
entradas 
numero  de alumnos-->nta
numero de niños-->int-->nh
numero de niñas-->int-->nm
salidas
porcentaje total de alumnos-->pta
porcentaje de niños-->pnh
porcentaje de niñas -->pnm
"""
nta=input(input("digte el numero total de alumnos"))
nh=int(input("digite el numero de niños"))
nm=int(input("digte el numero de niñas "))
#caja negra 
pta=(nh+nm)
pnh = (nh*100)/pta
pnm = (nm*100)/pta
print("el porcentaje de mujeres es de un: ""{:.0f}".format(pnm),"%")
print("el porcentaje de hombres  es de un: ""{:.0f}".format(pnh) ,"%")
