import pandas as pd
import plotly
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

##for interactivity
app = dash.Dash(__name__)

#read in data file
df = pd.read_csv("goldcopyhalfstats.csv")

#view data file
df.head()

app.layout = html.Div([

    html.Div([
        dcc.Graph(id='penaltygraph')
    ],className='two columns'),
    
    html.Div([
        dcc.Graph(id='offrushgraph')
    ],className='two columns'),
    
    html.Div([
        dcc.Graph(id='defrushgraph')
    ],className='two columns'),
    
    html.Div([
        dcc.Graph(id='offpassgraph')
    ],className='two columns'),
    
    html.Div([
        dcc.Graph(id='defpassgraph')
    ],className='two columns'),

    html.Div([

        html.Br(),
        html.Label(['Select Your Competitors'],style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Dropdown(id='team_one',
            options=[{'label':x, 'value':x} for x in df.sort_values('a_team_name')['a_team_name'].unique()],
            value='Air Force',
            multi=False,
            disabled=False,
            clearable=True,
            searchable=True,
            placeholder='Choose The Team...',
            className='form-dropdown',
            style={'width':"90%"},
            persistence='string',
            persistence_type='memory'),

        dcc.Dropdown(id='team_two',
            options=[{'label':x, 'value':x} for x in df.sort_values('a_team_name')['a_team_name'].unique()],
            value='Akron',
            multi=False,
            disabled=False,
            clearable=True,
            searchable=True,
            placeholder='Choose The Team...',
            className='form-dropdown',
            style={'width':"90%"},
            persistence='string',
            persistence_type='memory'),

        dcc.Dropdown(id='team_three',
            options=[{'label':x, 'value':x} for x in df.sort_values('a_team_name')['a_team_name'].unique()],
            value='Alabama',
            multi=False,
            disabled=False,
            clearable=True,
            searchable=True,
            placeholder='Choose The Team...',
            className='form-dropdown',
            style={'width':"90%"},
            persistence='string',
            persistence_type='memory'),
    ],className='three columns'),

])

@app.callback(
    Output('penaltygraph','figure'),
    [Input('team_one','value'),
     Input('team_two','value'),
     Input('team_three','value')]
)

def build_graph(first_team, second_team, third_team):
    dff=df[(df['a_team_name']==first_team)|
           (df['a_team_name']==second_team)|
           (df['a_team_name']==third_team)]
    # print(dff[:5])

    fig = px.scatter(dff, x="visit_date", y="a_penalty_yards", color='a_team_name', height=600)
    fig.update_layout(xaxis={'title':'Game Date'},
                      yaxis={'title': 'Penalty Yards'},
                      title={'text':'Penalty Yards at the Half',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig


@app.callback(
    Output('offrushgraph','figure'),
    [Input('team_one','value'),
     Input('team_two','value'),
     Input('team_three','value')]
)

def build_graph2(first_team, second_team, third_team):
    dff=df[(df['a_team_name']==first_team)|
           (df['a_team_name']==second_team)|
           (df['a_team_name']==third_team)]
    # print(dff[:5])

    fig = px.scatter(dff, x="visit_date", y="a_offense_rush_yards", color='a_team_name', height=600)
    fig.update_layout(xaxis={'title':'Game Date'},
                      yaxis={'title': 'Rush Yards'},
                      title={'text':'Offense Rush Yards at the Half',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig
@app.callback(
    Output('defrushgraph','figure'),
    [Input('team_one','value'),
     Input('team_two','value'),
     Input('team_three','value')]
)

def build_graph3(first_team, second_team, third_team):
    dff=df[(df['a_team_name']==first_team)|
           (df['a_team_name']==second_team)|
           (df['a_team_name']==third_team)]
    # print(dff[:5])

    fig = px.scatter(dff, x="visit_date", y="a_defense_rush_yards", color='a_team_name', height=600)
    fig.update_layout(xaxis={'title':'Game Date'},
                      yaxis={'title': 'Rush Yards'},
                      title={'text':'Defense Rush Yards at the Half',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig

@app.callback(
    Output('defpassgraph','figure'),
    [Input('team_one','value'),
     Input('team_two','value'),
     Input('team_three','value')]
)

def build_graph4(first_team, second_team, third_team):
    dff=df[(df['a_team_name']==first_team)|
           (df['a_team_name']==second_team)|
           (df['a_team_name']==third_team)]
    # print(dff[:5])

    fig = px.scatter(dff, x="visit_date", y="a_defense_pass_yards", color='a_team_name', height=600)
    fig.update_layout(xaxis={'title':'Game Date'},
                      yaxis={'title': 'Pass Yards'},
                      title={'text':'Defense Pass Yards at the Half',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig

@app.callback(
    Output('offpassgraph','figure'),
    [Input('team_one','value'),
     Input('team_two','value'),
     Input('team_three','value')]
)

def build_graph5(first_team, second_team, third_team):
    dff=df[(df['a_team_name']==first_team)|
           (df['a_team_name']==second_team)|
           (df['a_team_name']==third_team)]
    # print(dff[:5])

    fig = px.scatter(dff, x="visit_date", y="a_offense_pass_yards", color='a_team_name', height=600)
    fig.update_layout(xaxis={'title':'Game Date'},
                      yaxis={'title': 'Pass Yards'},
                      title={'text':'Offense Pass Yards at the Half',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig



if __name__ == '__main__':
    app.run_server(debug=False)