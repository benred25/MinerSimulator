from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QHBoxLayout, QTabWidget, QWidget, QApplication, QPushButton
import threading
from Miner import Glossary as G
from Miner import Help as H
from Miner import Welcome as W
from Miner import Messages as M
from Miner import Controller, CreateDatabases, MarketView, Model, BuySellView, PortfolioView
# Stock, StockExchange, StockInvestor, UserID

import os, sys

# frozen = 'not'
# if getattr(sys, 'frozen', False):
#         # we are running in a bundle
#         frozen = 'ever so'
#         bundle_dir = sys._MEIPASS
# else:
#         # we are running in a normal Python environment
#         bundle_dir = os.path.dirname(os.path.abspath(__file__))
#
# print( 'we are',frozen,'frozen')
# print( 'bundle dir is', bundle_dir )
# print( 'sys.argv[0] is', sys.argv[0] )
# print( 'sys.executable is', sys.executable )
# print( 'os.getcwd is', os.getcwd() )


class CustomMainWindow(QMainWindow):  # MainWindow is a subclass of QMainWindow
    def __init__(self, *args, **kwargs):
        super(CustomMainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Miner")

        # set font
        self.font = QFont()
        self.font.setPixelSize(20)

        mainArea = QVBoxLayout()    # main layout for the buy, sell, portfolio, and market areas of the screen

        layout = QHBoxLayout()  # layout for the entire program screen

        learningLayout = QVBoxLayout()  # layout for the right side of screen with learning materials
        learningLayout.addSpacing(20)

        TW = QTabWidget()   # widget for market and portfolio tabs

        # create the server for portfolio view
        web1 = QWebEngineView()
        web1.load(QUrl("http://127.0.0.1:8052"))

        # create the server for market view
        web2 = QWebEngineView()
        web2.load(QUrl("http://127.0.0.1:8051"))

        # add the tabs
        TW.addTab(web1, 'Portfolio')
        TW.addTab(web2, 'Market')

        # add the tabs and buy and sell to the main area of the screen
        mainArea.addWidget(TW)
        mainArea.addLayout(BuySellView.BuySellView())

        layout.addLayout(mainArea) # add the main area to the program

        # add glossary search bar to gui layout
        gloss = G.Glossary()
        w = QWidget()
        w.setLayout(gloss)
        w.setFixedWidth(400)
        learningLayout.addWidget(w)

        # # add topics to gui layout
        # topics = T.Topics()
        # w = QWidget()
        # w.setLayout(topics)
        # w.setFixedWidth(400)
        # learningLayout.addWidget(w)

        # create grade me button
        gradeMeButton = QPushButton()
        gradeMeButton.setText("Press here to be graded")
        gradeMeButton.setFont(self.font)
        gradeMeButton.setFixedHeight(50)
        gradeMeButton.clicked.connect(lambda: M.grade_me())

        # create button to take you to video learning
        videoHelpButton = QPushButton()
        videoHelpButton.setText("Video Learning via Khan Academy")
        videoHelpButton.setFont(self.font)
        videoHelpButton.setFixedHeight(50)
        videoHelpButton.clicked.connect(lambda: H.open_video_help())

        # create help area
        help = H.Help()
        button = help.button
        button.clicked.connect(lambda: H.help_dialog())
        help.addWidget(gradeMeButton) # add grade me button underneath help button
        help.addWidget(videoHelpButton)  # add video learning button to layout

        # create a reset progress button
        resetButton = QPushButton("Press here to reset simulation")
        resetButton.setFont(self.font)
        resetButton.setFixedHeight(50)
        resetButton.clicked.connect(lambda: H.resetProgress())
        help.addWidget(resetButton)

        # add all the learning tools to the learning layout at the right side of the screen
        w = QWidget()
        w.setLayout(help)
        w.setFixedWidth(400)
        learningLayout.addWidget(w)

        layout.addLayout(learningLayout)    # add the learning layout to the main program layout

        # set the layout for the entire main window
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


""" Method to build the backend (we can use model methods to add/remove data)"""
def BuildBackend():
    conn = CreateDatabases.create_database('MinerDB')
    Model.add_data_to_USERS(conn, 'CSVdata/Users.csv')
    Model.add_data_to_STOCK_ID(conn, 'CSVdata/StockID.csv')
    # Model.add_data_to_TRANSASCTIONS()
    # Model.add_data_to_PORTFOLIO()


def main():
    """
    The main function to create the windows and show them to the user.
    Basically just runs the program for the user.
    """

    # Model.grab_data()
    # connection = CreateDatabases.create_connection("MinerDB")
    # Model.add_data_to_portfolio_table(12000.0, 16500.0, 4500.0, connection)

    # create a thread to run the market view server
    market = threading.Thread(target=MarketView.generate_market_view, daemon=True)
    market.start()

    # create a thread to run the portfolio view server
    portfolio = threading.Thread(target=PortfolioView.generate_portfolio_view, daemon=True)
    portfolio.start()

    app = QApplication(sys.argv)

    W.Welcome()  # bring up welcome screen

    # bring up main program window
    CMWindow = CustomMainWindow()
    CMWindow.setGeometry(40, 40, 1800, 900)
    CMWindow.setWindowIcon(QIcon('./Icons/MinerIcon.png'))
    CMWindow.show()
    sys.exit(app.exec())

    #BuildBackend()


if __name__ == "__main__":
    main()
