import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'Peace Agreements 1990-2016'
myheading1 = "Peace Agreements 1990-2016"
myheading2 = 'There are about 1500 Peace Agreements from 1990 to 2016. The number of agreements are decreasing. \nAs of 2018  "Pre" agreements, meaning the process is under negotiation is common in Asia and Europe. \nContrary, in Africa, "SubPar", which is partially agreed peace process is dominant.'
image1 = 'Agreements_byYear.png'
image2 = 'Agreements_byRegionState.png'
sourceurl = 'https://www.kaggle.com/university-of-edinburgh/peace-agreements-dataset'
githublink = 'https://github.com/ayk-oishi/peaceagreement'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H2(myheading1),
    html.H5(myheading2),
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url(image1), style={'width': '250%', 'height': 'auto'})
        ],className='three columns'),
        html.Div([
            html.Img(src=app.get_asset_url(image2), style={'width': '250%', 'height': 'auto'}),
        ],className='three columns'),
    ],className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl)
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
