"""
Tienes un fichero "ventas.csv" que contiene datos de ventas en formato CSV.  
Cada línea del fichero tiene la siguiente estructura: 
    fecha,producto,cantidad,precio_unitario 

Debes leer el fichero, procesar los datos y calcular el total de ventas por producto. 
Finalmente, debes escribir los resultados en un nuevo fichero
total_ventas.txt.
"""
from pprint import pprint

# 1. lectura
ruta_archivo = '/workspaces/ProgramacionPython202407/Modulo4/src/ventas.csv' # ruta absoluta
# ruta_archivo = '../src/ventas.csv' # ruta relativa

listado_lineas = open(ruta_archivo, mode='r').readlines()

# 2. procesamiento

# 2.1. Crear un diccionario para almacenar las ventas
listado_ventas = []
for linea in listado_lineas:
    dicx = {}
    # separo los elementos de la linea
    elementos = linea.strip().split(',')

    # asigno los elementos a las claves del diccionario
    dicx['fecha'] = elementos[0]
    dicx['producto'] = elementos[1]
    dicx['cantidad'] = int(elementos[2])
    dicx['precio_unitario'] = float(elementos[3])

    # creo nuevos
    dicx['subtotal'] = dicx['cantidad'] * dicx['precio_unitario']

    # agrego el diccionario a la lista
    listado_ventas.append(dicx)

# 2.2. Agrupar las ventas por producto
dicx_ventas_por_producto = {}
for venta in listado_ventas:
    producto = venta['producto']
    subtotal = venta['subtotal']

    # genero diccionario productox:venta_subtotal
    dicx_ventas_por_producto[producto] = dicx_ventas_por_producto.get(producto, 0) + subtotal

# print(dicx_ventas_por_producto)

escribir_lista = [f'{producto};{total_venta}\n' for producto,total_venta in dicx_ventas_por_producto.items()]

# 3. escritura
ruta_archivo = '/workspaces/ProgramacionPython202407/Modulo4/src/total_ventas.csv' # ruta absoluta
# escribir en un archivo
open(ruta_archivo, mode='w').writelines(escribir_lista)
















