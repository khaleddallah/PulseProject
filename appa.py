import sys
from PyQt5.QtCore import pyqtSlot 
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QStackedWidget,QTableWidgetItem
from PyQt5.uic import loadUi
#from DBfunctions import *

class Main(QStackedWidget):
# class Main(QStackedWidget,DBMain):
	def __init__(self):
		super().__init__()
		loadUi('s1.ui',self)
		self.loadMain()

	#0
	def loadMain(self):
		self.setCurrentIndex(0)
		self.PatientsDB0.clicked.connect(self.loadPatientsDB)
		self.PulseRecording0.clicked.connect(self.loadPulseRecordingC)
		self.MedicalImagesProcessing0.clicked.connect(self.loadMedImgProcessingC)

	#1h
	def loadPatientsDB(self):
		self.setCurrentIndex(1)
		
		#Going to another Ui
		self.Back1.clicked.connect(self.loadMain)
		self.Add1.clicked.connect(self.loadNewPatient)
		self.View1.clicked.connect(self.loadViewPatient)
		self.AddMedicalImage1.clicked.connect(self.loadAddMedImg)

		#Search button (get the first name and last name fields)
		self.Search1.clicked.connect(self.SearchF1)
		self.Delete1.clicked.connect(self.insertInTable)

		#Table config



	def SearchF1(self):
		fn1=self.FirstNameBox1.text()
		ln1=self.LastNameBox1.text()
		print(fn1+' '+ln1)

	def insertInTable (self):
		numRows = self.tableWidget1.rowCount()
		self.tableWidget1.insertRow(numRows)

		self.tableWidget1.setItem(0,0, QTableWidgetItem("1"))
		self.tableWidget1.setItem(0,1, QTableWidgetItem("Khaled"))
		self.tableWidget1.setItem(0,2, QTableWidgetItem("Dallah"))
		self.tableWidget1.setItem(0,3, QTableWidgetItem("EzzAlden"))
		self.tableWidget1.setItem(0,4, QTableWidgetItem("12-2-2019"))


	#2
	def loadNewPatient(self):
		self.setCurrentIndex(2)
		self.Back2.clicked.connect(self.loadPatientsDB)
		self.Main2.clicked.connect(self.loadMain)

	#3
	def loadNewPatientS(self):
		self.setCurrentIndex(3)
		self.Back5.clicked.connect(self.loadNewPatient)
		self.Main5.clicked.connect(self.loadMain)


	#4
	def loadNewPatientE(self):
		self.setCurrentIndex(4)
		self.Back5.clicked.connect(self.loadNewPatient)
		self.Main5.clicked.connect(self.loadMain)


	#5
	def loadViewPatient(self):
		self.setCurrentIndex(5)
		self.Back5.clicked.connect(self.loadPatientsDB)
		self.Main5.clicked.connect(self.loadMain)

	#6
	def loadAddMedImg(self):
		self.setCurrentIndex(6)
		self.Back6.clicked.connect(self.loadPatientsDB)
		self.Main6.clicked.connect(self.loadMain)

	#9
	def loadPulseRecordingC(self):
		self.setCurrentIndex(9)
		self.Back9.clicked.connect(self.loadMain)
		self.Next9.clicked.connect(self.loadPulseRecordingM)


	#10
	def loadPulseRecordingM(self):
		self.setCurrentIndex(10)
		self.Back10.clicked.connect(self.loadPulseRecordingC)
		self.Main10.clicked.connect(self.loadMain)

	#7
	def loadMedImgProcessingC(self):
		self.setCurrentIndex(7)
		self.Back7.clicked.connect(self.loadMain)
		self.Next7.clicked.connect(self.loadMedImgProcessingM)


	#8
	def loadMedImgProcessingM(self):
		self.setCurrentIndex(8)
		self.Back8.clicked.connect(self.loadMedImgProcessingC)
		self.Main8.clicked.connect(self.loadMain)





if __name__=="__main__":
	app=QApplication(sys.argv)
	w1=Main()
	w1.show()
	sys.exit(app.exec_())

