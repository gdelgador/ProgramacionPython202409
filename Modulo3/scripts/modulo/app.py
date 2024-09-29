"""
REALIZAR UN PROGRAMA MENU QUE REALICE LAS SIGUIENTES OPERACIONES:

1. Mostrar un triangulo rectangulo de altura n
2. Calcula el factorial de un número
3. Realizar la suma de divisores de un numero
4. Salir
"""
# 1. Importamos librerias

# desde carpeta.nombre_archivo import nombre_funcion
from figuras.triangulo import mostrar_triangulo
# from numerico.mate import calcular_factorial_recursivo

# importas todas las funciones de un archivo
from numerico.mate import *

# importas todas las funciones de un archivo
from numerico import mate 


# 2. Definimos las contantes

MENSAJE_BIENVENIDA = "Bienvenido al menú interactivo"
MENSAJE_OPCIONES = """¿Qué quieres hacer?

1. Mostrar un triangulo rectangulo de altura n
2. Calcula el factorial de un número
3. Realizar la suma de divisores de un numero
4. Salir

Escribe una opción: """


# 3. Definimos la función y/o clases

def ingreso_entero(msg='Ingrese un número entero: ')->int:
    try:
        return int(input(msg))
    except:
        print('Error, el valor ingresado no es un número entero')
        return ingreso_entero(msg)
    

def main():

    print(MENSAJE_BIENVENIDA)

    while True:
        
        # Mostramos el menú de opciones
        opcion = input(MENSAJE_OPCIONES)

        if opcion == '1':
            altura = ingreso_entero('Ingrese la altura de la piramide: ')
            mostrar_triangulo(altura)
        elif opcion == '2':
            numero = ingreso_entero('Ingrese un número para calcular su factorial: ')
            factorial = mate.calcular_factorial_recursivo(numero)

            print(f'{numero}! = {factorial}')
        elif opcion == '3':
            numero = ingreso_entero('Ingrese un número para calcular la suma de sus divisores: ')
            suma_div = mate.sumar_divisores_numero(numero)
            print(f'La suma de los divisores de {numero} es: {suma_div}')

        elif opcion == '4':
            print('Saliendo del menú')
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")
    pass


# 4. Ejecutamos el código
if __name__ == '__main__':
    main()
    print('Finalizando el programa ...')
