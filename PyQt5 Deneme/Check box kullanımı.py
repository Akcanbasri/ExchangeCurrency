import sys
from PyQt5.QtWidgets import *


class Pencere(QWidget):
    def __init__(self):
        super(Pencere, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.check_box = QCheckBox("Pythonu seviyor musunuz?")
        self.yazi_alanı = QLabel("")
        self.buton = QPushButton("Bana tıkla")

        v_box = QVBoxLayout()
        v_box.addWidget(self.check_box)
        v_box.addWidget(self.yazi_alanı)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.setWindowTitle("Check Box")

        self.buton.clicked.connect(lambda: self.click(self.check_box.isChecked(), self.yazi_alanı))
        self.show()


    def click(self, check_box, yazi_alanı):
        if check_box:
            yazi_alanı.setText("Harika......")
        else:
            yazi_alanı.setText("Neden ???")


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
