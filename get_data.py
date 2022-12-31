import requests
from zipfile import ZipFile

#récupération du fichier geoJson
def recupererGeojsonFile(URL,name):
    # On télécharge le fichier surlequel pointe l'URL
    response = requests.get(URL)
    # On sauve réponse dans un nouveau fichier appelé stackoverflow.ico
    open(name, "wb").write(response.content)


#on récupere le fichier des communes 
URL = "https://perso.esiee.fr/~courivad/python_advanced/_downloads/8578d763bdb7d7d0d1a7aaeb2e3b4814/datagouv-communes.geojson"
recupererGeojsonFile(URL,"datagouv-communes.geojson")
#on récupere le fichier des départements
URL = "https://france-geojson.gregoiredavid.fr/repo/departements.geojson"
recupererGeojsonFile(URL,"datagouv-departements.geojson")

# Récupération du fichier csv
file = "tableau-de-bord-mci-commune-techno.zip"
#ouvrir le fichier zip en mode lecture
with ZipFile(file,'r') as zip:
        zip.printdir()
        #extraire les fichiers
        zip.extractall()