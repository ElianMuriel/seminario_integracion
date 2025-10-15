"""
Vacaciones por antiguedad
Pide años de antiguedad y muestra dias de vacaciones segun 
<1=0
<3=3
<5=10
>=5=15
"""
anios=int(input("años de antiguedad"))
if(anios>=5):
    print("Días de vacaciones = 15" )
else:
    if(anios<5 and anios>=3):
        print("Días de vacaciones = 10" )
    else:
        if(anios<3 and anios>0):
            print("Días de vacaciones = 3" )
        else:
            print("Días de vacaciones = 0" )