"""
Identifique los divisores para cada uno de los numeros del 10 al 30.

"""
from pprint import pprint

# dicx_numeros = {}
# for numero in range(10, 31):

#     # obtengo divisores
#     listado_divisores = []
#     for i in range(numero):
#         # como range comienza en 0, debo sumar 1 para tener el rango de 1-100
#         div = i+1

#         if numero % div == 0:
#             # print(f'{div} es divisor de {numero}')
#             listado_divisores.append(div)
#         pass
    
#     # numero: listado_numeros
#     dicx_numeros[numero] = listado_divisores # aqui deberia ir el listado de los divisores del numero colocado como llave
#     pass

# pprint(dicx_numeros)


# Funciones
# ---------------------------
# Funciones nos permiten reutilizar código, nos sirven para agrupar un bloque de código que se ejecuta cuando la función es llamada


def genera_listado_divisores(num):

    # obtengo divisores
    listado_divisores = []
    for i in range(num):
        # como range comienza en 0, debo sumar 1 para tener el rango de 1-100
        div = i+1

        if num % div == 0:
            listado_divisores.append(div)
        
    # retorno el listado de los numero
    return listado_divisores



# genero un diccionario con los numeros del 10 al 30
dicx_numeros = {}
for numero in range(10, 31):

    # numero: listado_numeros
    dicx_numeros[numero] = genera_listado_divisores(numero) # aqui deberia ir el listado de los divisores del numero colocado como llave
    pass

# Imprimo para cada numero, su listado de divisores asociado
pprint(dicx_numeros)



