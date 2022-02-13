import pandas as pd
from dash.dependencies import Input, Output
from dash import Dash, dash_table
import dash_bootstrap_components as dbc

#read in data file
df = pd.read_csv('goldcopyhalfstats.csv')

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Label('Click a cell in the table:'),
    dash_table.DataTable(df.to_dict('records'),[{"name": i, "id": i} for i in df.columns], id='tbl'),
    dbc.Alert(id='tbl_out'),
])

@app.callback(
    Output('tbl_out', 'children'), Input('tbl', 'active_cell')
)

def update_graphs(active_cell):
    return str(active_cell) if active_cell else "Click the table"

if __name__ == "__main__":
    app.run_server(debug=True)