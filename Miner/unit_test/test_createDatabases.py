import unittest
import sqlite3
import pandas as pd
import csv
import os

""" Python file to check """
from Miner import CreateDatabases

# ---------------------------------------------------------

class TestCreateDatabases ( unittest.TestCase ):

    @classmethod
    def setUp(self):
        # Create an csv sample file for users
        with open('UserSample.csv', 'w') as f:
            lineWrite = csv.writer(f)

            # user samples
            lineWrite.writerow(['UserName', 'Email', 'Money'])
            lineWrite.writerow(['bot1', 'bot1@yahoo.com', 500])
            lineWrite.writerow(['bot2', 'bot2@gmail.com', 600])

        # Create an csv sample file for stocks
        with open('StockSample.csv', 'w') as f:
            lineWrite = csv.writer(f)

            # stock samples
            lineWrite.writerow(['Symbol', 'Name'])
            lineWrite.writerow(['ABC', 'firstAlpha'])
            lineWrite.writerow(['YXZ', 'lastAlpha'])

        self.db = CreateDatabases.create_database(':memory:')               # not test for create_database

    @classmethod
    def tearDown(self):
        # Delete csv sample files
        os.remove('UserSample.csv')
        os.remove('StockSample.csv')

    def test_create_database(self):
        """
        Test if create_database function creates the table properly
        """
        sample = CreateDatabases.create_database(':memory:')

        c = sample.cursor()

        # Add the sample data file of USERS into the database
        readUser = pd.read_csv(r'UserSample.csv')
        readUser.to_sql('USERS', sample, if_exists='append', index=False)

        # USER TESTING 1 --------------------------------------------------------------
        c.execute("SELECT * FROM USERS WHERE UserName=:UserName", {'UserName' : 'bot1'})

        Result1 = c.fetchall()
        user1 = Result1[0][1]
        email1 = Result1[0][2]
        money1 = Result1[0][3]

        self.assertEqual(user1, 'bot1')
        self.assertEqual(email1, 'bot1@yahoo.com')
        self.assertEqual(money1, 500)

        # USER TESTING 2 -------------------------------------------------------------
        c.execute("SELECT * FROM USERS WHERE UserName=:UserName", {'UserName': 'bot2'})

        Result2 = c.fetchall()
        user2 = Result2[0][1]
        email2 = Result2[0][2]
        money2 = Result2[0][3]

        self.assertEqual(user2, 'bot2')
        self.assertEqual(email2, 'bot2@gmail.com')
        self.assertEqual(money2, 600)

        # Add the sample data file of STOCKS into the database
        readUser = pd.read_csv(r'StockSample.csv')
        readUser.to_sql('STOCK_ID', sample, if_exists='append', index=False)

        # STOCK TESTING 1 ---------------------------------------------------------
        c.execute("SELECT * FROM STOCK_ID WHERE Symbol=:Symbol", {'Symbol': 'ABC'})

        Result1 = c.fetchall()
        symbol = Result1[0][1]
        name = Result1[0][2]

        self.assertEqual(symbol, 'ABC')
        self.assertEqual(name, 'firstAlpha')

        # STOCK TESTING 2 ---------------------------------------------------------
        c.execute("SELECT * FROM STOCK_ID WHERE Symbol=:Symbol", {'Symbol': 'YXZ'})

        Result1 = c.fetchall()
        symbol = Result1[0][1]
        name = Result1[0][2]

        self.assertEqual(symbol, 'YXZ')
        self.assertEqual(name, 'lastAlpha')

        sample.close()      # Close database

    def test_remove_data_table(self):
        """
        Test if the remove_data function deletes the table.
        """
        c = self.db.cursor()

        # Add the sample data file of USERS into the database
        readUser = pd.read_csv(r'UserSample.csv')
        readUser.to_sql('USERS', self.db, if_exists='append', index=False)

        c.execute("SELECT * FROM USERS")
        data = c.fetchall()[-1][0]        # Expected value 2

        # TESTING -------------------------------------------------------
        CreateDatabases.remove_data_table('USERS', self.db)

        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='USERS'")
        result = c.fetchall()

        self.assertNotEqual(result, data)

        self.db.close()

    def test_add_data(self):
        """
        Test if the add_data function added the csv file to the databas.
        """
        c = self.db.cursor()

        # TESTING -------------------------------------------------------
        CreateDatabases.add_data_to_table(self.db, 'USERS', 'UserSample.csv')

        c.execute("SELECT * FROM USERS")

        result = c.fetchall()

        # Sample 1
        user1 = result[0][0]
        email1 = result[0][1]
        money1 = result[0][2]

        # Sample 2
        user2 = result[1][0]
        email2 = result[1][1]
        money2 = result[1][2]

        self.assertEqual(user1, 'bot1')
        self.assertEqual(email1, 'bot1@yahoo.com')
        self.assertEqual(money1, 500)

        self.assertEqual(user2, 'bot2')
        self.assertEqual(email2, 'bot2@gmail.com')
        self.assertEqual(money2, 600)

        self.db.close()     # Close database

if __name__ == '__main__':
    unittest.main()