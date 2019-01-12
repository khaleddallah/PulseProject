# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Patients_DB.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Patients_DB(object):
    def setupUi(self, Patients_DB):
        Patients_DB.setObjectName("Patients_DB")
        Patients_DB.resize(400, 300)

        self.retranslateUi(Patients_DB)
        QtCore.QMetaObject.connectSlotsByName(Patients_DB)

    def retranslateUi(self, Patients_DB):
        _translate = QtCore.QCoreApplication.translate
        Patients_DB.setWindowTitle(_translate("Patients_DB", "Patients DB"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Patients_DB = QtWidgets.QWidget()
    ui = Ui_Patients_DB()
    ui.setupUi(Patients_DB)
    Patients_DB.show()
    sys.exit(app.exec_())

