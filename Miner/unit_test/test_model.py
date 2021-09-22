import unittest
import csv
import os
import pandas as pd

from Miner import Model
from Miner import CreateDatabases


# --------------------------------------------------------

class TestModel ( unittest.TestCase ):

    @classmethod
    def setUp(self):
        with open('UserTimelineSample.csv', 'w', newline='') as f:
            lineWrite = csv.writer(f)

            lineWrite.writerow(['Date', 'AAPL', 'AMZN', 'DOW', 'G', 'INTC', 'INTU', 'NVDA', 'RS', 'SAM', 'SNP500'])
            lineWrite.writerow(['03/01/2000', '3.745536', '81.5', '11501.84961', '14', '41.632813', '29.804688', '3.9375', '11.71875', '6000', '1469.25'])

        # Get the header of the real file to use as sample
        head = ['Transaction Index',
                'Stock Symbol',
                'Buy in price',
                'Number of Stocks',
                'Stock',
                '% of stock Portfolio',
                'Initial Capital',
                'Current Capital',
                'Profit',
                'Profit %']

        # Create an csv sample file for users
        with open('UserSample.csv', 'w', newline='') as f:
            lineWrite = csv.writer(f)
            lineWrite.writerow(head)

        self.filename = 'UserSample.csv'
        self.timeline = 'UserTimelineSample.csv'

    @classmethod
    def tearDown(self):
        # Delete csv sample files
        os.remove('UserSample.csv')
        os.remove('UserTimelineSample.csv')

    def test_get_current_capital(self):
        """ Test if it does get the current capital in the file """

        # Set the csv file for test
        df = pd.read_csv(f'{self.filename}', engine='python')
        df.at[0, 'Current Capital'] = 1500
        df.to_csv(f'{self.filename}', index=False)

        self.assertEqual(Model.get_current_capital(self.filename), 1500)
        self.assertNotEqual(Model.get_current_capital(self.filename), 1499)
        self.assertRaises(FileNotFoundError, Model.get_current_capital, 'notrealfile.csv')

    def test_get_initial_capital(self):
        """ Test if it does get the initial capital in the file """

        # Set the csv file for test
        df = pd.read_csv(f'{self.filename}', engine='python')
        df.at[0, 'Initial Capital'] = 1000
        df.to_csv(f'{self.filename}', index=False)

        self.assertEqual(Model.get_initial_capital(self.filename), 1000)
        self.assertNotEqual(Model.get_initial_capital(self.filename), 999)
        self.assertRaises(FileNotFoundError, Model.get_initial_capital, 'notrealfile.csv')

    def test_calc_overall_profit_num(self):
        """ Test if the calculation of the function is correct """

        # Set the csv file for test
        df = pd.read_csv(f'{self.filename}', engine='python')
        df.at[0, 'Current Capital'] = 1500
        df.at[0, 'Initial Capital'] = 1000
        df.to_csv(f'{self.filename}', index=False)

        # TEST 1
        self.assertEqual(Model.calc_overall_profit_num(self.filename), 500)
        self.assertNotEqual(Model.calc_overall_profit_num(self.filename), 2500)

        # Different test
        df.at[0, 'Current Capital'] = 500
        df.to_csv(f'{self.filename}', index=False)

        # TEST 2
        self.assertEqual(Model.calc_overall_profit_num(self.filename), -500)
        self.assertNotEqual(Model.calc_overall_profit_num(self.filename), 1500)

        self.assertRaises(FileNotFoundError, Model.calc_overall_profit, 'notrealfile.csv')

    def test_calculate_total_stocks_owened(self):
        """ Test if it returns all the stocks owned """

        # Set the csv file for test
        df = pd.read_csv(f'{self.filename}', engine='python')
        df.at[0, 'Number of Stocks'] = 5
        df.at[1, 'Number of Stocks'] = 6
        df.at[2, 'Number of Stocks'] = 7
        df.to_csv(f'{self.filename}', index=False)

        self.assertEqual(Model.calculate_total_stocks_owned(self.filename), 18)
        self.assertLess(Model.calculate_total_stocks_owned(self.filename), 19)
        self.assertGreater(Model.calculate_total_stocks_owned(self.filename), 17)
        self.assertRaises(FileNotFoundError, Model.calculate_total_stocks_owned, 'notrealfile.csv')

    def test_calc_num_of_company_stock(self):
        """ Test if it gets the given symbol of all stock owned """

        # Set the csv file for the test
        df = pd.read_csv(f'{self.filename}', engine='python')
        df.at[0, 'Stock Symbol'] = "AAPL"
        df.at[0, 'Number of Stocks'] = 5

        df.at[1, 'Stock Symbol'] = "AMZN"
        df.at[1, 'Number of Stocks'] = 3

        df.at[2, 'Stock Symbol'] = "AAPL"
        df.at[2, 'Number of Stocks'] = 2

        df.to_csv(f'{self.filename}', index=False)

        self.assertEqual(Model.calc_num_of_company_stock("AAPL", self.filename), 7)
        self.assertLess(Model.calc_num_of_company_stock("AAPL", self.filename), 8)
        self.assertGreater(Model.calc_num_of_company_stock("AAPL", self.filename), 6)

        self.assertEqual(Model.calc_num_of_company_stock("AMZN", self.filename), 3)
        self.assertLess(Model.calc_num_of_company_stock("AMZN", self.filename), 4)
        self.assertGreater(Model.calc_num_of_company_stock("AMZN", self.filename), 2)

        self.assertRaises(FileNotFoundError, Model.calculate_total_stocks_owned, 'notrealfile.csv')

    def test_calc_num_of_transaction_stock(self):
        """ Test if it returns number of stocks owned in a given index """

        # Set the csv file for the test
        df = pd.read_csv(f'{self.filename}', engine='python')
        df.at[0, 'Transaction Index'] = 0
        df.at[1, 'Transaction Index'] = 1
        df.at[2, 'Transaction Index'] = 2

        df.at[0, 'Number of Stocks'] = 11
        df.at[1, 'Number of Stocks'] = 24
        df.at[2, 'Number of Stocks'] = 37
        df.to_csv(f'{self.filename}', index=False)

        self.assertEqual(Model.calc_num_of_transaction_stock(0, self.filename), 11)
        self.assertLess(Model.calc_num_of_transaction_stock(0, self.filename), 24)
        self.assertGreater(Model.calc_num_of_transaction_stock(0, self.filename), 7)

        self.assertEqual(Model.calc_num_of_transaction_stock(1, self.filename), 24)
        self.assertLess(Model.calc_num_of_transaction_stock(1, self.filename), 37)
        self.assertGreater(Model.calc_num_of_transaction_stock(1, self.filename), 11)

        self.assertEqual(Model.calc_num_of_transaction_stock(2, self.filename), 37)
        self.assertLess(Model.calc_num_of_transaction_stock(2, self.filename), 71)
        self.assertGreater(Model.calc_num_of_transaction_stock(2, self.filename), 11)

        self.assertRaises(FileNotFoundError, Model.calculate_total_stocks_owned, 'notrealfile.csv')

    def test_calc_percent_of_portfolio(self):
        """ Test if it updates the percentage of the stock and place it correctly """

        # Set the csv file for the test
        df = pd.read_csv(f'{self.filename}', engine='python')
        df.at[0, 'Number of Stocks'] = 10
        df.at[1, 'Number of Stocks'] = 15
        df.at[2, 'Number of Stocks'] = 25
        df.at[3, 'Number of Stocks'] = 10

        df.at[0, 'Stock Symbol'] = "AAPL"
        df.at[1, 'Stock Symbol'] = "AMZN"
        df.at[2, 'Stock Symbol'] = "G"
        df.at[3, 'Stock Symbol'] = "AAPL"

        df.to_csv(f'{self.filename}', index=False)

        Model.calc_percent_of_portfolio(self.filename)

        df = pd.read_csv(f'{self.filename}', engine='python')
        sample1 = df.loc[df['Stock'] == "AAPL", '% of stock Portfolio']
        sample2 = df.loc[df['Stock'] == "AMZN", '% of stock Portfolio']
        sample3 = df.loc[df['Stock'] == "G", '% of stock Portfolio']

        self.assertEqual(sample1.values[0], 33.33333333333333)
        self.assertEqual(sample2.values[0], 25.0)
        self.assertEqual(sample3.values[0], 41.66666666666667)
        self.assertRaises(FileNotFoundError, Model.calc_percent_of_portfolio, 'notrealfile.csv')

    def test_get_current_stock_price(self):
        """ Test if it gets the latest stock price in the file """

        self.assertEqual(Model.get_current_stock_price('AMZN', self.timeline), 81.5)
        self.assertLess(Model.get_current_stock_price('AMZN', self.timeline), 11501.84961)
        self.assertGreater(Model.get_current_stock_price('AMZN', self.timeline), 3.745536)
        with self.assertRaises(FileNotFoundError):
            Model.get_current_stock_price('AMZN', 'notrealfile.csv')

    def test_get_transaction_value(self):
        """ Test if it returns the right price value of the transaction"""

        self.assertEqual(Model.get_transaction_value('AMZN', 5, self.timeline), 407.5)
        self.assertLess(Model.get_transaction_value('AMZN', 5, self.timeline), 7346.25)
        self.assertGreater(Model.get_transaction_value('AMZN', 5, self.timeline), 149.02344)

    def test_set_number_of_stocks(self):
        """ Test if it sets it properly """

        # Set the csv file for the test
        df = pd.read_csv(f'{self.filename}', engine='python')
        df.at[0, 'Transaction Index'] = 0
        df.at[1, 'Transaction Index'] = 1
        df.at[2, 'Transaction Index'] = 2
        df.at[3, 'Transaction Index'] = 3
        df.to_csv(f'{self.filename}', index=False)

        Model.set_number_of_stocks(0, 5, self.filename)
        Model.set_number_of_stocks(1, 10, self.filename)
        Model.set_number_of_stocks(2, 15, self.filename)
        Model.set_number_of_stocks(3, 20, self.filename)

        df = pd.read_csv(f'{self.filename}', engine='python')
        sample1 = df.loc[df['Transaction Index'] == 0, 'Number of Stocks']
        sample2 = df.loc[df['Transaction Index'] == 1, 'Number of Stocks']
        sample3 = df.loc[df['Transaction Index'] == 2, 'Number of Stocks']
        sample4 = df.loc[df['Transaction Index'] == 3, 'Number of Stocks']

        self.assertEqual(sample1.values[0], 5.0)
        self.assertEqual(sample2.values[0], 10.0)
        self.assertEqual(sample3.values[0], 15.0)
        self.assertEqual(sample4.values[0], 20.0)
        with self.assertRaises(FileNotFoundError):
            Model.set_number_of_stocks(0, 5, 'notrealfile.csv')

    def test_get_number_of_stocks(self):
        """ Test if it gets the right number of stocks """

        # Set the csv file for the test
        df = pd.read_csv(f'{self.filename}', engine='python')
        df.at[0, 'Transaction Index'] = 0
        df.at[1, 'Transaction Index'] = 1
        df.at[2, 'Transaction Index'] = 2
        df.at[3, 'Transaction Index'] = 3
        df.to_csv(f'{self.filename}', index=False)

        Model.set_number_of_stocks(0, 5, self.filename)
        Model.set_number_of_stocks(1, 10, self.filename)
        Model.set_number_of_stocks(2, 15, self.filename)
        Model.set_number_of_stocks(3, 20, self.filename)

        test1 = Model.get_number_of_stocks(0, self.filename)
        test2 = Model.get_number_of_stocks(1, self.filename)
        test3 = Model.get_number_of_stocks(2, self.filename)
        test4 = Model.get_number_of_stocks(3, self.filename)

        self.assertEqual(test1, 5.0)
        self.assertEqual(test2, 10.0)
        self.assertEqual(test3, 15.0)
        self.assertEqual(test4, 20.0)
        with self.assertRaises(FileNotFoundError):
            Model.get_number_of_stocks(0, 'notrealfile.csv')

    def test_add_stock(self):
        """ Test if it does add stock to portfolio """

        Model.add_stock('AAPL', 3.0, 5, self.filename)
        Model.add_stock('AMZN', 25.0, 2, self.filename)
        Model.add_stock('G', 81.0, 1, self.filename)

        df = pd.read_csv(f'{self.filename}', engine='python')
        sample_price1 = df.loc[df['Stock Symbol'] == 'AAPL', 'Buy in price']
        sample_price2 = df.loc[df['Stock Symbol'] == 'AMZN', 'Buy in price']
        sample_price3 = df.loc[df['Stock Symbol'] == 'G', 'Buy in price']

        sample_number1 = Model.get_number_of_stocks(0, self.filename)
        sample_number2 = Model.get_number_of_stocks(1, self.filename)
        sample_number3 = Model.get_number_of_stocks(2, self.filename)

        # TEST FOR Buy in price
        self.assertEqual(sample_price1.values[0], 3.0)
        self.assertEqual(sample_price2.values[0], 25.0)
        self.assertEqual(sample_price3.values[0], 81.0)

        # TEST FOR Number of Stocks
        self.assertEqual(sample_number1, 5)
        self.assertEqual(sample_number2, 2)
        self.assertEqual(sample_number3, 1)

        with self.assertRaises(FileNotFoundError):
            Model.add_stock('AAPL', 1, 2, 'notrealfile.csv')

if __name__ == '__main__':
    unittest.main()