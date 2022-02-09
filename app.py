import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv('goldcopyhalfstats.csv')

# you need to include __name__ in your Dash constructor if
# you plan to use a custom CSS or JavaScript in your Dash apps
app = dash.Dash(__name__)
#---------------------------------------------------------------
app.layout = html.Div([
    html.Div([
        html.Label(['Your Team Stats']),
        dcc.Dropdown(
            id='my_dropdown',
            options=[
                     {'label': 'B Team', 'value': 'b_team_name'},
                     {'label': 'A Team', 'value': 'a_team_name'}
            ],
            value='a_team_name',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
    ]),

    html.Div([
        dcc.Graph(id='the_graph')
    ]),

])

#---------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def update_graph(my_dropdown):
    dfg = df

    piechart=px.pie(
            data_frame=dfg,
            names=my_dropdown,
            hole=.3,
            )

    return (piechart)


if __name__ == '__main__':
    app.run_server(debug=True)