"""
nota de los parciales-->int-->flot-->np,np1,np2,np3
nota de examen final-->float-->ne
nota de trabajos-->float-->ntrb 
salidas
promedio de los parciles -->float-->p
nota fianal-->nt
"""
np1=int(input("digite la nota del primer parcial"))
np2=int(input("digite la nota del parcial 2"))
np3=int(input("digite la nota del parcial 3"))
ne=int(input("digite la nota del examen final: "))
ntrb=int(input("digite la nota del trabajo: "))
#caja negra 
p=(np1+np2+np3)/3
notap = (np*0.55)
notane= (ne*0.30)
notatrb= (ntrb*0.15)
nt= (np+ne+ntrb)
#salidas
print("la nota final es : "+str(nt))