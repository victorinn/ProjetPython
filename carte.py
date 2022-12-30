import pandas as pd
import numpy
import folium
import re
import branca

#Préparation des données numeriques
pop_data = pd.read_csv('tableau-de-bord-mci-commune-techno.csv', sep=';',header=1,encoding='latin-1',dtype={
    "Code Insee": "string",
    "Commune": "string",
    "code_reg": "string",    
    "Fibre": "string",
    "Câble": "string",
    "DSL": "string",
    "THD Radio": "string",
    "4G Fixe": "string",
    "HD Radio": "string",
    "Satellite" : "string",
    "code_insee": "string",
    "nom_com": "string",
    "code_dep" : "string",
    
    "type" : "string",
    "date": "string"
    })
# -------------------------------------------------------------------------------------------------------------
#print(pop_data)
#MODIFIER LA COLLONE FIBRE
lFibre = []
pl = pop_data['Fibre']                              #Création d'une series
for index, value in pl.loc[:34956].items():
    stringCut = re.sub("\%","",value)               #On est obligé de stocker le string coupé dans une nouvelle variable car un string est immutable en python
    stringCut2 = re.sub(",",".",stringCut)
    lFibre.append(stringCut2)
# print(fibre)
floatFibre = []
for item in lFibre:
    if item == '-':
        floatFibre.append(-1)                       #Pour les zones non-renseignées , on met -1 
    else:
        fItem = round((float(item)/100),3)
        floatFibre.append(fItem)

fibreDF = pd.DataFrame(floatFibre)
fibreDF.columns = ['FibreByCommune']                #On renome la colonne pour plus de comprehension 

dfs = [pop_data,fibreDF]
myDataFrame = pd.concat(dfs,axis=1,ignore_index=False)      #DataFrame contenant la part de fibre de chaques communes de France dans le bon format
# print(myDataFrame)


# -------------------------------------------------------------------------------------------------------------
def carteCommuneChoroplethe():
    # La colonne code_insee contient le code INSEE des communes:
    dep_code = myDataFrame['code_dep']

    # La création d’un masque booléen permet de construire le sous ensemble recherché:
    mask = (  ( dep_code.str.startswith('0') )
            | ( dep_code.str.startswith('1') )
            | ( dep_code.str.startswith('2') )
            | ( dep_code.str.startswith('3') )
            | ( dep_code.str.startswith('4') )
            | ( dep_code.str.startswith('5') )
            | ( dep_code.str.startswith('6') )
            | ( dep_code.str.startswith('7') )
            | ( dep_code.str.startswith('8') )
            | ( dep_code.str.startswith('9') ))
    #filtrage par ligne
    pop_data = myDataFrame[mask]
    # print(pop_data)
    #creation de la carte
    coords = (48.7190835,2.4609723)
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=7)
    folium.Choropleth(
        geo_data='franceCommunes.geojson',                              # geographical data
        name='choropleth',
        data=pop_data,                                  # numerical data
        columns=['code_insee', 'FibreByCommune'],                     # numerical data key/value pair
        key_on='feature.properties.code_commune',       # geographical property used to establish correspondance with numerical data
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Pourcentage fibre'
    ).add_to(map)

    map.save(outfile='myMap.html')

def carteDepChoroplethe():
    # La colonne code_insee contient le code INSEE des communes:
    dep_code = myDataFrame['code_dep']

    # La création d’un masque booléen permet de construire le sous ensemble recherché:
    mask = (  ( dep_code.str.startswith('0') )
            | ( dep_code.str.startswith('1') )
            | ( dep_code.str.startswith('2') )
            | ( dep_code.str.startswith('3') )
            | ( dep_code.str.startswith('4') )
            | ( dep_code.str.startswith('5') )
            | ( dep_code.str.startswith('6') )
            | ( dep_code.str.startswith('7') )
            | ( dep_code.str.startswith('8') )
            | ( dep_code.str.startswith('9') ))
    #filtrage par ligne
    pop_data = myDataFrame[mask]
    # print(pop_data)
    #creation de la carte
    coords = (48.7190835,2.4609723)
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=7)
    folium.Choropleth(
        geo_data='franceDep.geojson',                              # geographical data
        name='choropleth',
        data=pop_data,                                  # numerical data
        columns=['code_dep', 'FibreByCommune'],                     # numerical data key/value pair
        key_on='feature.properties.code',       # geographical property used to establish correspondance with numerical data
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Pourcentage fibre'
    ).add_to(map)

    map.save(outfile='myMapDepartementale.html')

carteCommuneChoroplethe()
carteDepChoroplethe()          #Les deps se découpent en communes

  