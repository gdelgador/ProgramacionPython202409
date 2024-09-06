"""
Una funcion es un bloque de código que solo se ejecuta cuando se llama.
Las funciones son reutilizables: 
    el mismo bloque de código se puede ejecutar muchas veces, lo que ahorra tiempo y esfuerzo.
Las funciones pueden tomar parámetros que se utilizan dentro de la función.
"""
## Problema 1
# Calcule la suma de los divisores para un número dado por el usuario.

# las funciones deberian ir al inicio del script
def es_divisor(numero, divisor):
    # retorna True si el modulo es 0 y False en caso contrario
    return numero % divisor == 0

def generar_listado_divisores_numero(numero):
    listado_divisores = []
    # debo buscar los divisores del numero entre [1, numero]
    for i in range(1, numero+1):
        # identifico si es divisor por media del modulo del numero
        if es_divisor(numero, i):
            listado_divisores.append(i)
    return listado_divisores

# Solicitar al usuario un número
numero = int(input('Ingrese un número: '))


# 2. identificar divisores del numero
listado_divisores = generar_listado_divisores_numero(numero)

# 3. Calcular la suma de los divisores
suma_divisores = sum(listado_divisores)
# 4. imprimo resultado
print(f'Los divisores de {numero} son:\nDivisores: {listado_divisores}\nSumaDivisores: {suma_divisores}')


## Problema 2
# Identificar si el 2 es divisor de 10
resultado = es_divisor(10, 2)
print(f'La validación de 10%2 es {resultado}') # True

# Problema 3
#  Identificar cada uno de los divisores del siguiente listado de numero [100, 15, 8, 79]

for numero in [100, 15, 8, 79]:
    listado_divisores = generar_listado_divisores_numero(numero)
    print(f'Los divisores de {numero} son: {listado_divisores}')

