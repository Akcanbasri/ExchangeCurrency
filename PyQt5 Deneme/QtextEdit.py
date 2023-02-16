import sys
from PyQt5.QtWidgets import *


class Pencere(QWidget):
    def __init__(self):
        super(Pencere, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.yazi_alanı = QTextEdit()
        self.temizle = QPushButton("temizle")

        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi_alanı)
        v_box.addWidget(self.temizle)
        self.setWindowTitle("Qtext Edit")
        self.setLayout(v_box)

        self.temizle.clicked.connect(self.temzileyici)
        self.show()

    def temzileyici(self):
        self.yazi_alanı.clear()


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
