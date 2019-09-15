import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'Peace Agreements 1990-2016'
myheading1 = "Peace Agreements 1990-2016"
myheading2 = 'The number of agreements are decreasing'
image1 = 'Agreements_byYear.png'
image2 = 'Agreements_byRegionState.png'
textbody = "There are about 1500 Peace Agreements from 1990 to 2016."
sourceurl = 'https://www.kaggle.com/university-of-edinburgh/peace-agreements-dataset'
githublink = 'https://github.com/ayk-oishi/dash-dc-layout'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H2(myheading1),
    html.H3(myheading2),
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url(image1), style={'width': '50%', 'height': 'auto'})
        ],className='three columns'),
        html.Div([
            html.Img(src=app.get_asset_url(image2), style={'width': '80%', 'height': 'auto'}),
        ],className='three columns'),
        html.Div([
            html.Div(textbody, style={
                'padding': '22px',
                'font-size': '22px',
                'height': '120px',
                'border': 'thin red solid',
                'color': 'rgb(155, 255, 355)',
                'backgroundColor': 'rgb(57, 83, 107)',
                'textAlign': 'left',
                }),
        ],className='six columns'),
    ],className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
