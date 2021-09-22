import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog, QRadioButton, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import pyqtSlot, QRect, Qt

from Miner import Model as Model


class Welcome(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        d = QDialog()

        d.setWindowIcon(QIcon('./Icons/MinerIcon.png'))
        d.setWindowTitle('Miner')
        d.left = 500
        d.top = 300
        d.width = 800
        d.height = 400

        font1 = QFont()
        font1.setBold(True)
        font1.setPixelSize(60)

        font2 = QFont()
        font2.setPixelSize(30)

        font3 = QFont()
        font3.setPixelSize(22)

        buttonFont = QFont()
        buttonFont.setPixelSize(18)

        self.imagelLabel = QLabel(d)
        self.pixmap = QPixmap('./Icons/MinerAlt.png')
        self.imagelLabel.setPixmap(self.pixmap)
        self.imagelLabel.move(20,20)
        # self.resize(self.pixmap.width(),self.pixmap.height())

        self.mainLabel = QLabel("Welcome to Miner", d)
        self.mainLabel.setWordWrap(True)
        self.mainLabel.setAlignment(Qt.AlignCenter)
        self.mainLabel.setGeometry(QRect(440, 40, 350, 160))
        self.mainLabel.setFont(font1)

        self.secondaryLabel = QLabel("Stock Market Teacher and Simulator", d)
        self.secondaryLabel.setWordWrap(True)
        self.secondaryLabel.setAlignment(Qt.AlignCenter)
        self.secondaryLabel.setGeometry(QRect(470, 130, 300, 200))
        self.secondaryLabel.setFont(font2)

        self.label = QLabel("Choose starting capital:", d)
        self.label.setFont(font3)
        self.label.move(20, 320)

        self.option1 = QRadioButton("1,000", d)
        self.option1.setFont(buttonFont)

        self.option2 = QRadioButton("10,000", d)
        self.option2.setFont(buttonFont)

        self.option3 = QRadioButton("100,000", d)
        self.option3.setFont(buttonFont)

        self.option4 = QRadioButton("1,000,000", d)
        self.option4.setFont(buttonFont)

        self.option1.move(250, 322)
        self.option2.move(320, 322)
        self.option3.move(400, 322)
        self.option4.move(490, 322)

        Model.reset_portfolio()
        Model.reset_timeline()

        self.option1.setChecked(True)

        self.file = "CSVdata/User1Transactions.csv"

        if self.option1.isChecked():
            Model.set_current_capital(1000, self.file)
            Model.set_initial_capital(1000, self.file)
        if self.option2.isChecked():
            Model.set_current_capital(10000, self.file)
            Model.set_initial_capital(10000, self.file)
        if self.option3.isChecked():
            Model.set_current_capital(100000, self.file)
            Model.set_initial_capital(100000, self.file)
        if self.option4.isChecked():
            Model.set_current_capital(1000000, self.file)
            Model.set_initial_capital(1000000, self.file)

        self.openButton = QPushButton("Begin", d)
        self.openButton.setFont(font3)
        self.openButton.setMinimumSize(180, 50)
        self.openButton.move(600, 310)
        self.openButton.clicked.connect(self.on_click)
        self.openButton.clicked.connect(lambda: d.accept())

        d.exec_()

    @pyqtSlot()
    def on_click(self):
        if self.option1.isChecked():
            Model.set_current_capital(1000, self.file)
            Model.set_initial_capital(1000, self.file)
        if self.option2.isChecked():
            Model.set_current_capital(10000, self.file)
            Model.set_initial_capital(10000, self.file)
        if self.option3.isChecked():
            Model.set_current_capital(100000, self.file)
            Model.set_initial_capital(100000, self.file)
        if self.option4.isChecked():
            Model.set_current_capital(1000000, self.file)
            Model.set_initial_capital(1000000, self.file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Welcome()
    sys.exit(app.exec_())