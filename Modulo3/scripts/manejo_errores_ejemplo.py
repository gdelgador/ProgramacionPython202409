# 1. Importamos librerias

# 2. Definimos las contantes

# 3. Definimos la función y/o clases

def area_rectangulo(base, altura):

    if base <0 or altura <0:
        raise ValueError("Los valores deben ser positivos")
    return base * altura


def ingreso_entero(msg='Ingrese un número entero: ')->int:
    try:
        return int(input(msg))
    except:
        print('Error, el valor ingresado no es un número entero')
        return ingreso_entero(msg)
    

# 4. Ejecutamos el código
base = ingreso_entero("Ingrese la base: ")
altura = ingreso_entero("Ingrese la altura: ")

area = area_rectangulo(base, altura)
print(f'El area del rectangulo es: {area}')