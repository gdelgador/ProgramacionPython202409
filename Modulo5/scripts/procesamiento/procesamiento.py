"""
Crearemos un procesamiento de datos con pandas, a partir de una lectura de información.
realizaremos algunos calculos solictados y luego guardaremos la información en cierto formato.

Tienes un fichero ventas.csv que contiene datos de ventas en formato CSV.
Cada línea del fichero tiene la siguiente estructura: fecha,producto,cantidad,precio_unitario.
Debes leer el fichero, procesar los datos y calcular el total de ventas por producto.
Finalmente, debes escribir los resultados en un nuevo fichero total_ventas.txt.
"""

# import librerias
import pandas as pd


# coloco constantes

SCHEMA_DATOS = {
            'fecha': 'string',           # o pd.StringDtype()
            'producto': 'string',        # o pd.StringDtype()
            'cantidad': 'int64',
            'precio_unitario': 'float64'
        }

RUTA_ARCHIVO = '/workspaces/ProgramacionPython202407/Modulo5/scripts/ventas.csv' 
RUTA_SALIDA = '/workspaces/ProgramacionPython202407/Modulo5/scripts/total_ventas.txt'

# defino funciones y/o clases

class Procesamiento:

    def __init__(self, archivo):
        self.archivo = archivo

    def leer_archivo(self, esquema):
        # leo el archivo con esquema de datos
        df = pd.read_csv(self.archivo, sep=',', encoding='utf-8', dtype=esquema)
        return df
    
    def calcular_total_ventas_producto(self, df: pd.DataFrame)->pd.DataFrame:
        # agrupo por producto y sumo la cantidad y el precio unitario
        df = df.groupby('producto').agg({'cantidad':'sum', 'precio_unitario':'sum'}).reset_index()

        # calculo el total de ventas
        df['total_ventas'] = df['cantidad'] * df['precio_unitario']
        return df
    
    def guardar_resultados_csv(self, df: pd.DataFrame, ruta_salida):
        # guardo el archivo
        df.to_csv(ruta_salida, sep=';', encoding='utf-8', index=False)

def main():
    # instancio la clase
    process = Procesamiento(archivo = RUTA_ARCHIVO)

    print('Leyendo archivo...')
    df = process.leer_archivo(esquema = SCHEMA_DATOS)

    print('Calculando total de ventas por producto...')
    df_group = process.calcular_total_ventas_producto(df)

    print('Guardando resultados...')
    process.guardar_resultados_csv(df_group, 
                                   ruta_salida = RUTA_SALIDA)
    print('Proceso finalizado.')
    pass

# ejecuto el main
if __name__ == '__main__':
    main()