
MIMES = {
    'gif':'image/gif',
    'jpg':'image/jpeg',
    'jpeg':'image/jpeg',
    'png':'image/png',
    'pdf':'application/pdf',
    'txt':'text/plain',
    'zip':'application/zip'
    }

# obtenemos dato
response = input('ext name: ')
response = response.lower().strip()

# separamos archivo de extension
_, ext = response.split('.')


# Obtendo valor MIME correspondiente de diccionario
if ext.lower() in MIMES.keys():
    x = MIMES.get(ext)
    print(x)
else:
    print('application/octet-stream')