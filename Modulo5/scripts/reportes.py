# Me solicitan generar un archivo excel por cada uno de los paises en el archivo 'wine_review'
import pandas as pd

# lectura
df_wine = pd.read_excel('/workspaces/ProgramacionPython202409/Modulo5/output/wine_review.xlsx')

paises = df_wine[df_wine.country.notna()]['country'].unique()
cantidad_paises_generar_reportes = len(paises)

print(f'Se tienen {cantidad_paises_generar_reportes} paises')


contador = 0
for pais in paises:
    pais_report = pais.lower().replace(' ', '_')
    
    # filtrar
    condition = (df_wine.country == pais)
    df_filter = df_wine[condition]

    # escribir
    df_filter.to_excel(f'/workspaces/ProgramacionPython202409/Modulo5/output/reportes/{pais_report}.xlsx', sheet_name=pais_report, index=False)
    print(f'Se genero el reporte para el pais: {pais}')
    contador +=1


print(f'Se generaron {contador} reportes')
print('Proceso Finalizado ...')

