from PyQt5.QtGui import QIcon, QFont, QDesktopServices
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QDialog, QLabel, QLineEdit
from PyQt5.QtCore import Qt, QRect, QUrl
from Miner import Welcome as W
from Miner import Model as M


class Help(QVBoxLayout):
    """
    Help objects will be carry links to local information
    """
    def __init__(self):
        super(Help, self).__init__()

        self.layout = QVBoxLayout()

        self.font = QFont()
        self.font.setPixelSize(20)

        self.button = QPushButton("Press here for help")
        self.button.setFont(self.font)
        self.button.setFixedHeight(50)
        self.addWidget(self.button)
        self.setAlignment(Qt.AlignBottom)


def help_dialog():
    d = QDialog()

    d.setWindowIcon(QIcon('./Icons/MinerIcon.png'))
    d.setWindowTitle('Miner Help')
    d.left = 500
    d.top = 200
    d.width = 500
    d.height = 400

    font1 = QFont()
    font1.setBold(True)
    font1.setPixelSize(50)

    font2 = QFont()
    font2.setPixelSize(26)

    font3 = QFont()
    font3.setPixelSize(20)

    mainLabel = QLabel("Miner Help Section", d)
    mainLabel.setWordWrap(True)
    mainLabel.setAlignment(Qt.AlignCenter)
    mainLabel.setGeometry(QRect(10, 10, 400, 150))
    mainLabel.setFont(font1)

    moneyLabel = QLabel("I need more money!", d)
    moneyLabel.setWordWrap(True)
    moneyLabel.setAlignment(Qt.AlignCenter)
    moneyLabel.setGeometry(QRect(10, 100, 400, 160))
    moneyLabel.setFont(font2)

    moneyBox = QLineEdit("", d)
    moneyBox.setGeometry(QRect(50, 210, 200, 40))

    moneyButton = QPushButton("Add $$$", d)
    moneyButton.setGeometry(QRect(260, 210, 100, 40))
    moneyButton.clicked.connect(lambda: M.add_capital(moneyBox.text(), "CSVdata/User1Transactions.csv"))

    expLabel = QLabel("Reach out to experts in your area", d)
    expLabel.setWordWrap(True)
    expLabel.setAlignment(Qt.AlignCenter)
    expLabel.setGeometry(QRect(10, 200, 400, 160))
    expLabel.setFont(font2)

    linkLabel = QLabel("", d)
    linkLabel.setWordWrap(True)
    linkLabel.setAlignment(Qt.AlignCenter)
    linkLabel.setGeometry(QRect(10, 250, 400, 160))
    linkLabel.setFont(font3)
    linkLabel.setText("<a href=" + "https://www.manta.com/world/North+America/Canada/stock_brokers_and_dealers--A10D302Y" + "> Click here to go to find local stock experts </a>")
    linkLabel.setTextFormat(Qt.RichText)
    linkLabel.setTextInteractionFlags(Qt.TextBrowserInteraction)
    linkLabel.setOpenExternalLinks(True)

    d.exec()


def open_video_help():
    QDesktopServices.openUrl(QUrl("https://www.khanacademy.org/economics-finance-domain/core-finance/stock-and-bonds"))


def reset_progress():
        W.Welcome()

