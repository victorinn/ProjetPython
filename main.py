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
import ctypes
from dash.dependencies import Input, Output

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


year = 2002
gapminder = px.data.gapminder() # (1)
years = gapminder["year"].unique()
data = { year:gapminder.query("year == @year") for year in years} # (2)

#
# Main
#

if __name__ == '__main__':

    app = dash.Dash(__name__) # (3)

    fig = px.scatter(data[year], x="gdpPercap", y="lifeExp",
                        color="continent",
                        size="pop",
                        hover_name="country") # (4)

    app.layout = html.Div(children=[

                            html.H1(id="titre", children=f'Pourcentage d\'installation fibre par département en 2022',
                                        style={'textAlign': 'center', 'color': '#7FDBFF'}), # (5)

                            dcc.Dropdown(options=listDep, value=listDep[0], id='dropdown-departement'),

                            dcc.Graph(
                                id='graph1',
                                figure=fig
                            ), # (6)

                            html.H1(children=f'Carte d\'installation fibre en France par département en 2022',
                                        style={'textAlign': 'center', 'color': '#7FDBFF'}), # (5)

                            html.Div(children=[
                                html.Iframe(id='mapDepartementale', srcDoc=open('myMapDepartementale.html', 'r').read())
                            ], style={'width': '100%', 'height': '50vh', 'margin': "0px", "display": "block"}),          
    ]
    )

    @app.callback(Output('titre', 'value'), Input('dropdown-departement', 'value'),)
    def changeGraph(value):
        ctypes.cast("titre", ctypes.py_object).value = 'Bye Bye World!'
        return value

    #
    # RUN APP
    #

    app.run_server(debug=False) # (8)





   