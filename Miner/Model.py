import sqlite3
import pandas as pd
import random
from Miner import Messages as M

day_holder = 0
month_holder = 0
year_holder = 0

def reset_portfolio():
    '''
    This method resets any transactions that are done by the user.
    This method is used when a new simulation is started or the user wishes to reset the simulation.
    :return:
    '''
    #empty data for each column is input
    data = {'Transaction Index':[], 'Stock Symbol':[], 'Buy in price':[], 'Number of Stocks':[], 'Stock':[], '% of stock Portfolio':[], 'Initial Capital':[], 'Current Capital':[], 'Profit':[], 'Profit %':[]}
    df = pd.DataFrame(data)
    #the line below writes it to the transactions excel file
    df.to_csv("CSVdata/User1Transactions.csv", index=False)
    return


def reset_timeline():
    '''
    This method resets the timeline and starts from day 0 again.
    This method is used when a new simulation is started or the user wishes to reset the simulation.
    :return:
    '''
    #this inputs initial day 0 values so that the graph has starting data points.
    data = {'Date':['03/01/2000'], 'AAPL':[3.745536], 'AMZN':['81.5'], 'DOW':['11501.84961'], 'G':['14'], 'INTC':['41.632813'], 'INTU':['29.804688'], 'NVDA':['3.9375'], 'RS':['11.71875'], 'SAM':['6000'], 'SNP500':['1469.25']}
    df = pd.DataFrame(data)
    #this writes these data values to the timelin excel file
    df.to_csv("CSVdata/User1Timeline.csv", index=False)
    return


def calc_brokerfees(transactionValue):
    """
    This method calculated broker fees of a transaction
    :param transactionValue: total value of a transaction
    :return: 1-2% broker fees calculated from transaction value
    """
    brokerFees = round(transactionValue * (random.uniform(1, 2)/100), 2)
    return brokerFees


def calc_overall_profit(filename):
    """
    This method calculates and writes overall profit to file using initial and current capital.
    :param filename: STRING, path to the csv file.
    :return:
    """
    try:
        df = pd.read_csv(f'{filename}', engine='python')            # "CSVdata/User1Transactions.csv"
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')
    profit = get_current_capital(filename) - get_initial_capital(filename) #standard formula for calculating overall profit
    df.at[0, 'Profit'] = profit #write it to the "Profit" column of the transactions excel file
    df.to_csv(f'{filename}', index=False)     # "CSVdata/User1Transactions.csv"
    return


def calc_overall_profit_num(filename):
    """
    This method calculates overall profit using initial and current capital.
    :param filename: STRING, path to the csv file.
    :return: float value of the overall profit
    """
    profit = get_current_capital(filename) - get_initial_capital(filename) #standard formula for calculating profit
    return profit


def calc_overall_profit_percentage(filename):
    """
    This method calculates the overall profit as a percentage and writes it to file
    :param filename: STRING, path to the csv file.
    :return:
    """
    try:
        df = pd.read_csv(f'{filename}', engine='python')  # "CSVdata/User1Transactions.csv"
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')
    profit = calc_overall_profit_num(filename) #reads current profit value
    percentProfit = (profit/get_initial_capital(filename))*100 #uses a standard formula for calculating profit percentage
    df.at[0, 'Profit %'] = percentProfit #writes the percentage profit to the file
    df.to_csv(f'{filename}', index=False)                       # "CSVdata/User1Transactions.csv"
    return


def set_initial_capital(initialCapital, filename):
    """
    This method sets the initial capital to file
    :param filename: STRING, path to the csv file.
    :param initialCapital: capital value to set to file
    :return:
    """
    try:
        df = pd.read_csv(f'{filename}', engine='python')  # "CSVdata/User1Transactions.csv"
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')
    df.at[0, 'Initial Capital'] = initialCapital
    df.to_csv(f'{filename}', index=False)     # "CSVdata/User1Transactions.csv"
    return


def get_initial_capital(filename):
    """
    This method returns initial capital set in the file
    :param filename: STRING, path to the csv file.
    :return: initial capital
    """
    try:
        df = pd.read_csv(f'{filename}', engine='python')
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')
    return df.at[0, 'Initial Capital']


def set_current_capital(currentCapital, filename):
    """
    This method sets the current capital to file
    :param filename: STRING, path to the csv file.
    :param currentCapital: capital value to set to file
    :return:
    """
    try:
        df = pd.read_csv(f'{filename}', engine='python')  # "CSVdata/User1Transactions.csv"
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')
    df.at[0, 'Current Capital'] = currentCapital
    df.to_csv(f'{filename}', index=False)                     # "CSVdata/User1Transactions.csv"
    return


def get_current_capital(filename):
    """
    This method returns current capital set in the
    :param filename: STRING, path to the csv file.
    :return: current capital
    """
    try:
        df = pd.read_csv(f'{filename}', engine='python')  # "CSVdata/User1Transactions.csv"
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')
    return df.at[0, 'Current Capital']


def calculate_total_stocks_owned(filename):
    """
    This method calculates the total number of stocks owned
    :param filename: STRING, path to the csv file.
    :return: total number of stocks owned
    """
    try:
        df = pd.read_csv(f'{filename}', engine='python')  # "CSVdata/User1Transactions.csv"
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')
    totalStockNum = df['Number of Stocks'].sum() #this goes through the entire column of "Number of Stocks" in the transactions file and adds them up
    return totalStockNum


def calc_num_of_company_stock(companySymbol, filename):
    """
    This method calculates the number of stocks owned of a paticular company
    :param filename: STRING, path to the csv file.
    :param companySymbol: symbol of the company for which number of stocks owned needs to be calculated
    :return: number of stocks owned for a given company
    """
    try:
        df = pd.read_csv(f'{filename}', engine='python')  # "CSVdata/User1Transactions.csv"
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')
    company_stocks_owned = df.loc[df['Stock Symbol'] == companySymbol, 'Number of Stocks'].sum() #this adds up all stocks owned for a particular company
    return company_stocks_owned


def calc_num_of_transaction_stock(transactionIndex, filename):
    """
        This method calculates the number of stocks owned in a particular transaction
        :param filename: STRING, path to the csv file.
        :param transactionIndex: transaction for which number of stocks owned are calculated
        :return: number of stocks owned in a given transaction
        """
    try:
        df = pd.read_csv(f'{filename}', engine='python')  # "CSVdata/User1Transactions.csv"
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')
    try:
        numStocks = df.loc[df['Transaction Index'] == transactionIndex, 'Number of Stocks'] #this give number of stocks owned in a particular transaction
        return numStocks.values[0]
    except:
        M.showdialog("You entered an invalid transaction index.")
        return -1


def calc_percent_of_portfolio(filename):
    """
    This method writes to file the breakdown of the portfolio in terms of percentage.
    Each stock has percentage corresponding to the total number of stocks owned.
    This is mainly to use for the portfolio pie chart.

    :param filename: STRING, path to the csv file.
    :return:
    """
    try:
        df = pd.read_csv(f'{filename}', engine='python')  # "CSVdata/User1Transactions.csv"
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')

    totalOwned = calculate_total_stocks_owned(filename) #used to negate a divide by zero error, by checking if zero stocks are owned
    companiesInPortfolio = df['Stock Symbol'].unique() #to calculate the number of unique companies in the portfolio of transactions
    counter = 0
    companiesInPortfolio = [companies for companies in companiesInPortfolio if str(companies) != 'nan'] #cancel out empty companies

    #these if statements take into account total stocks being zero
    if totalOwned != 0:
        for i in companiesInPortfolio:
            companyStocksOwned = calc_num_of_company_stock(i, filename)
            percentage = (companyStocksOwned / totalOwned) * 100 #percentage of that particular stock in the portfolio
            df.loc[counter, 'Stock'] = i
            df.at[counter, '% of stock Portfolio'] = percentage #writes the value into the dataframe
            counter = counter + 1
    if totalOwned == 0:
        for i in companiesInPortfolio:
            df.loc[counter, 'Stock'] = i
            df.at[counter, '% of stock Portfolio'] = 0.0 #percentage is zero when zero stocks are owned
            counter = counter + 1

    df.to_csv(f'{filename}', index=False)         # "CSVdata/User1Transactions.csv"
    return


def get_current_stock_price(companySymbol, filename):
    """
    This method returns the latest price of the stock given the company
    :param filename: STRING, path to the csv file.
    :param companySymbol: company for which you want the latest stock price
    :return: latest stock price of the company
    """
    try:
        df = pd.read_csv(f'{filename}', engine='python')  # "CSVdata/User1Timeline.csv"
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')
    currentStockPrice = df[companySymbol].iloc[-1] #checks last value for the particular stock in the timeline file for current stock price
    return currentStockPrice


def get_transaction_value(companySymbol, numberofStocks, filename):
    """
    This method calculates the transaction value using the number of stocks and the current price of stock
    :param filename: STRING, path to the csv file.
    :param companySymbol: company for which you need the current price of stock
    :param numberofStocks: number of stock you wish to buy
    :return: price value of the transaction
    """
    #standard formula to calculate value of the transaction.
    #current stock price multiplied by number of stocks
    transactionValue = get_current_stock_price(companySymbol, filename)*numberofStocks
    return transactionValue


def transaction_out_price(companySymbol, numberofStocks, filename):
    """
    This method calculates the price value of the transaction when selling
    :param filename: STRING, path to the csv file.
    :param companySymbol: company of the stock you are selling
    :param numberofStocks: number of stocks you are selling
    :return: the price value of the selling transaction
    """
    #transaction value calculated to be used to calculate brokerfees and substract from transaction payout to the user
    transactionValue = get_transaction_value(companySymbol, numberofStocks, filename)
    transactionOut = transactionValue - calc_brokerfees(transactionValue)
    return transactionOut


def transaction_in_price(buyInPrice, numberofStocks):
    """
    This method calculated the price of the transaction when buying
    :param buyInPrice: buy in price of the stock
    :param numberofStocks: number of stocks to buy
    :return: the price value of the buying transaction
    """
    #transaction buyin price for the user. Transaction value is added with the broker fees.
    transactionIn = (buyInPrice*numberofStocks) + calc_brokerfees(buyInPrice*numberofStocks)
    return transactionIn


def set_number_of_stocks(transactionIndex, numofStocks, filename):
    """
    This method sets the number of stocks to file for a given transaction index.
    This can be used when the user is buying or selling stock, as to remove or add stock to a particular transaction.
    :param transactionIndex: index of transaction for which you want to edit number of stocks
    :param numofStocks: number of stocks you wish to set
    :param filename: STRING, path to the csv file.
    :return:
    """
    try:
        df = pd.read_csv(f'{filename}', engine='python')  # "CSVdata/User1Transactions.csv"
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')
    #sets the number of stocks for that particular transaction index and writes it to file
    df.loc[df['Transaction Index'] == transactionIndex, 'Number of Stocks'] = numofStocks
    df.to_csv(f'{filename}', index=False)                         # "CSVdata/User1Transactions.csv"
    return


def get_number_of_stocks(transactionIndex, filename):
    """
    This method returns the number of stocks on file for a given transaction index
    :param transactionIndex: index of transaction
    :param filename: STRING, path to the csv file.
    :return: number of stocks in a particular transaction index
    """
    try:
        df = pd.read_csv(f'{filename}', engine='python')  # "CSVdata/User1Transactions.csv"
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')
    #gets the number of stocks owned for that particular transaction index
    numberofStocks = df.loc[df['Transaction Index'] == transactionIndex, 'Number of Stocks']
    return numberofStocks.values[0]


def add_stock (companySymbol, buyInPrice, numberofStocks, filename):
    """
    This method adds stock to the portfolio.
    :param companySymbol: company for the stock which you wish to add
    :param buyInPrice: buy in price of the stock
    :param numberofStocks: number of stocks you wish to buy
    :param filename: STRING, path to the csv file.
    :return:
    """
    try:
        df = pd.read_csv(f'{filename}', engine='python')  # "CSVdata/User1Transactions.csv"
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')
    counter = df['Transaction Index'].last_valid_index() #to see which index to add the transaction values to.
    if counter == None:
        #adds company symbol, buyinprice (aka the current stock price) and number of stocks to buy for transaction 0
        counter = 0
        df.at[0, 'Transaction Index'] = counter
        df.loc[df['Transaction Index'] == counter, 'Stock Symbol'] = companySymbol
        df.loc[df['Transaction Index'] == counter, 'Buy in price'] = buyInPrice
        df.loc[df['Transaction Index'] == counter, 'Number of Stocks'] = numberofStocks
        df.to_csv(f'{filename}', index=False)         # "CSVdata/User1Transactions.csv"
    else:
        # adds company symbol, buyinprice (aka the current stock price) and number of stocks to buy for last transaction number + 1
        counter = counter + 1
        df.at[counter, 'Transaction Index'] = counter
        df.loc[df['Transaction Index'] == counter, 'Stock Symbol'] = companySymbol
        df.loc[df['Transaction Index'] == counter, 'Buy in price'] = buyInPrice
        df.loc[df['Transaction Index'] == counter, 'Number of Stocks'] = numberofStocks
        df.to_csv(f'{filename}', index=False)                   # "CSVdata/User1Transactions.csv"
    return


def buy_stock(companySymbol, buyInPrice, numberofStocks, filename):
    """
    This method performs all the functions necessary to buy stock.
    It also calculates overall profit and updates the percentages in the portfolio.
    :param companySymbol: stock of the company you wish to buy
    :param buyInPrice: buy in price of the stock
    :param numberofStocks: number of stock you wish to buy
    :param filename: STRING, path to the csv file.
    :return:
    """
    #error checking for invalid values that may mess with the functions
    if numberofStocks == 0:
        M.showdialog("You can't buy zero stocks.")
        return
    if numberofStocks < 0:
        M.showdialog("You can't buy negative stocks.")
        return
    if get_current_capital(filename) < buyInPrice * numberofStocks:
        M.showdialog("You do not have enough money to complete the transaction")
        return
    #sets current capital to what is left after the buying fees for the transaction
    set_current_capital(get_current_capital(filename) - transaction_in_price(buyInPrice, numberofStocks), filename)
    #adds the stock to the transactions
    add_stock(companySymbol, buyInPrice, numberofStocks, filename)
    #calculates the breakdown of the portfolio percentages after this transaction
    calc_percent_of_portfolio(filename)
    #calculated the overall profit after this transaction
    calc_overall_profit(filename)
    #calculated the overall profit percentage after this transaction
    calc_overall_profit_percentage(filename)
    return


def sell_stock(transactionIndex, numberofStocks, filename):
    """
    This method performs all the functions necessary to sell stock.
    It also calculates overall profit and updates the percentages in the portfolio.
    :param transactionIndex: index of the transaction from which you wish to sell
    :param numberofStocks: number of stocks you wish to sell
    :param filename: STRING, path to the csv file.
    :return:
    """
    #error checking for invalid values that may mess with the functions
    if calc_num_of_transaction_stock(transactionIndex, filename) == -1:
        return
    if numberofStocks < 0:
        M.showdialog("You can't sell negative stocks.")
        return
    if numberofStocks == 0:
        M.showdialog("You can't sell zero stocks.")
        return
    if calc_num_of_transaction_stock(transactionIndex, filename) == 0:
        M.showdialog("You have sold all stock in this transaction. No stock left to sell.")
        return
        # raise Exception("You have sold all stock in this transaction. No stock left to sell.")
    if (calc_num_of_transaction_stock(transactionIndex, filename)-numberofStocks) < 0:
        M.showdialog("You are trying to sell more stocks than you own for this transaction. Choose a lower number of stock to sell.")
        return
        # raise Exception("You are trying to sell more stocks than you own for this transaction. Choose a lower number of stock to sell.")
    try:
        df = pd.read_csv(f'{filename}', engine='python')  # "CSVdata/User1Transactions.csv"
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')
    companySymbol = df.loc[df['Transaction Index'] == transactionIndex, 'Stock Symbol']
    companySymbol = companySymbol.values[0]

    #profit of the transaction after fees
    transactionProfit = transaction_out_price(companySymbol, numberofStocks, "CSVdata/User1Timeline.csv")
    #takes the profit and adds it to current capital so that user can make more trades with the money earned
    set_current_capital(transactionProfit+get_current_capital(filename), filename)
    #sets the number of stocks for the transaction after sale of the user input number of stocks
    set_number_of_stocks(transactionIndex, get_number_of_stocks(transactionIndex, filename)-numberofStocks, filename)
    #calculates overall profit after this transaction
    calc_overall_profit(filename)
    #calculated the overall profit percentage after this transaction
    calc_overall_profit_percentage(filename)
    #calculates the breakdown of the portfolio percentages after this transaction
    calc_percent_of_portfolio(filename)
    return


def increment_day(timefile, stockfile):
    '''
    This method adds stock data for the next day
    :param stockfile STRING, datapath to the csv file
    :param timefile STRING, datapath to the csv file
    :return:
    '''
    try:
        dd = pd.read_csv(f'{timefile}', engine='python')              # "CSVdata/User1Timeline.csv"
        ds = pd.read_csv(f'{stockfile}', engine='python', encoding='utf-8-sig')        # "CSVdata/StockData.csv"
    except FileNotFoundError as err:
        return err

    #if its the last day of operations in the stock data, it throw this message
    last_date = ds['Date'].iloc[-1]
    if last_date in dd.values:
        M.showdialog("You are done the simulation. Please sell all remaining stocks and check your final grade.")
        return

    #finds current date in timeline, and adds the stock values for the next business day.
    currentDate = dd["Date"].iloc[-1]
    dateFinder = ds.loc[ds['Date'] == currentDate].index[0]
    dateFinder = dateFinder + 1

    transfer = ds.iloc[dateFinder, :]

    dd = dd.append(pd.Series(transfer, index=dd.columns, name='Date'))
    dd.to_csv(f'{timefile}', index=False)         # "CSVdata/User1Timeline.csv"
    return


def increment_month(timefile, stockfile):
    '''
    This method adds stock data for the next month

    :param stockfile STRING, datapath to the csv file
    :param timefile STRING, datapath to the csv file
    :return:
    '''
    try:
        dd = pd.read_csv(f'{timefile}', engine='python')              # "CSVdata/User1Timeline.csv"
        ds = pd.read_csv(f'{stockfile}', engine='python', encoding='utf-8-sig')        # "CSVdata/StockData.csv"
    except FileNotFoundError as err:
        return err

    last_date = ds['Date'].iloc[-1]


    #finds current date in timeline, and adds the stock values for the next business month.
    for x in range(21): #business days in a month
        # if its the last day of operations in the stock data, it throw this message
        if last_date in dd.values:
            M.showdialog("You are done the simulation. Please sell all remaining stocks and check your final grade.")
            return
        currentDate = dd["Date"].iloc[-1]
        dateFinder = ds.loc[ds['Date'] == currentDate].index[0]
        dateFinder = dateFinder + 1

        transfer = ds.iloc[dateFinder, :]

        dd = dd.append(pd.Series(transfer, index=dd.columns, name='Date'))
        dd.to_csv(f'{timefile}', index=False)                     # "CSVdata/User1Timeline.csv"
    return


def increment_year(timefile, stockfile):
    '''
    This method adds stock data for the next year
    :return:
    '''
    try:
        dd = pd.read_csv(f'{timefile}', engine='python')              # "CSVdata/User1Timeline.csv"
        ds = pd.read_csv(f'{stockfile}', engine='python', encoding='utf-8-sig')        # "CSVdata/StockData.csv"
    except FileNotFoundError as err:
        return err

    last_date = ds['Date'].iloc[-1]

    #finds current date in timeline, and adds the stock values for the next business month.
    for x in range(261): #business days in a year
        # if its the last day of operations in the stock data, it throw this message
        if last_date in dd.values:
            M.showdialog("You are done the simulation. Please sell all remaining stocks and check your final grade.")
            return
        currentDate = dd["Date"].iloc[-1]
        dateFinder = ds.loc[ds['Date'] == currentDate].index[0]
        dateFinder = dateFinder + 1

        transfer = ds.iloc[dateFinder, :]

        dd = dd.append(pd.Series(transfer, index=dd.columns, name='Date'))
        dd.to_csv(f'{timefile}', index=False)                     # "CSVdata/User1Timeline.csv"
    return


def grade_performance(stockfile):
    """

    :param timefile STRING, datapath to the csv file
    :return:
    """
    try:
        df = pd.read_csv(f'{stockfile}', engine='python')          # "CSVdata/User1Transactions.csv"
    except FileNotFoundError as err:
        return err


    #grades performance of user using profit percentage
    profitPercentage = df.at[0, 'Profit %']
    grade = ''

    if profitPercentage < 0:
        grade = 'F'
    if 0 <= profitPercentage < 0.7:
        grade = 'D'
    if 0.7 <= profitPercentage < 1.8:
        grade = 'C'
    if 1.8 <= profitPercentage < 2.2:
        grade = 'C+'
    if 2.2 <= profitPercentage < 4.5:
        grade = 'B-'
    if 4.5 <= profitPercentage < 7:
        grade = 'B'
    if 7 <= profitPercentage < 12:
        grade = 'B+'
    if 12 <= profitPercentage < 18:
        grade = 'A-'
    if 18 <= profitPercentage < 25:
        grade = 'A'
    if profitPercentage >= 25:
        grade = 'A+'
    if profitPercentage >= 35:
        grade = 'A++'
    return grade


def add_capital(moneyToAdd, filename):
    try:
        df = pd.read_csv(f'{filename}', engine='python')  # "CSVdata/User1Transactions.csv"
    except FileNotFoundError:
        raise FileNotFoundError('There is no file')

    moneyToAdd = int(moneyToAdd)
    # error checking for invalid values

    if moneyToAdd < 0:
        M.showdialog("You can't add negative money. Please enter a positive number.")
        return
    if moneyToAdd == 0:
        M.showdialog("You can't add zero money. Please enter a positive number.")
        return

    #adds money to current capital and initial capital
    df.at[0, 'Initial Capital'] = get_initial_capital(filename) + moneyToAdd
    df.at[0, 'Current Capital'] = get_current_capital(filename) + moneyToAdd

    #calculated the overall profit after addition of money
    calc_overall_profit(filename)
    #calculated the overall profit percentage after addition of money
    calc_overall_profit_percentage(filename)

    df.to_csv(f'{filename}', index=False)     # "CSVdata/User1Transactions.csv"
    M.money_added()
    return


if __name__ == '__main__':
    print("Hello World")