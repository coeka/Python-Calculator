import pyqt5_tools
import pyqt5_plugins
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize   
from PyQt5.QtWidgets import QLabel 
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
import sys
class MainWindow(QMainWindow):
    zahl1 = int
    zahl2 = int
    Rechenverfahren = "nix"
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(350, 400))    
        self.setWindowTitle("Python Calculator") 

        buttonPlus = QPushButton('+', self)
        buttonPlus.clicked.connect(self.Addition)
        buttonPlus.resize(100,32)
        buttonPlus.move(50, 50)
        buttonMinus = QPushButton('-', self)
        buttonMinus.clicked.connect(self.Subtraktion)
        buttonMinus.resize(100,32)
        buttonMinus.move(200, 50)
        buttonMal = QPushButton('*', self)
        buttonMal.clicked.connect(self.Multiplikation)
        buttonMal.resize(100,32)
        buttonMal.move(50, 100)
        buttonGeteilt = QPushButton('/', self)
        buttonGeteilt.clicked.connect(self.Division)
        buttonGeteilt.resize(100,32)
        buttonGeteilt.move(200, 100)
        buttonErgebnis = QPushButton('=', self)
        buttonErgebnis.clicked.connect(self.Ergebnis)
        buttonErgebnis.resize(100,32)
        buttonErgebnis.move(100, 200)
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(20, 20)
        self.textbox1.resize(280,30)

    
    def Addition(self):
        self.zahl1 = self.textbox1.text()
        Rechenverfahren = "Plus"
    def Subtraktion(self):
        self.zahl1 = self.textbox1.text()
        zahl1= self.textbox.text
        Rechenverfahren = "Minus"
    def Multiplikation(self):
        self.zahl1 = self.textbox1.text()
        zahl1= self.textbox.text
        Rechenverfahren = "Mal"
    def Division(self):
        self.zahl1 = self.textbox1.text()
        zahl1= self.textbox.text
        Rechenverfahren = "Geteilt"
    def Ergebnis(self):
        self.zahl2 = self.textbox1.text()
        self.textbox1.setText( str(int(self.zahl1) + int(self.zahl2)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )