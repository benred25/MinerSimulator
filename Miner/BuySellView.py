from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QLineEdit, QVBoxLayout, QCompleter, QComboBox
from Miner import Model
from Miner.Model import get_current_stock_price
from Miner import Messages as M

class BuySellView(QHBoxLayout):

    def __init__(self):
        super(BuySellView, self).__init__()

        # fonts
        font = QFont()
        font.setBold(True)
        font.setPixelSize(15)

        cFont = QFont()
        cFont.setBold(True)
        cFont.setPixelSize(20)

        efont = QFont()
        efont.setPixelSize(19)

        # Capital
        currentCapital = QLabel("Current Capital")
        currentCapital.setFont(cFont)
        self.money = QLabel("")
        self.money.setFont(font)
        capital = Model.get_current_capital("CSVdata/User1Transactions.csv")
        self.money.setText(str(capital))

        # Last Buy & Last Sell
        lastBuyLabel = QLabel("Last Purchase")
        lastBuyLabel.setFont(cFont)
        self.lastBuy = QLabel("")
        self.lastBuy.setFont(font)

        lastSellLabel = QLabel("Last Sale")
        lastSellLabel.setFont(cFont)
        self.lastSale = QLabel("")
        self.lastSale.setFont(font)


        # buy stock stuff
        buyTitle = QLabel("Buy")
        buyTitle.setFont(cFont)
        buyButton = QPushButton("Buy")
        buyButton.setFont(efont)
        buyCompanySymbolTitle = QLabel("Company Symbol")
        buyCompanySymbolTitle.setFont(efont)
        # add predictive text to the buy bar
        self.buyCompanySymbol = self.build_buy_bar()
        buyNumOfStocksTitle = QLabel("Amount to Buy")
        buyNumOfStocksTitle.setFont(efont)
        self.buyNumOfStocks = QLineEdit()

        # sell stock stuff
        sellTitle = QLabel("Sell")
        sellTitle.setFont(cFont)
        sellButton = QPushButton("Sell")
        sellButton.setFont(efont)
        sellTransactionIndexTitle = QLabel("Transaction Index")
        sellTransactionIndexTitle.setFont(efont)
        # add predictive text to the sell bar
        self.sellTransactionIndex = QLineEdit()  # will need to be: self.build_sell_bar()
        sellNumOfStocksTitle = QLabel("Amount to Sell")
        sellNumOfStocksTitle.setFont(efont)
        self.sellNumOfStocks = QLineEdit()

        # capital layout
        capitalLayout = QVBoxLayout()

        c1 = QHBoxLayout()
        c1.addWidget(currentCapital)
        c1.addWidget(self.money, 0, Qt.AlignCenter)
        capitalLayout.addLayout(c1)

        c2 = QHBoxLayout()
        c2.addWidget(lastBuyLabel)
        c2.addWidget(self.lastBuy, 0, Qt.AlignCenter)
        capitalLayout.addLayout(c2)

        c3 = QHBoxLayout()
        c3.addWidget(lastSellLabel)
        c3.addWidget(self.lastSale, 0, Qt.AlignCenter)
        capitalLayout.addLayout(c3)

        # buy layout
        buyLayout = QVBoxLayout()
        buyLayout.addWidget(buyTitle)

        b1 = QHBoxLayout()
        b1.addWidget(buyCompanySymbolTitle)
        b1.addWidget(self.buyCompanySymbol)
        buyLayout.addLayout(b1)

        b2 = QHBoxLayout()
        b2.addWidget(buyNumOfStocksTitle)
        b2.addWidget(self.buyNumOfStocks)
        buyLayout.addLayout(b2)

        buyLayout.addWidget(buyButton)

        # sell layout
        sellLayout = QVBoxLayout()
        sellLayout.addWidget(sellTitle)

        s1 = QHBoxLayout()
        s1.addWidget(sellTransactionIndexTitle)
        s1.addWidget(self.sellTransactionIndex)
        sellLayout.addLayout(s1)

        s2 = QHBoxLayout()
        s2.addWidget(sellNumOfStocksTitle)
        s2.addWidget(self.sellNumOfStocks)
        sellLayout.addLayout(s2)

        sellLayout.addWidget(sellButton)

        # bring it all together
        self.addLayout(capitalLayout)
        self.addLayout(buyLayout)
        self.addLayout(sellLayout)

        buyButton.clicked.connect(lambda : self.buy())
        sellButton.clicked.connect(lambda : self.sell())

    def buy(self):
        """
        Called buy the buy button and buys the user the desired stocks
        """
        # check for invalid user input in the buy text boxes
        # and throw an exception if anything is invalid
        try:
            n = int(self.buyNumOfStocks.text())
            if n <= 0:
                self.buyNumOfStocks.setText("")
                int("")
        except:
            M.showdialog("You entered an invalid amount of stocks to buy. Please make sure you enter a postive interger.")
            return

        # buy the stocks for the user
        prevCap = Model.get_current_capital("CSVdata/User1Transactions.csv")
        Model.buy_stock(self.buyCompanySymbol.currentText(),
                        get_current_stock_price(self.buyCompanySymbol.currentText(), "CSVdata/User1Timeline.csv"),
                        int(self.buyNumOfStocks.text()),
                        "CSVdata/User1Transactions.csv")
        self.buyNumOfStocks.setText("")
        capital = Model.get_current_capital("CSVdata/User1Transactions.csv")
        self.money.setText(str(capital))
        self.lastBuy.setText(str(prevCap - capital))

    def sell(self):
        """
        Called by the sell button and used to sell the user's desired stocks
        """
        # check for invalid user input to the sell text boxes
        # and throw an exception if anything is invalid
        try:
            n = int(self.sellTransactionIndex.text())
            if n < 0:
                self.sellNumOfStocks.setText("")
                self.sellTransactionIndex.setText("")
                int("")
        except:
            M.showdialog("You entered an invalid transaction index. Please make sure it matches one in your transaction list.")
            return
        try:
            n = int(self.sellNumOfStocks.text())
            if n <= 0:
                self.sellNumOfStocks.setText("")
                self.sellTransactionIndex.setText("")
                int("")
        except:
            M.showdialog("You entered an invalid number of stocks to sell. Please make sure you enter a positive integer.")
            return

        # sell the stocks for the user
        prevCap = Model.get_current_capital("CSVdata/User1Transactions.csv")
        Model.sell_stock(int(self.sellTransactionIndex.text()),
                         int(self.sellNumOfStocks.text()),
                         "CSVdata/User1Transactions.csv")
        self.sellNumOfStocks.setText("")
        self.sellTransactionIndex.setText("")
        capital = Model.get_current_capital("CSVdata/User1Transactions.csv")
        self.money.setText(str(capital))
        self.lastSale.setText(str(capital - prevCap))

    def build_buy_bar(self):
        """
        builds the buy bar and adds predictive texts to it
        :return: the search bar as a QLineEdit object
        """
        buy_bar = QComboBox()
        buy_bar.addItems(["AAPL", "AMZN", "DOW", "G", "INTC", "INTU", "NVDA", "RS", "SAM", "SNP500"])

        return buy_bar

    def build_sell_bar(self):
        """
        builds the sell bar from user portfolio and adds predictive texts to it
        :return: the search bar as a QLineEdit object
        """
        user_stocks = []
        sell_bar = QLineEdit()
        completer = QCompleter(user_stocks)
        sell_bar.setCompleter(completer)

        return sell_bar
