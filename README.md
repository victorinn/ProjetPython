# User Guide 
Pour déployer ce projet, il vous faut : 
- Copier le projet avec la commande ``` git clone adresse_publique_de_votre_projet ```
- Télécharger les fichiers JSON nécéssaire. (car trop grand pour être incorporé dans GitHub)
- Exécuter la commande ``` python -m pip install -r requirements.txt ``` pour installer les packages additionnels requis.
- Exécuter la commande ``` python main.py ``` qui génèrera le dashboard. 
# Rapport
Le but de notre projet est de mettre en avant les installations Fibre des communes francaises. Selon le [ministere de l'économie des finances et de la souveraineté industrielle et numérique](https://www.economie.gouv.fr/cedef/date-deploiement-fibre-commune#:~:text=Les%20objectifs%20fix%C3%A9s%20par%20le,tous%20d'ici%20fin%202022.), l'objectif est que la haut débit disponible pour tous fin 2020 et le très haut débit, fin 2022.

La conclusion de cette étude est que l'objectif n'est pas atteint. Une partie de la France est entierement fibré mais la grande partie des communes françaises sont fibré à moins de 70%. 
En regardant communes par communes, on peut aussi s'apercevoir que la plus grande partie est fibré à moins de 30%. On est alors loin de l'objectif initial. 

# Developper guide
## Fichier utilisés : 
- [datagouv-communes.geojson](https://perso.esiee.fr/~courivad/python_advanced/_downloads/8578d763bdb7d7d0d1a7aaeb2e3b4814/datagouv-communes.geojson). Ce fichier était accessible directement depuis le cours à ce [lien](https://perso.esiee.fr/~courivad/python_advanced/chapters/02-geo.html).
* [datagouv-departements.geojson](https://france-geojson.gregoiredavid.fr/).
+ [tableau-de-bord-mci-commune-techno.csv](https://france-geojson.gregoiredavid.fr/).

## Structure :
Le projet est découpé en plusieurs fichiers python :
- creationGeoJSON.py : 
    - Ce fichier permet de créer les fichiers geojson en gardant les données qui nous interessent.
* carte.py :
    * Ce fichier permet de créer les 2 cartes traitant nos données. Pour créer cette carte il a fallu garder uniquement la colonne liée aux installations fibre et la colonne lié aux codes communes. 
        * Une carte choroplethe découpée en département est crée.
        * Une carte choroplethe découpée en commune est crée.
+ main.py :
    + Ce fichier sert à créer entierement le dashboard.

## Membres :
Membres de ce projet : 
- @github/victorinn
+ @github/ServianB
