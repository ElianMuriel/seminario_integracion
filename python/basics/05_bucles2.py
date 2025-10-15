"""
Pide el numero de empleados y luego el sueldo de cada uno.
suma y muestra la nomina total
"""
empleados=int(input("Número de empleados"))
suma=0
for i in range(empleados):
    suma+=float(input(f"sueldo empleado {i+1}"))
print("Total nomina = ",suma)