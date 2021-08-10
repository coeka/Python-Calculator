import pyqt5_tools
import pyqt5_plugins
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys
app = QApplication(sys.argv)
w = QWidget()
w.setGeometry(50,50,1000,500)
w.setWindowTitle("My First GUI")
w.setWindowIcon(QIcon("email.png"))
w.show()
sys.exit(app.exec_())

print(sys.path)