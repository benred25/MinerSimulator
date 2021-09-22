import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output


def generate_portfolio_view():

    ds = pd.read_csv("CSVdata/User1Transactions.csv") #reads user transactions for the data table
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] #styling of fonts used and buttons
    app = dash.Dash(__name__,  external_stylesheets=external_stylesheets)
    app.layout = html.Div([

        html.Div([
            #title labels
            html.H1(children='Your Portfolio'),
            html.H2('''This page will hold information about your current stock holdings.''')
        ]),

        html.Div([
            # this creates the pie chart of the stocks in the portfolio
            dcc.Graph(figure=px.pie(ds, values='% of stock Portfolio', names='Stock'),
                      id='pie'),
        ]),

        html.Div([
            # the two buttons which update the table of transactions and the pie chart
            html.H3("Press the Update Transactions button to refresh the table below and press the Update Portfolio "
                    "button to update the graph above."),
            html.Button('Update Transactions', id='update'),
            html.Button('Update Portfolio', id='piebutton'),
        ]),

        html.Div([
            # creates a table of transactions conducted by the user
            dash_table.DataTable(
                style_cell={'fontSize': 14, 'textAlign': 'center', },
                id='table',
                columns=[{"name": i, "id": i} for i in ds.columns[0:4]],
                data=ds.to_dict('records'),
            )
        ]),
    ])

    # This updates the porfolio percentages of total stocks owned when the button is clicked.
    @app.callback(Output('pie', 'figure'), [Input('piebutton', 'n_clicks')])
    def update_pie(n_clicks):
        dt = pd.read_csv("CSVdata/User1Transactions.csv")
        return px.pie(dt, values='% of stock Portfolio', names='Stock')

    # This updates the table of transactions when the button is clicked.
    @app.callback(Output('table', 'data'), [Input('update', 'n_clicks')])
    def update_table(n_clicks):
        ds = pd.read_csv("CSVdata/User1Transactions.csv")
        return ds.to_dict('records')

    app.run_server(debug=False, port=8052)


if __name__ == "__main__":
    generate_portfolio_view()
