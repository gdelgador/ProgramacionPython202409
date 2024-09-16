# determinar la fecha de nacimiento de una persona en base a su edad
YEAR_CURRENT=2024
edad = int ( input("Ingrese su edad actual: "))

fecha_nacimiento=YEAR_CURRENT - edad

# tipos de salida
#1
print("el año de nacimiento es "+ str(fecha_nacimiento)+" con "+str(edad)+" años")
#2
print(f"el año de nacimiento es {fecha_nacimiento} con {edad} años") # recomendacion
#3
print("el año de nacimiento es {} con {} años".format(fecha_nacimiento,edad))


