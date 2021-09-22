import sqlite3
import pandas as pd


def create_database(databaseName):
    """
    Create the database if one does not exist.
    :return:
    """
    connect = sqlite3.connect(databaseName)
    c = connect.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS USERS
                    ([GenerateUserId] INTEGER PRIMARY KEY, [UserName] TEXT, [Email] TEXT, [Money] INTEGER, [StocksOwned] LIST)''')

    c.execute(''' CREATE TABLE IF NOT EXISTS STOCK_ID 
                    ([GenerateStockId] INTEGER PRIMARY KEY, [Symbol] TEXT, [Name] TEXT)''')

    c.execute(''' CREATE TABLE IF NOT EXISTS STOCK_PRICE
                    ([Symbol] TEXT PRIMARY KEY, [Date] DATE, [Open] FLOAT , [Close] FLOAT )''')

    c.execute(''' CREATE TABLE IF NOT EXISTS TRANSACTIONS
                    ([Symbol] TEXT PRIMARY KEY , [Price] FLOAT, [NumberStocks] INTEGER, [Name] TEXT)''')

    c.execute(''' CREATE TABLE IF NOT EXISTS PORTFOLIO
                     ([InitCapital] FLOAT, [CurrCapital] FLOAT, [Profit] FLOAT)''')

    connect.commit()

    return connect

def create_connection(db):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db)
    except sqlite3.Error as e:
        print(e)

    return conn

def remove_data_table(tableName, dataBase):
    """
    Delete the table from the database

    :param tableName: STRING, Name of the table that will be drop.
    :param dataBase: STRING, Name of the database
    :return: None
    """
    c = dataBase.cursor()
    c.execute(f'''DROP TABLE {tableName}''')
    dataBase.commit()

def add_data_to_table(dataBase, table, fileName):
    """
    Insert the data values in a specific table in the database.

    :param dataBase: STRING, Name of the database.
    :param table: STRING, Name of the table that will be storing the value.
    :param fileName: STRING CSV FILE, path to the file.
    :return: None
    """
    readStockID = pd.read_csv(f'{fileName}')
    readStockID.to_sql(table, dataBase, if_exists='replace', index=False)

def select_all_tasks_from_table(dataBase, table):
    """
    Get the data values from a specific table in the database.

    :param dataBase: STRING, Name of the database.
    :param table: STRING, Name of the table that will be getting all the data.
    :return: None
    """
    c = dataBase.cursor()
    c.execute(f'''SELECT * FROM {table}''')

    rows = c.fetchall()

    for row in rows:
        print(row)