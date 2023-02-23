import requests
import json
import os

# Hacer la solicitud GET a la API de TwitchInsights
response = requests.get('https://api.twitchinsights.net/v1/bots/all')
response_json = json.loads(response.text)

# Extraer el primer valor de cada objeto en el arreglo 'bots'
bots = response_json['bots']
bot_names = [bot[0] for bot in bots]

# Ordenar los nombres de los bots alfabéticamente
bot_names.sort()

# Escribir los nombres de los bots en un archivo temporal
with open('content/temp_file', 'w') as f:
    for name in bot_names:
        f.write(name + '\n')


# Comparar
# Leer los contenidos del archivo whitelist.md y almacenarlos en un conjunto
with open('content/whitelist', 'r') as f:
    whitelist = set(f.read().splitlines())

# Leer los contenidos del archivo temporal y almacenarlos en otro conjunto
with open('content/temp_file', 'r') as f:
    bot_names = set(f.read().splitlines())

# Encontrar los elementos que están en bot_names pero no en whitelist
unknown_bots = bot_names - whitelist

# Escribir los resultados en un archivo de salida llamado output_file
with open('content/output_file', 'w') as f:
    f.write('\n'.join(sorted(unknown_bots)))

# Eliminar el archivo temporal

os.remove('content/temp_file')
