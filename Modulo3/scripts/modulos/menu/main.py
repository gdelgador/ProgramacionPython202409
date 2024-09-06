"""
Generaremos un programa menu que realice las siguiente tareas.

1. Saludar
2. Calcular el factorial de un numero
3. Calcular el area de un circulo
4. Suma de divisores de un numero
5. Generar un triangulo rectangulo
6. Salir
"""
# 1. Importamos Librerias
# from <nombre_carpeta> import <nombre_archivo> as <nombre_corto>
from mate import funciones as mate
from mate import areas

# import <nombre_archivo> as <nombre_corto>
# import validaciones

# from <nombre_carpeta>.<nombre_archivo> import <nombre_funcion>
from validaciones import ingreso_numero_entero


# 2. Definir las constantes
MENSAJE_BIENVENIDA = "Bienvenido al menú interactivo"
MENSAJE_OPCIONES = """¿Qué quieres hacer? Escribe una opción
1. Saludar
2. Calcular el factorial de un numero
3. Calcular el area de un circulo
4. Suma de divisores de un numero
5. Generar un triangulo rectangulo
6. Salir

RESPUESTA: """
MENSAJE_SALIDA = "¡Hasta luego! Ha sido un placer ayudarte"


# 3. Definimos Funciones y/o clases
def saludar():
    print("Hola, espero que estés teniendo un buen día")

def opcion_2():    
    numero = ingreso_numero_entero("Ingresa un número entero para calcular su factorial: ")

    factorial = mate.factorial_recursivo(numero)
    print(f"{numero}!: {factorial}")
    pass

def opcion_3():
    
    radio = ingreso_numero_entero("Ingresa el radio de un círculo para calcular su área: ")

    # genero una excepcion si el radio es negativo
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    
    # calculo el area del circulo
    area = areas.area_circulo(radio)
    print(f"El área de un círculo con radio {radio} es: {area}")
    pass

# 4. Definimos la función principal
def main():
    ### Código de la función principal

    print(MENSAJE_BIENVENIDA)
    while True:
        # mostrar las opciones del menu
        print(MENSAJE_OPCIONES)
        
        respuesta = input()
        if respuesta == '1':
            saludar()
        elif respuesta == '2':
            opcion_2()
        elif respuesta == '3':
            opcion_3()
        elif respuesta == '4':
            pass
        elif respuesta == '5':
            pass
        elif respuesta == '6':
            print(MENSAJE_SALIDA)
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")
        pass


    pass

# 5. Punto de entrada a la aplicación
if __name__ == '__main__':
    main()
