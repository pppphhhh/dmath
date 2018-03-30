import sys

from PyQt5 import QtWidgets

from mainwin import MainWindow


app = QtWidgets.QApplication(sys.argv)

win = MainWindow()

win.show()
app.exec()

