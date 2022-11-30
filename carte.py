import pandas as pd
import numpy
import folium

#Préparation des données numeriques
pop_data = pd.read_csv('tableau-de-bord-mci-commune-techno.csv', sep=';',header=1,encoding='latin-1',dtype={
    "Code Insee": int,
    "Commune": "string",
    " Nombre de locaux ": int,
    "Fibre": float,
    "Câble": float,
    "DSL": float,
    "THD Radio": float,
    "4G Fixe": float,
    "HD Radio": numpy.date,
    "Satellite" : float,

    })
# La colonne code_insee contient le code INSEE des communes:
dpt_code = pop_data['code_insee']

# La création d’un masque booléen permet de construire le sous ensemble recherché:
mask = ( ( dpt_code.str.startswith('75')  )
        | ( dpt_code.str.startswith('77') )
        | ( dpt_code.str.startswith('78') )
        | ( dpt_code.str.startswith('91') )
        | ( dpt_code.str.startswith('92') )
        | ( dpt_code.str.startswith('93') )
        | ( dpt_code.str.startswith('94') )
        | ( dpt_code.str.startswith('95') ) )
#filtrage par ligne
pop_data = pop_data[mask]
# print(pop_data)
#creation de la carte
coords = (48.7190835,2.4609723)
map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=9)

folium.Choropleth(
    geo_data='idf.geojson',                              # geographical data
    name='choropleth',
    data=pop_data,                                  # numerical data
    columns=['code_insee', 'nbr'],                     # numerical data key/value pair
    key_on='feature.properties.code_commune',       # geographical property used to establish correspondance with numerical data
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Population'
).add_to(map)

map.save(outfile='map.html')