import sys
from PyQt5.QtWidgets import *
import sqlite3


class Pencere(QWidget):
    def __init__(self):
        super(Pencere, self).__init__()
        self.baglanti_olustur()
        self.init_ui()

    def init_ui(self):
        self.kullanici_adi = QLineEdit()
        self.parola = QLineEdit()
        self.parola.setEchoMode(QLineEdit.Password)
        self.giris = QPushButton("Giris Yap")
        self.yazi_alani = QLabel("")

        v_box = QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Kulanici Girisi")
        self.giris.clicked.connect(self.login)
        self.show()

    def baglanti_olustur(self):
        con = sqlite3.connect("database.db")
        self.cursor = con.cursor()

        self.cursor.execute("Create Table if not exists Uyeler(kullanıcı_adı Text, parola Text)")
        con.commit()

    def login(self):
        adi = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("Select * from uyeler where kullanıcı_adı = ? and parola = ?", (adi, par))
        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("Böyle bir kullanıcı yok\n Tekrar deneyin")
        else:
            self.yazi_alani.setText("Şifreniz doğrudur. Hoşgeldiniz " + adi)


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
