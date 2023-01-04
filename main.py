# filename = 'main.py'

#
# Imports
#

import plotly_express as px
import dash
from dash import dcc
from dash import html
import pandas as pd
import geopandas as gpd
from dash.dependencies import Input, Output
import dash_daq as daq
import carte

#
# Data
#

#Récupération des noms de département pour la liste déroulante
franceDep = gpd.read_file('datagouv-departements.geojson')
print(franceDep["nom"].head())

listDep = []
listDep.append(franceDep["nom"][0])

for depData in franceDep["nom"]:
    if not pd.isna(depData):
        if depData not in listDep:
            listDep.append(depData)

listDep.sort()



data = carte.myDataFrame


#
# Main
#

if __name__ == '__main__':

    app = dash.Dash(__name__) # (3)
    dataDep = data[data['code_dep'] == '65']
    # print(dataDep)
    fig = px.bar(dataDep, x= 'Commune', y='FibreByCommune')


    # fig = px.scatter(data, x="FibreByCommune", y="FibreByCommune",
    #                     color= "code_dep",
    #                     size="FibreByCommune",
    #                     hover_name="FibreByCommune") # (4)

    app.layout = html.Div(children=[

                            html.H1(id="titre", children=f'Pourcentage d\'installation fibre par département en 2022',
                                        style={'textAlign': 'center', 'color': '#7FDBFF'}), # (5)

                            dcc.Dropdown(listDep, listDep[0], id='dropdown-departement', #onChange=changeGraph()),
                            ),

                            dcc.Graph(
                                id='graph1',
                                figure=fig
                            ), # (6)

                            html.H1(id= 'titreMap', children=f'Carte d\'installation fibre en France par département en 2022',
                                        style={'textAlign': 'center', 'color': '#7FDBFF'}), # (5)

                            daq.ToggleSwitch(id="switch-map", value=True),

                            html.Div(children=[
                                html.Iframe(id='mapDepartementale', srcDoc=open('myMapDepartementale.html', 'r').read(),
                                style={'width': '100%', 'height': '50vh', 'margin': "0px", "display": "block"})
                            ]),
    ]
    )

 #Modification du graphe selon le département sélectionné
    @app.callback(Output('titre', 'children'), Input('dropdown-departement', 'value'),)
    def changeGraph(value):

        return f'Pourcentage d\'installation fibre en '+ value +' en 2022'
    
    #Modification du titre de la carte affichée
    @app.callback(Output('titreMap', 'children'), Input('switch-map', 'value'))
    def on_tick(value):
        if value == False:
            return f'Carte d\'installation fibre en France par commune en 2022'
        elif value == True:
            return f'Carte d\'installation fibre en France par département en 2022'
    
    #Modification de la carte selon le mode d'affichage sélectionné
    @app.callback(Output('mapDepartementale', 'srcDoc'), Input('switch-map', 'value'))
    def on_tick(value):
        if value == False:
            return open('myMapCommunale.html', 'r').read()
        elif value == True:
            return open('myMapDepartementale.html', 'r').read()

    
    #
    # RUN APP
    #

    app.run_server(debug=False) # (8)