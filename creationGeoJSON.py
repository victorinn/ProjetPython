import geojson, geopandas, pandas

# lecture du fichier global
france = geopandas.read_file("datagouv-communes.geojson")
fr = geopandas.read_file("datagouv-departements.geojson")

def geoJsonCommunes(file):
    l = []
    # sélection des données de France à afficher
    for dpt in ["0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9"]:    #A changer plus tard par toute la france
        dptidf = file[file["code_commune"].str.startswith(dpt)]
        l.append(dptidf)

    # construction de la GeoDataFrame correspondante
    idf = pandas.concat(l)

    # écriture dans un fichier
    with open("franceCommunes.geojson", "w") as f:
        geojson.dump(idf, f)
def geoJsonDepartements(file):
    l = []
    # sélection des données de France à afficher
    for dpt in ["0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9"]:    #A changer plus tard par toute la france
        dptidf = file[file["code"].str.startswith(dpt)]
        l.append(dptidf)

    # construction de la GeoDataFrame correspondante
    idf = pandas.concat(l)

    # écriture dans un fichier
    with open("franceDep.geojson", "w") as f:
        geojson.dump(idf, f)
def geoJsonRegions(file):
    l = []
    # sélection des données de France à afficher
    for reg in ["0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "7",
                "8",
                "9"]:    #A changer plus tard par toute la france
        regions = file[file["code_insee_region"].str]
        l.append(regions)

    # construction de la GeoDataFrame correspondante
    idf = pandas.concat(l)

    # écriture dans un fichier
    with open("franceRegions.geojson", "w") as f:
        geojson.dump(idf, f)
 
geoJsonCommunes(france)   
geoJsonDepartements(fr)
# geoJsonRegions(france)
