"""
Escribe un programa que pida edad, años de experinecia y si tiene titulo universitario.
Un candidato es elegible si tiene >=21 años y experiencia>=2 años o título.
Muestra Elegible o No Elegible
"""

edad = int(input("Edad del candidato"))
exp = float(input("Años de experiencia"))
tiene_titulo = input("Tiene título universitario? s/n").strip().lower()=="s"

if(edad>=21 and (exp>=2 or tiene_titulo=="s")):
    print("Elegible")
else:
    print("No Elegible")