# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created: Sat Jan 12 20:38:03 2019
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self,Patients_DB,Medical_Images_Processing,Pulse_Recording,QMW):
        self.Patients_DB_UI=Patients_DB
        self.Medical_Images_Processing_UI=Medical_Images_Processing
        self.Pulse_Recording_UI=Pulse_Recording
        self.QMW=QMW


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Patients_DB = QtWidgets.QPushButton(self.centralwidget)
        self.Patients_DB.setEnabled(True)
        self.Patients_DB.setGeometry(QtCore.QRect(130, 50, 211, 41))
        self.Patients_DB.setObjectName("Patients_DB")
       
        self.Medical_Images_Processing = QtWidgets.QPushButton(self.centralwidget)
        self.Medical_Images_Processing.setEnabled(True)
        self.Medical_Images_Processing.setGeometry(QtCore.QRect(130, 130, 211, 41))
        self.Medical_Images_Processing.setObjectName("Medical_Images_Processing")
       
        self.Pulse_Recording = QtWidgets.QPushButton(self.centralwidget)
        self.Pulse_Recording.setEnabled(True)
        self.Pulse_Recording.setGeometry(QtCore.QRect(130, 210, 211, 41))
        self.Pulse_Recording.setObjectName("Pulse_Recording")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # Execute Transition when click on the buttons
        self.Patients_DB.clicked.connect(self.goto_PatientDB)
        self.Medical_Images_Processing.clicked.connect(self.goto_Medical_Images_Processing)
        self.Pulse_Recording.clicked.connect(self.goto_Pulse_Recording)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Patients_DB.setText(_translate("MainWindow", "Patients DB"))
        self.Medical_Images_Processing.setText(_translate("MainWindow", "Medical Images Processing"))
        self.Pulse_Recording.setText(_translate("MainWindow", "Pulse Recording"))

    # Change to Patients DB window
    # def ChangeToPatientDB (self):
    #     self.ui = self.Patients_DB0
    #     self.ui.setupUi(self.QMW)
    #     self.QMW.show()
    #     self.centralwidget.hide()



    # general change function
    def gotoWin (self,ui):
        # self.centralwidget.hide()
        # self.QMW.hide()

        # self.QMW.hide()
        # self.QMW=QtWidgets.QWidget()
        # ui.setupUi(self.QMW)
        # self.QMW.show()

        self.QMW.hide()
        self.QMW=QtWidgets.QMainWindow()
        ui.setupUi(self.QMW)
        self.QMW.show()





    # Change to Patients_DB window 
    def goto_PatientDB (self):
        self.gotoWin(self.Patients_DB_UI)


    # Change to Medical_Images_Processing window
    def goto_Medical_Images_Processing (self):
        self.gotoWin(self.Medical_Images_Processing_UI)



    # Change to Pulse_Recording window
    def goto_Pulse_Recording (self):
        self.gotoWin(self.Pulse_Recording_UI)






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

