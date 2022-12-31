import requests

URL = "https://perso.esiee.fr/~courivad/python_advanced/_downloads/8578d763bdb7d7d0d1a7aaeb2e3b4814/datagouv-communes.geojson"

# 2. On télécharge le fichier surlequel pointe l'URL
response = requests.get(URL)

# 3. On sauve réponse dans un nouveau fichier appelé stackoverflow.ico
open("datagouv-communes.geojson", "wb").write(response.content)