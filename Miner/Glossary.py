from PyQt5.QtWidgets import QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QLineEdit, QCompleter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import csv
import pandas as pd


class Glossary(QVBoxLayout):
    """
    Glossary object that contains all glossary data and layout managers for the search bar, search button,
    and text area where definitions are shown.
    """

    def __init__(self):
        super(Glossary, self).__init__()
        """
        it's a Vbox with the search bar and button at the top and the text area for the definition underneath.
        That's what this init sets up.
        """

        self.layout = QVBoxLayout()
        self.glossarySearchLayout = QHBoxLayout()
        self.glossarySearchLayout.setAlignment(Qt.AlignTop)

        # set font
        self.font = QFont()
        self.font.setPixelSize(16)

        # create definition variable to store and print current definition
        self.definition = QLabel("")
        self.definition.setFixedHeight(250)
        self.definition.setFont(self.font)
        self.definition.setWordWrap(True)

        # create the search button
        self.searchButton = QPushButton("Search")
        self.searchButton.setFont(self.font)

        # set what the search button does
        self.searchBar = self.build_search_bar()
        self.searchButton.clicked.connect(lambda: self.search(self.searchBar.text()))

        # add it all to the glossary layout
        self.glossarySearchLayout.addWidget(self.searchBar)
        self.glossarySearchLayout.addWidget(self.searchButton)
        self.addLayout(self.glossarySearchLayout)
        self.addWidget(self.definition)
        self.setAlignment(Qt.AlignTop)

        # set up a place for the extra info links to appear for the user to learn more
        self.definition_topic = QLabel("After you search a term, info will appear here")
        self.definition_topic.setFont(self.font)
        self.definition_topic.setFixedHeight(200)
        self.definition_topic.setWordWrap(True)
        self.definition_topic.setTextFormat(Qt.RichText)
        self.definition_topic.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.definition_topic.setOpenExternalLinks(True)

        # add a second function to the search button
        self.searchButton.clicked.connect(lambda: self.getTopic(self.searchBar.text()))

        # add definition topic to the glossary layout
        self.addWidget(self.definition_topic)
        self.setAlignment(Qt.AlignTop)

    def build_search_bar(self):
        """
        builds the search bar and adds predictive texts to it
        :return: the search bar as a QLineEdit object
        """
        glossary_terms = ["agent", "assets", "symbol", "volume", "day range", "52 week range", "dividend", "yield",
                          "open price", "closing price", "stock categories", "sector", "bear market", "bonds",
                          "bull market", "business day", "capital", "certificate", "equities", "frequency",
                          "growth stock", "index", "inflation", "liquidity", "mutual fund", "option", "penny stock",
                          "portfolio", "preferred stock", "profit", "risk", "securities", "transactions", "volatility",
                          "venture capital"]
        searchBar = QLineEdit()
        completer = QCompleter(glossary_terms)
        searchBar.setCompleter(completer)

        return searchBar

    def search(self, term):
        """
        searches the python dictionary of terms and sets the text area in glossary as the definition of
        the searched term.
        :param term: the term to grab the definition of
        :return: none
        """
        term = term.lower()  # makes the given term lower case to prevent terms not being found due to case sensitivity

        terms_dict = {
              "agent": "A securities firm is classified as an agent when it acts on behalf of its clients as buyer or "
                       "seller of a security. The agent does not own the security at any time during the transaction.",
              "assets": "Everything a company or person owns, including money, securities, equipment and real estate. "
                        "Assets include everything that is owed to the company or person. Assets are listed on a "
                        "company's balance sheet or an individual's net worth statement.",
              "symbol": "This is the code for the company in the stock market.",
              "volume": "The total number of shares that were traded for that particular day.",
              "day range": "The highest and the lowest price that the stock has reached within the trading day.",
              "52 week range": "The highest and lowest price that the stock has reached within a span of 52 weeks.",
              "dividend": "The portion of the issuer's equity paid directly to shareholders. "
                           "It is generally paid on common or preferred shares. The issuer or its representative "
                           "provides the amount, frequency (monthly, quarterly, semi-annually, or annually), "
                           "payable date, and record date. The exchange that the issue is listed on sets the "
                           "ex-dividend/distribution (ex-d) date for entitlement. An issuer is under no legal "
                           "obligation to pay either preferred or common dividends. ",
              "yield": "This is the measure of the return on an investment and is shown as a percentage. "
                        "A stock yield is calculated by dividing the annual dividend by the stock's current "
                        "market price. For example, a stock selling at $50 and with an annual dividend of $5 "
                        "per share yields 10%. A bond yield is a more complicated calculation, involving annual "
                        "interest payments, plus amortizing the difference between its current market price and "
                        "par value over the life of the bond. ",
              "closing price": "The final price at which it trades during regular market hours on any given day.",
              "open price": "The price of the first trade for any listed stock is its daily opening price.",
              "stock categories": "Types of stocks: Income, Penny, Speculative, Growth, Defensive, Value, Cyclical.",
              "sector": "General representative of the overall sectors of the economy. Example: Energy, "
                        "Basic Materials, Industrials, Consumer Discretionary, Consumer Staples, Healthcare, "
                        "Financial,Information Technology, Communications, Utilities, Real Estate.",
              "bear market": "A market in which stock prices are falling.",
              "bonds": "Promissory notes issued by a corporation or government to its lenders, usually with a "
                        "specified amount of interest for a specified length of time.",
              "bull market": "A market in which stock prices are rising.",
              "business day": "Any day from Monday to Friday, excluding statutory holidays.",
              "capital": "To an economist, capital means machinery, factories and inventory required to produce "
                          "other products. To investors, capital means their cash plus the financial assets they "
                          "have invested in securities, their home and other fixed assets.",
              "certificate": "The physical document that shows ownership of a bond, stock or other security.",
              "equities": "Common and preferred stocks, which represent a share in the ownership of a company.",
              "frequency": "Frequency refers to the given time period on an intraday, daily, weekly, monthly, "
                            "quarterly or yearly perspective. Typically, choosing a weekly or monthly perspective "
                            "when looking at several years of data makes it easier to identify long-term trends. "
                            "Daily charts are useful for active traders and short-term time period charts.",
              "growth stock": "The shares of companies that have enjoyed better-than-average growth over recent "
                               "years and are expected to continue their climb.",
              "index": "A statistical measure of the state of the stock market, based on the performance of stocks. "
                       "Examples are the S&P/TSX Composite Index and the S&P/TSX Venture Composite Index.",
              "inflation": "An overall increase in prices for goods and services, usually measured by the "
                           "percentage change in the Consumer Price Index.",
              "liquidity": "This refers to how easily securities can be bought or sold in the market. A security"
                           " is liquid when there are enough units outstanding for large transactions to occur "
                           "without a substantial change in price. Liquidity is one of the most important "
                           "characteristics of a good market. Liquidity also refers to how easily investors can "
                           "convert their securities into cash and to a corporation's cash position, which is "
                           "how much the value of the corporation's current assets exceeds current liabilities.",
              "mutual fund": "A fund managed by an expert who invests in stocks, bonds, options, money market "
                             "instruments or other securities. Mutual fund units can be purchased through "
                             "brokers or, in some cases, directly from the mutual fund company.",
              "option": "The right, but not the obligation, to buy or sell certain securities at a specified "
                        "price within a specified time. A put option gives the holder the right to sell the "
                        "security, and a call option gives the holder the right to buy the security.",
              "penny stock": "Low-priced speculative issues of stock selling at less than $1.00 a share.",
              "portfolio": "Holdings of securities by an individual or institution. A portfolio may include "
                           "various types of securities representing different companies and industry sectors.",
              "preferred stock": "If there are several orders competing for a stock at the same price, a priority "
                          "determines when one of these orders will be filled before any other at this price. "
                          "Priority is based on the time at which the order is received into the system.",
              "profit": "What is left over for the owners of a business after all expenses have been deducted "
                        "from revenues. Gross profit is the profit before corporate income taxes. Net profit "
                        "is the final profit of the business after taxes have been paid.",
              "risk": "The future chance or probability of loss",
              "securities": "Transferable certificates of ownership of investment products such as notes, "
                            "bonds, stocks, futures contracts and options.",
              "transactions": "As reported in exchange trading statistics, represents the total number of "
                              "trades for a specified period.",
              "volatility": "A statistical measure of changes in price over a period of time.",
              "venture capital": "Money raised by companies to finance new ventures."
              }

        try:
            self.definition.setText(terms_dict[term])
        except:
            self.definition.setText("The term "+self.searchBar.text()+" was not found.")

    def getTopic(self, topic):
        """
        Takes in a topic and returns the info for that topic (a URL).
        :param topic: a String of a topic title
        :return: a list of info on the topic???
        """
        topic = topic.lower() # makes the given term lower case to prevent terms not being found due to case sensitivity

        topics_dict = {
            "agent": ["https://www.investopedia.com/terms/a/agent.asp", "youtube-link"],
            "assets": ["https://www.investopedia.com/terms/s/stock.asp", "youtube-link"],
            "symbol": ["https://www.investopedia.com/terms/s/stocksymbol.asp", "youtube-link"],
            "volume": ["https://www.fool.com/knowledge-center/what-is-volume-in-stock-trading.aspx", "youtube-link"],
            "day range": ["https://www.investopedia.com/terms/r/range.asp", "youtube-link"],
            "52 week range": ["https://www.investopedia.com/terms/1/52-week-range.asp", "youtube-link"],
            "dividend": ["https://www.investopedia.com/terms/s/stockdividend.asp", "youtube-link"],
            "yield": ["https://www.fool.com/knowledge-center/dividend-yield.aspx", "youtube-link"],
            "closing price": ["https://www.investopedia.com/terms/c/closingprice.asp", "youtube-link"],
            "open price": ["https://www.investopedia.com/terms/o/openingprice.asp", "youtube-link"],
            "stock categories": ["https://economictimes.indiatimes.com/definition/categories", "youtube-link"],
            "sector": ["https://www.investopedia.com/terms/s/sector-breakdown.asp", "youtube-link"],
            "bear market": ["https://www.investopedia.com/terms/b/bearmarket.asp", "youtube-link"],
            "bonds": ["https://www.investopedia.com/terms/b/bond.asp", "youtube-link"],
            "bull market": ["https://www.investopedia.com/terms/b/bullmarket.asp", "youtube-link"],
            "business day": ["https://www.investopedia.com/terms/b/business-day.asp", "youtube-link"],
            "capital": ["https://www.investopedia.com/terms/c/capital.asp", "youtube-link"],
            "certificate": ["https://www.investopedia.com/terms/s/stockcertificate.asp", "youtube-link"],
            "equities": ["https://www.investopedia.com/terms/e/equity.asp", "youtube-link"],
            "frequency": ["https://www.moneycontrol.com/glossary/stocks/frequency_3404.html", "youtube-link"],
            "growth stock": ["https://www.fool.com/investing/how-to-find-a-growth-stock.aspx", "youtube-link"],
            "index": ["https://www.investopedia.com/terms/i/index.asp", "youtube-link"],
            "inflation": ["https://www.investopedia.com/terms/i/inflation.asp", "youtube-link"],
            "liquidity": ["https://www.investopedia.com/terms/l/liquidity.asp", "youtube-link"],
            "mutual fund": ["https://www.investopedia.com/terms/m/mutualfund.asp", "youtube-link"],
            "option": ["https://www.investopedia.com/terms/o/option.asp", "youtube-link"],
            "penny stock": ["https://www.investopedia.com/terms/p/pennystock.asp", "youtube-link"],
            "portfolio": ["https://www.investopedia.com/terms/p/portfolio.asp", "youtube-link"],
            "preferred stock": ["https://www.investopedia.com/terms/p/preferredstock.asp", "youtube-link"],
            "profit": ["https://www.investopedia.com/terms/p/profit.asp", "youtube-link"],
            "risk": ["https://www.investopedia.com/terms/r/risk.asp", "youtube-link"],
            "securities": ["https://www.investopedia.com/terms/s/security.asp", "youtube-link"],
            "transactions": ["https://www.investopedia.com/terms/t/transaction.asp", "youtube-link"],
            "volatility": ["https://www.investopedia.com/terms/v/volatility.asp", "youtube-link"],
            "venture capital": ["https://www.investopedia.com/terms/v/venturecapital.asp.", "youtube-link"]
        }
        try:
            self.definition_topic.setText("<a href=" + topics_dict[topic].__getitem__(0)
                                          + "> Click here to go to a resource about " + topic + "</a>")
        except:
            self.definition_topic.setText("The topic " + topic + " was not found.")


def makeDict(filename):
    """
    Creates an dictionary. CSV file must terms and description column only.

    :param filename: STRING, pathname to the file.
    :return: dictionary of terms and description of stocks
    """
    terms_dict = dict()

    try:
        with open(f'{filename}', mode='r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header

    except FileNotFoundError as e:
        raise e                                     # If the file is not found

    except Exception as e:
        raise e                                     # If something went wrong

    else:
        for row in reader:
            key = row[0]
            if key in terms_dict:
                pass
            terms_dict[key] = row[1]

    return terms_dict


def addGlossary(term, description):
    """
    Added a row in CSV file

    :param term: STRING, this will be the key of the description.
    :param description: STRING, this will be the value of the term.
    :return: None
    """

    try:
        with open('CSVdata/glossary.csv', 'w') as f:
            lineWrite = csv.writer(f)

    except FileNotFoundError as e:
        raise e                                             # if the file is not found

    else:
        lineWrite.writerow([term, description])             # Add a row in csv file

    finally:
        print(f'The term {term} has been added into your glossary')