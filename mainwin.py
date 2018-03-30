from PyQt5 import QtWidgets, QtGui, uic

from validators import RationalValidator, PolynomValidator


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('mainwin.ui', self)

        n_validator = QtGui.QIntValidator()
        z_validator = QtGui.QIntValidator()
        q_validator = RationalValidator()
        p_validator = PolynomValidator()

        n_validator.setBottom(0)

        self.ui.line_n_n1.setValidator(n_validator)
        self.ui.line_n_n2.setValidator(n_validator)
        self.ui.line_n_k.setValidator(n_validator)

        self.ui.line_z_z1.setValidator(z_validator)
        self.ui.line_z_z2.setValidator(z_validator)

        self.ui.line_q_q1.setValidator(q_validator)
        self.ui.line_q_q2.setValidator(q_validator)
        self.ui.line_q_z.setValidator(z_validator)

        self.ui.line_p_p1.setValidator(p_validator)
        self.ui.line_p_p2.setValidator(p_validator)
        self.ui.line_p_q.setValidator(q_validator)
        self.ui.line_p_k.setValidator(n_validator)

