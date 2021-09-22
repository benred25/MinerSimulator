import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog, QRadioButton, QLabel
from Miner import Model

def window():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QPushButton(w)
    b.setText("Show error message!")

    b.move(50, 50)
    b.clicked.connect(ask_reset)
    w.setWindowTitle("Error has occurred!")
    w.show()
    sys.exit(app.exec_())


def showdialog(error):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("You have encountered an error")
    msg.setWindowTitle("Error!")
    msg.setDetailedText("The details are as follows: " + error)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.buttonClicked.connect(msgbtn)

    retval = msg.exec_()


def ask_reset():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)

    msg.setText("Would you like to reset?")
    msg.setWindowTitle("Reset Progress?")
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg.buttonClicked.connect(msgbtn)

    retval = msg.exec_()

def grade_me():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Grade: "+Model.grade_performance("CSVdata/User1Transactions.csv"))
    msg.setDetailedText("Your grade is based on the profit profit percentage gained from your original capital amount. "
                        "If you didn't make any money you will get a letter grade of F and if you make your money back "
                        "you will receive a higher letter grade. ")
    msg.setWindowTitle("Your Performance Grade                   ")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.buttonClicked.connect(msgbtn)

    msg.exec_()

def msgbtn(i):
    print("Button pressed is:", i.text())
    if i is object:
        print("YES")
    else:
        print("NO")
        return

def money_added():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Money has been added to your account.")
    msg.setWindowTitle("Money Added!")
    msg.setStandardButtons(QMessageBox.Ok)

    msg.exec_()

if __name__ == '__main__':
    window()