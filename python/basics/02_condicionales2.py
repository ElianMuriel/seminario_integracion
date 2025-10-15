"""
Sistema que pida pago por hora y horas trabajadas.
Las primeras 40h son normales, las extras se pagan al 150%
Calcula y muestra el total semanal

"""

pagoH = float(input("Pago por horas"))
horas = int(input("Horas Trabajadas"))


if((horas-40)>0):
    total=(40*pagoH)+((horas-40)*(pagoH*1.50))
    print("EL pago es",total)
else:
    total=(40*pagoH)
    print("EL pago es",total)