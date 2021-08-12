import pyqt5_tools
import pyqt5_plugins
import PyQt5
import math
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, endl
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import sys
class MainWindow(QMainWindow):
    zahl1 = int
    zahl2 = int
    zahl3 = int
    Rechenverfahren = "nix"
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(350, 400))    
        self.setWindowTitle("Python Calculator") 
        buttonPlus = QPushButton('7', self)
        buttonPlus.clicked.connect(self.sieben)
        buttonPlus.resize(50,32)
        buttonPlus.move(00, 50) 
        buttonPlus = QPushButton('4', self)
        buttonPlus.clicked.connect(self.vier)
        buttonPlus.resize(50,32)
        buttonPlus.move(00, 100) 
        buttonPlus = QPushButton('1', self)
        buttonPlus.clicked.connect(self.eins)
        buttonPlus.resize(50,32)
        buttonPlus.move(00, 150)
        buttonPlus = QPushButton('8', self)
        buttonPlus.clicked.connect(self.acht)
        buttonPlus.resize(50,32)
        buttonPlus.move(50, 50) 
        buttonPlus = QPushButton('5', self)
        buttonPlus.clicked.connect(self.fuenf)
        buttonPlus.resize(50,32)
        buttonPlus.move(50, 100) 
        buttonPlus = QPushButton('2', self)
        buttonPlus.clicked.connect(self.zwei)
        buttonPlus.resize(50,32)
        buttonPlus.move(50, 150) 
        buttonPlus = QPushButton('9', self)
        buttonPlus.clicked.connect(self.neun)
        buttonPlus.resize(50,32)
        buttonPlus.move(100, 50) 
        buttonPlus = QPushButton('6', self)
        buttonPlus.clicked.connect(self.sechs)
        buttonPlus.resize(50,32)
        buttonPlus.move(100, 100) 
        buttonPlus = QPushButton('3', self)
        buttonPlus.clicked.connect(self.drei)
        buttonPlus.resize(50,32)
        buttonPlus.move(100, 150)
        buttonPlus = QPushButton('0', self)
        buttonPlus.clicked.connect(self.null)
        buttonPlus.resize(50,32)
        buttonPlus.move(0, 200)
        buttonPlus = QPushButton('AC', self)
        buttonPlus.clicked.connect(self.AC)
        buttonPlus.resize(50,32)
        buttonPlus.move(50, 200)
        buttonWurzel = QPushButton(',', self)
        buttonWurzel.clicked.connect(self.Komma)
        buttonWurzel.resize(50,32)
        buttonWurzel.move(150, 200)

        buttonPlus = QPushButton('+', self)
        buttonPlus.clicked.connect(self.Addition)
        buttonPlus.resize(50,32)
        buttonPlus.move(150, 50)
        buttonMinus = QPushButton('-', self)
        buttonMinus.clicked.connect(self.Subtraktion)
        buttonMinus.resize(50,32)
        buttonMinus.move(200, 50)
        buttonMal = QPushButton('*', self)
        buttonMal.clicked.connect(self.Multiplikation)
        buttonMal.resize(50,32)
        buttonMal.move(150, 100)
        buttonGeteilt = QPushButton('/', self)
        buttonGeteilt.clicked.connect(self.Division)
        buttonGeteilt.resize(50,32)
        buttonGeteilt.move(200, 100)
        buttonWurzel = QPushButton('√', self)
        buttonWurzel.clicked.connect(self.Wurzel)
        buttonWurzel.resize(50,32)
        buttonWurzel.move(150, 150)
        buttonPotenz = QPushButton('Potenz', self)
        buttonPotenz.clicked.connect(self.Potenz)
        buttonPotenz.resize(50,32)
        buttonPotenz.move(200, 150)
        buttonErgebnis = QPushButton('=', self)
        buttonErgebnis.clicked.connect(self.Ergebnis)
        buttonErgebnis.resize(50,32)
        buttonErgebnis.move(100, 200)
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(20, 20)
        self.textbox1.resize(280,30)

    def eins(self):
        self.textbox1.setText (self.textbox1.text() + str(1))
    def zwei(self):
        self.textbox1.setText (self.textbox1.text() + str(2))
    def drei(self):
        self.textbox1.setText (self.textbox1.text() + str(3))
    def vier(self):
        self.textbox1.setText (self.textbox1.text() + str(4))
    def fuenf(self):
        self.textbox1.setText (self.textbox1.text() + str(5))
    def sechs(self):
        self.textbox1.setText (self.textbox1.text() + str(6))
    def sieben(self):
        self.textbox1.setText (self.textbox1.text() + str(7))
    def acht(self):
        self.textbox1.setText (self.textbox1.text() + str(8))
    def neun(self):
        self.textbox1.setText (self.textbox1.text() + str(9))
    def null(self):
        self.textbox1.setText (self.textbox1.text() + str(0))
    def Komma(self):
        self.textbox1.setText (self.textbox1.text() + str("."))
    def AC(self):
        self.textbox1.setText ("")

    def Addition(self):
        self.zahl1 = self.textbox1.text()
        self.Rechenverfahren = "Plus"
    def Subtraktion(self):
        self.zahl1 = self.textbox1.text()
        self.Rechenverfahren = "Minus"
    def Multiplikation(self):
        self.zahl1 = self.textbox1.text()
        self.Rechenverfahren = "Mal"
    def Division(self):
        self.zahl1 = self.textbox1.text()
        self.Rechenverfahren = "Geteilt"
    def Potenz(self):
        self.zahl1 = self.textbox1.text()
        self.Rechenverfahren = "Potenz"
    def Wurzel(self):
        self.zahl1 = self.textbox1.text()
        self.Rechenverfahren = "Wurzel"
        self.Ergebnis()
    def Ergebnis(self):
        self.zahl2 = self.textbox1.text()

        if self.Rechenverfahren == "Plus" :
            self.textbox1.setText( str(float(self.zahl1) + float(self.zahl2)))
        
        if self.Rechenverfahren == "Minus" :
            self.textbox1.setText( str(float(self.zahl1) - float(self.zahl2)))
        
        if self.Rechenverfahren == "Mal" :
            self.textbox1.setText( str(float(self.zahl1) * float(self.zahl2)))
        
        if self.Rechenverfahren == "Geteilt" :
            self.textbox1.setText( str(float(self.zahl1) / float(self.zahl2)))
            
        if self.Rechenverfahren == "Wurzel" :
            self.textbox1.setText( str(math.sqrt(float(self.zahl1))))
            
        if self.Rechenverfahren == "Potenz" :
            self.zahl3 = self.zahl1
            while float(self.zahl2) > 1:
                self.zahl3 = float(self.zahl1) * float(self.zahl3)
                self.zahl2 = float(self.zahl2) - 1
            self.textbox1.setText( str(float(self.zahl3)))
            
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )