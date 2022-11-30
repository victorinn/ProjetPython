import geojson, geopandas, pandas

# lecture du fichier global
france = geopandas.read_file("datagouv-communes.geojson")

l = []
# sélection des données de France
for dpt in ["75", "77", "78", "91", "92", "93", "94", "95"]:    #A changer plus tard par toute la france
    dptidf = france[france["code_commune"].str.startswith(dpt)]
    l.append(dptidf)

# construction de la GeoDataFrame correspondante
idf = pandas.concat(l)

# écriture dans un fichier
with open("idf.geojson", "w") as f:
    geojson.dump(idf, f)