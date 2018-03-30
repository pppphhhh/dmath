import sys

from PyQt5 import QtCore, QtWidgets, uic


app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QMainWindow()
ui = uic.loadUi('mainwin.ui', win)

win.show()

app.exec()
