import sys
from PyQt5.QtWidgets import *
import os


class Pencere(QWidget):
    def __init__(self):
        super(Pencere, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.yazi_alanı = QTextEdit()
        self.temizle = QPushButton("Clear")
        self.dosya_ac = QPushButton("Open")
        self.kaydet = QPushButton("Save")

        h_box = QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.dosya_ac)
        h_box.addWidget(self.kaydet)

        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi_alanı)
        v_box.addLayout(h_box)

        self.setWindowTitle("NotePad Basic")
        self.setLayout(v_box)

        self.temizle.clicked.connect(self.temizlendi)
        self.dosya_ac.clicked.connect(self.acildi)
        self.kaydet.clicked.connect(self.kaydedici)

        self.show()

    def temizlendi(self):
        self.yazi_alanı.clear()

    def acildi(self):
        dosya_ismi = QFileDialog.getOpenFileName(self, "Dosya Ac", os.getenv("Home"))
        with open(dosya_ismi[0], "r", encoding="utf-8") as file:
            self.yazi_alanı.setText(file.read())

    def kaydedici(self):
        dosya_ismi = QFileDialog.getSaveFileName(self, "Dosya Kaydet", os.getenv("Home"))
        with open(dosya_ismi[0], "w", encoding="utf-8") as file:
            file.write(self.yazi_alanı.toPlainText())


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
