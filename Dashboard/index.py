#import dependencies
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import selectthree

#title page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.H1([
        dcc.Link(children = 'Compare Your Team!',
        style ={'textAlign' :'center','color':'#253ATC'}, href='/apps/selectthree'),
    ], className="row"),
    html.Div(id='page-content', children=[])
])

#callback for interactive links to other pages
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/selectthree':
        return selectthree.layout
    else:
        return "Select 'Compare Your Team' from the menu above."


if __name__ == '__main__':
    app.run_server(debug=False)