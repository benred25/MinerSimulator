import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
from Miner import PortfolioView
from dash.dependencies import Input, Output
import Miner.Model



def generate_market_view():

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] #styling buttons and fonts
    app = dash.Dash(__name__,  external_stylesheets=external_stylesheets)
    ds = pd.read_csv("CSVdata/User1Transactions.csv") #reading transactions file for data table

    app.layout = html.Div([

        html.Div([
            #Titles and subtitles

            html.H1(children='Market Simulation'),

            html.H2(children='''The following are stocks use real historical data from January 2000 to January 2020.'''),

            html.H3('''Select a Stock out of the drop box below'''),
        ], className="banner"),

        html.Div([
            # This creates a dropdown menu for selecting the stock for which you want to see the graph.
            dcc.Dropdown(
                id='stock_name',
                options=[
                        {'label': 'Apple Inc.', 'value': 'AAPL'},
                        {'label': 'Amazon.com Inc.', 'value': 'AMZN'},
                        {'label': 'Dow Jones Industrial Average.', 'value': 'DOW'},
                        {'label': 'Alphabet Inc.', 'value': 'G'},
                        {'label': 'Intel Corporation.', 'value': 'INTC'},
                        {'label': 'Intuit Inc.', 'value': 'INTU'},
                        {'label': 'NVIDIA Corporation.', 'value': 'NVDA'},
                        {'label': 'Reliance Steel & Aluminum Co.', 'value': 'RS'},
                        {'label': 'Samsung Electronics Co Ltd.', 'value': 'SAM'},
                        {'label': 'S&P 500 Index.', 'value': 'SNP500'}
                        ],
                        value='AAPL',
                        ),
                    ]),

        html.Div([
            # This creates the graph of the stock selected.
            dcc.Graph(id='stock_graph',)
        ]),

        html.Div([
            html.H4("These buttons will scrub through the data at the given rates."),
            # These buttons increment the graph for the duration clicked.
            html.Button('Day', id='day'),
            html.Button('Month', id='month'),
            html.Button('Year', id='year'),
            html.Label("|  Hitting the update button will refresh the table below.   |"),
            # This button updates the table of transactions.
            html.Button('Update', id='update'),

        ]),

        html.Div([
            # This creates a table of transactions conducted by the user.
            dash_table.DataTable(
                style_cell={'fontSize': 14, 'textAlign': 'center',},
                data=[{}],
                id='table',
                columns=[{"name": i, "id": i} for i in ds.columns[0:4]]
            )
        ]),
    ])

    # This updates the table of transactions when the button is clicked.
    @app.callback(Output('table', 'data'), [Input('update', 'n_clicks')])
    def update_table(n_clicks):
        ds = pd.read_csv("CSVdata/User1Transactions.csv")
        return ds.to_dict('records')

    # This updates the graph to one selected in the dropdown menu & increments the graph when the buttons are clicked.
    @app.callback(Output('stock_graph', 'figure'), [Input('stock_name', 'value'),
                                                    Input('day', 'n_clicks'),
                                                    Input('month', 'n_clicks'),
                                                    Input('year', 'n_clicks')])
    def update_graph(drop_value, day_value, month_value, year_value):

        valueselected = format(drop_value)
        traces = []

        timefile = "CSVdata/User1Timeline.csv"
        stockfile = "CSVdata/StockData.csv"

        # Implementing the updating of graph when increment buttons are clicked.
        if day_value == (Miner.Model.day_holder + 1):
            Miner.Model.increment_day(timefile, stockfile)
        if month_value == (Miner.Model.month_holder + 1):
            Miner.Model.increment_month(timefile, stockfile)
        if year_value == (Miner.Model.year_holder + 1):
            Miner.Model.increment_year(timefile, stockfile)

        #This is a work around I had to do because of plotly limitations with buttons
        #operating on the amount of clicks
        if day_value != None:
            Miner.Model.day_holder = day_value
        if month_value != None:
            Miner.Model.month_holder = month_value
        if year_value != None:
            Miner.Model.year_holder = year_value

        dd = pd.read_csv("CSVdata/User1Timeline.csv")

        # This returns the changes by the user to the graph.
        traces.append(dict(
            x=dd.index,
            y=dd[valueselected],
        ))

        #this returns the data points, title and axis labels for the graph
        return{
            'data': traces,
            'layout':dict(title = "Graph of " + drop_value + " stock",
                          xaxis = dict(title='Business Day(s)'),
                          yaxis = dict(title='Price per stock ($ USD)'))
        }

    app.run_server(debug=False, port=8051)

if __name__ == "__main__":
    generate_market_view()


