"""
Pide salario y desempeño (1-5)
si el desempeño es:
>4 = 15%
>3 = 10%
>2 = 5%
>1 = 2%
"""
salario = float(input("Ingresa tu salario actual: "))
desempeño = int(input("Ingresa tu calificación de desempeño (1 a 5): "))

if desempeño > 4:
    aumento = 0.15
elif desempeño > 3:
    aumento = 0.10
elif desempeño > 2:
    aumento = 0.05
elif desempeño > 1:
    aumento = 0.02
else:
    aumento = 0.0

incremento = salario * aumento
nuevo_salario = salario + incremento

print(f"Aumento: ${incremento:.2f}")
print(f"Nuevo salario: ${nuevo_salario:.2f}")
