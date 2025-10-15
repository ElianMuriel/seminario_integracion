"""
Pide numero de empleados
cada empleado solicita nombre y salario
determina quien tiene el mayor salario y muestralo
"""

num_empleados = int(input("¿Cuántos empleados vas a ingresar? "))

mayor_salario = 0
nombre_mayor_salario = ""

for i in range(num_empleados):
    print(f"\nEmpleado {i + 1}")
    nombre = input("Nombre: ")
    salario = float(input("Salario: "))

    if salario > mayor_salario:
        mayor_salario = salario
        nombre_mayor_salario = nombre

print(f"\nEl empleado con el mayor salario es {nombre_mayor_salario} con un salario de ${mayor_salario:.2f}")
print(i)
