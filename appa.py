import sys
from PyQt5.QtCore import pyqtSlot 

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow,QWidget
from PyQt5.QtWidgets import QStackedWidget,QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView,QAbstractItemView

from PyQt5.QtGui import QIntValidator

from PyQt5.uic import loadUi

from warf_files.funktions2 import *


#===========================================================================
class Main(QStackedWidget,funktions):
	def __init__(self):
		super().__init__()
		funktions.ConnectToDB(r"./warf_files/database3.db")
		loadUi('s1.ui',self)
		self.loadMain()

	#=============================== 0
	def loadMain(self):
		self.setCurrentIndex(0)
		self.PatientsDB0.clicked.connect(self.loadPatientsDB)
		self.PulseRecording0.clicked.connect(self.loadPulseRecordingC)
		self.MedicalImagesProcessing0.clicked.connect(self.loadMedImgProcessingC)

	#=============================== 1
	def loadPatientsDB(self):
		self.setCurrentIndex(1)
		
		#Going to another Ui
		self.Back1.clicked.connect(self.loadMain)
		self.Add1.clicked.connect(self.loadNewPatient)
		self.View1.clicked.connect(self.loadViewPatient)
		self.AddMedicalImage1.clicked.connect(self.loadAddMedImg)

		#Search button (get the first name and last name fields)
		self.Search1.clicked.connect(self.SearchByName)
		self.SearchById1.clicked.connect(self.SearchById)

		#self.Delete1.clicked.connect(self.insertInPatientsTableWidget)

		#Table config
		#resize table header to fit the word of fields
		self.tableWidget1.resizeColumnsToContents()
		#to make user able to select complete row by click any where of it 
		self.tableWidget1.setSelectionBehavior(QAbstractItemView.SelectRows)


		#To allow only int
		self.onlyInt = QIntValidator()
		self.IdBox1.setValidator(self.onlyInt)



	def SearchById(self):
		print('...searchByID Running')
		patId=int(self.IdBox1.text())
		data=funktions.sucheID(patId)
		print(data)
		self.insertMultiRowInPatientsTable(data)


	def SearchByName(self):
		print('...searchByName Running')
		firstName=self.FirstNameBox1.text()
		lastName=self.LastNameBox1.text()
		data=funktions.sucheName(firstName,lastName)
		print(data)
		self.insertMultiRowInPatientsTable(data)


	def insertMultiRowInPatientsTable (self,m):
		self.tableWidget1.setRowCount(0);
		for i in m:
			self.insertOneRowInPatientsTable(i)
		

	def insertOneRowInPatientsTable (self,x):
		numRows = self.tableWidget1.rowCount()
		self.tableWidget1.insertRow(numRows)
		self.tableWidget1.setItem(0,0, QTableWidgetItem(x[0])) #id
		self.tableWidget1.setItem(0,1, QTableWidgetItem(x[0])) #first
		self.tableWidget1.setItem(0,2, QTableWidgetItem(x[0])) #last
		self.tableWidget1.setItem(0,3, QTableWidgetItem(x[0])) #fater
		self.tableWidget1.setItem(0,4, QTableWidgetItem(x[0])) #lastVisit





	#=============================== 2
	def loadNewPatient(self):
		self.setCurrentIndex(2)
		self.Back2.clicked.connect(self.loadPatientsDB)
		self.Main2.clicked.connect(self.loadMain)
		self.Add2.clicked.connect(self.AddToPatientsTableDB)


	def AddToPatientsTableDB(self):
		patId=funktions.CountOfPatientsTable()+1
		firstName=self.FirstNameBox2.text()
		lastName=self.LastNameBox2.text()
		father=self.FatherNameBox2.text()
		BirthDate=self.BirthDateBox2.text()
		Data=[patId,firstName,lastName,father,BirthDate]
		funktions.neuPat(Data)

	#=============================== 3
	def loadNewPatientS(self):
		self.setCurrentIndex(3)
		self.Back5.clicked.connect(self.loadNewPatient)
		self.Main5.clicked.connect(self.loadMain)


	#=============================== 4
	def loadNewPatientE(self):
		self.setCurrentIndex(4)
		self.Back5.clicked.connect(self.loadNewPatient)
		self.Main5.clicked.connect(self.loadMain)


	#=============================== 5
	def loadViewPatient(self):
		self.setCurrentIndex(5)
		self.Back5.clicked.connect(self.loadPatientsDB)
		self.Main5.clicked.connect(self.loadMain)

	#=============================== 6
	def loadAddMedImg(self):
		self.setCurrentIndex(6)
		self.Back6.clicked.connect(self.loadPatientsDB)
		self.Main6.clicked.connect(self.loadMain)

	#=============================== 9
	def loadPulseRecordingC(self):
		self.setCurrentIndex(9)
		self.Back9.clicked.connect(self.loadMain)
		self.Next9.clicked.connect(self.loadPulseRecordingM)


	#=============================== 10
	def loadPulseRecordingM(self):
		self.setCurrentIndex(10)
		self.Back10.clicked.connect(self.loadPulseRecordingC)
		self.Main10.clicked.connect(self.loadMain)

	#=============================== 7
	def loadMedImgProcessingC(self):
		self.setCurrentIndex(7)
		self.Back7.clicked.connect(self.loadMain)
		self.Next7.clicked.connect(self.loadMedImgProcessingM)


	#=============================== 8
	def loadMedImgProcessingM(self):
		self.setCurrentIndex(8)
		self.Back8.clicked.connect(self.loadMedImgProcessingC)
		self.Main8.clicked.connect(self.loadMain)





if __name__=="__main__":
	app=QApplication(sys.argv)
	w1=Main()
	w1.show()
	sys.exit(app.exec_())

