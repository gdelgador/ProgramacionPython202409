""""

Suma los divisores de los numeros del 5 al 20
"""

from pprint import pprint

def genera_listado_divisores(num):

    # obtengo divisores
    listado_divisores = []
    for i in range(num):
        div = i+1

        if num % div == 0:
            listado_divisores.append(div)
        
    # retorno el listado de los numero
    return listado_divisores



dicx_numeros = {}
for numero in range(5, 21):

    # numero: listado_numeros
    dicx_numeros[numero] = sum(genera_listado_divisores(numero)) # aqui deberia ir el listado de los divisores del numero colocado como llave
    pass

# Imprimo para cada numero, su listado de divisores asociado
pprint(dicx_numeros)




# {
#     numero: {
#         'divisores': [1, 2, 3, 6],
#         'suma_divisores': 12
#     }
# }
