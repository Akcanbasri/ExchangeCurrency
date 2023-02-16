import sys
from PyQt5.QtWidgets import *


class Pencere(QWidget):
    def __init__(self):
        super(Pencere, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.radio_yazi = QLabel("Hangi dili daha çok seviyorsun")
        self.java = QRadioButton("Java")
        self.python = QRadioButton("Python")
        self.Php = QRadioButton("Php")

        self.yazi_alani = QLabel("")
        self.buton = QPushButton("Gönder")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radio_yazi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.Php)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.setWindowTitle("Radio Button ")

        self.buton.clicked.connect(
            lambda: self.clicked(self.java.isChecked(), self.python.isChecked(), self.Php.isChecked(), self.yazi_alani))
        self.show()

    def clicked(self, java, python, php, yazi_alani):
        if python:
            yazi_alani.setText("Python Seçildi")
        if java:
            yazi_alani.setText("java Seçildi")
        if php:
            yazi_alani.setText("php Seçildi")



app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
