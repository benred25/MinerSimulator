import pandas as pd
import plotly.express as px
from Miner import Model, CreateDatabases, MarketView

"""
    This class with contain controller methods
    Will activate and function when a user interacts with the system
    These changes will affect the model
"""


def handle_click():
    """ this will be called when a user clicks"""


def handle_buy(stock):
    """
        this will handle the buying of a stock
        change the users portfolio
    """


def handle_sell(stock):
    """
        this will handle the selling of a stock
        change the users portfolio
    """


def create_graph(stock):
    """
    Uses the data from CSVdata to create a table using plotly
    :param stock: stock that you want a graph for
    :return:
    """
    df = pd.read_csv("CSVdata/" + stock + ".csv")

    fig = px.line(df, x='Date', y=stock + '.Open', title='Shares')
    fig.show()

def run_sim():
    """
    Uses the data from CSVdata to create drop down menu and create the corresponding graphs
    :return:
    """
    MarketView.app.run_server()




def get_user_data():
    Model.select_all_tasks_from_USERS(CreateDatabases.create_connection('MinerDB'))


def get_stock_data():
    Model.select_all_tasks_from_STOCK_ID(CreateDatabases.create_connection('MinerDB'))

