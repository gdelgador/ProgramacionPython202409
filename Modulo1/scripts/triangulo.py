"""
Calcular el area de un triangulo, solicitar los datos de altura y base al usuario
"""

# 1. Solicitar los datos al usuario
base_triangulo = float(input("Ingrese la base del triangulo: "))
altura_triangulo = float(input("Ingrese la altura del triangulo: "))

# 2. Calcular el area del triangulo
area_triangulo = (base_triangulo * altura_triangulo) / 2

# 3. Mostrar el resultado

# str -> convierte un valor numerico a cadena
print("El area del triangulo es " + str(area_triangulo))

# f-string
print(f"El area del triangulo es {area_triangulo}")

# format
print("El area del triangulo de base {}  y altura {} es: {}".format(base_triangulo,altura_triangulo ,area_triangulo))





