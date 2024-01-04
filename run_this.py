from PyQt5 import QtWidgets
from run import Ui_MainWindow
import w3
import sys

adr1 = ""
pat = ""
adr2 = ""
doc = ""
work = ""
adr3 = ""
adr4 = ""
time = ""
diag = ""
ill_nam = ""

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.knopka1.clicked.connect(self.reg_pat)
        self.ui.knopka2.clicked.connect(self.reg_doc)
        self.ui.knopka3.clicked.connect(self.priem)
        self.ui.knopka4.clicked.connect(self.statistika)
        self.ui.knopka5.clicked.connect(self.spisok)

    def reg_pat(self):
        Pol = w3.poliklinika()
        adr1 = self.ui.line1.text()
        pat = self.ui.line2.text()
        Pol.patient_registration(adr1, pat)

    def reg_doc(self):
        Pol = w3.poliklinika()
        adr2 = self.ui.line3.text()
        doc = self.ui.line4.text()
        work = self.ui.line5.text()
        Pol.doctor_registration(adr2, doc, work)

    def priem(self):
        Pol = w3.poliklinika()
        adr3 = self.ui.line6.text()
        adr4 = self.ui.line7.text()
        time = self.ui.line8.text()
        diag = self.ui.line9.text()
        ill_nam = self.ui.line10.text()
        Pol.doctor_appointment(adr3, adr4, time, diag, ill_nam)

    def statistika(self):
        what_diag = self.ui.line11.text()
        t = w3.Pol.ill_statistics(what_diag)
        a = str(t)
        self.ui.print_field.setText(a)

    def spisok(self):
        special = self.ui.line12.text()
        s = ''
        mass = w3.Pol.print_info(special)
        for i in mass:
            s += i + '\n'
        self.ui.print_field.setText(s)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Main()
    myapp.show()
    sys.exit(app.exec_())
