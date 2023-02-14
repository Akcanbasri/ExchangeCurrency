from PyQt5 import QtWidgets
import sys


def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Deneme 3")

    okey = QtWidgets.QPushButton("Onayla")
    cansel = QtWidgets.QPushButton("İptal")

    """# Horizontal layout
    h_layout = QtWidgets.QHBoxLayout()
    h_layout.addStretch()
    h_layout.addWidget(okey)
    h_layout.addWidget(cansel)"""

    """# Vertical layout
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(okey)
    v_box.addWidget(cansel)
    v_box.addStretch()"""

    # Nested Layouts
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(okey)
    h_box.addWidget(cansel)

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)

    """# horizontal layout maker
    pencere.setLayout(h_layout)

    # Vertical layout maker
    pencere.setLayout(v_box)"""

    # Nested Layout maker
    pencere.setLayout(v_box)

    pencere.setGeometry(100, 100, 500, 500)
    pencere.show()

    sys.exit(app.exec_())


Pencere()
