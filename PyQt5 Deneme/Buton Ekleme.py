from PyQt5 import QtWidgets
import sys


def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Deneme 2")

    button = QtWidgets.QPushButton(pencere)
    button.setText("Burası bir butondur")
    button.move(190, 80)

    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("Merhaba DÜnya")
    etiket.move(200, 30)

    pencere.setGeometry(100, 100, 500, 500)
    pencere.show()
    sys.exit(app.exec_())


Pencere()
