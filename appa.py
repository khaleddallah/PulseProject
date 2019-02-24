# Main File of Project

import sys
import datetime
from PyQt5.QtCore import pyqtSlot, Qt

from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtWidgets import QStackedWidget, QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtGui import QIntValidator, QPixmap

from PyQt5.uic import loadUi

from funktions2 import *

#========================================================================================================================
class Main(QStackedWidget,funktions):
	def __init__(self):
		super().__init__()
		funktions.ConnectToDB(r"./database3.db")
		loadUi('s1.ui',self)
		self.loadMain()
		self.setButtonsFunc()

		#change background
		# pixmap = QPixmap('image.jpg')
		# self.setPixmap(pixmap)
		


	#============================================================================ config all buttons
	# when we set button to run func more one time , it run the func mort one time
	# so we will make one function for set functions for all buttons
	#تهيئة جميع الأزرار في جميع الصفحات  ليقومو بالمهام الخاصة بهم
	def setButtonsFunc(self):
		### 0
		self.PatientsDB0.clicked.connect(self.loadPatientsDB)
		self.PulseRecording0.clicked.connect(self.loadPulseRecordingC)
		self.MedicalImagesProcessing0.clicked.connect(self.loadMedImgProcessingCF)

		### 1
		#self.Back1.clicked.connect(lambda:self.setCurrentIndex(0))
		self.Back1.clicked.connect(self.loadMain)
		self.Add1.clicked.connect(self.loadNewPatient)
		self.Details1.clicked.connect(self.loadViewPatient)
		self.AllPatients1.clicked.connect(self.AllPatients)
		self.AddMedicalImage1.clicked.connect(self.loadAddMedImg)
		self.SearchByName1.clicked.connect(self.SearchBN1)
		self.SearchById1.clicked.connect(self.SearchBID1)
		self.Delete1.clicked.connect(self.deleteSelected)

		#Table config TableWidget1
		#resize table header to fit the word of fields
		self.tableWidget1.resizeColumnsToContents()
		#to make user able to select complete row by click any where of it 
		self.tableWidget1.setSelectionBehavior(QAbstractItemView.SelectRows)

		#Table config MedicalImageTable5
		#resize table header to fit the word of fields
		self.MedicalImageTable5.resizeColumnsToContents()
		#to make user able to select complete row by click any where of it 
		self.MedicalImageTable5.setSelectionBehavior(QAbstractItemView.SelectRows)

		#Table config Records_table_5
		#resize table header to fit the word of fields
		self.Records_table_5.resizeColumnsToContents()
		#to make user able to select complete row by click any where of it 
		self.Records_table_5.setSelectionBehavior(QAbstractItemView.SelectRows)

		#Table config MedicalImageTable7
		#resize table header to fit the word of fields
		self.MedicalImageTable7.resizeColumnsToContents()
		#to make user able to select complete row by click any where of it 
		self.MedicalImageTable7.setSelectionBehavior(QAbstractItemView.SelectRows)

		#Table config PatientTable7
		#resize table header to fit the word of fields
		self.PatientTable7.resizeColumnsToContents()
		#to make user able to select complete row by click any where of it 
		self.PatientTable7.setSelectionBehavior(QAbstractItemView.SelectRows)

		#Table config tableWidget9
		#resize table header to fit the word of fields
		self.tableWidget9.resizeColumnsToContents()
		#to make user able to select complete row by click any where of it 
		self.tableWidget9.setSelectionBehavior(QAbstractItemView.SelectRows)



		#To allow only int
		self.onlyInt = QIntValidator()
		self.IdBox1.setValidator(self.onlyInt)



		### 2
		self.Back2.clicked.connect(self.loadPatientsDB)
		self.Main2.clicked.connect(self.loadMain)
		self.Add2.clicked.connect(self.AddToPatientsTableDB)

		### 3
		self.Back3.clicked.connect(self.loadNewPatient)
		self.Main3.clicked.connect(self.loadMain)
		self.PatientDB3.clicked.connect(self.loadPatientsDB)

		### 4
		self.Back4.clicked.connect(self.loadNewPatient)
		self.Main4.clicked.connect(self.loadMain)
		self.PatientDB4.clicked.connect(self.loadPatientsDB)


		### 5
		self.Back5.clicked.connect(self.loadPatientsDB)
		self.Main5.clicked.connect(self.loadMain)

		### 6
		self.Back6.clicked.connect(self.loadPatientsDB)
		self.Main6.clicked.connect(self.loadMain)
		self.ChooseImageButton6.clicked.connect(self.setImage6)
		self.AddImg6.clicked.connect(self.AddImgDB)

		### 7
		self.Back7.clicked.connect(self.loadMain)
		self.Next7.clicked.connect(self.loadMedImgProcessingM)
		self.SearchByName7.clicked.connect(self.SearchBN7)
		self.SearchById7.clicked.connect(self.SearchBID7)

		self.PatientTable7.cellClicked.connect(self.SetImgData7)


		#To allow only int
		self.onlyInt = QIntValidator()
		self.IdBox7.setValidator(self.onlyInt)

		### 8
		self.Back8.clicked.connect(self.loadMedImgProcessingCF)
		self.Main8.clicked.connect(self.loadMain)

		### 9
		self.Back9.clicked.connect(self.loadMain)
		self.Next9.clicked.connect(self.loadPulseRecordingM)
		self.SearchByName9.clicked.connect(self.SearchBN9)
		self.SearchById9.clicked.connect(self.SearchBID9)


		#To allow only int
		self.onlyInt = QIntValidator()
		self.IdBox9.setValidator(self.onlyInt)


		### 10
		self.Back10.clicked.connect(self.loadPulseRecordingC)
		self.Main10.clicked.connect(self.loadMain)

		### 12
		self.Main12.clicked.connect(self.loadMain)
		self.CFhard12.clicked.connect(self.setImage12)
		self.CFpat12.clicked.connect(self.loadMedImgProcessingC)
	#============================================================================ 0
	def loadMain(self):
		#self.setStyleSheet("background-image: url(image.jpg);")
		self.setCurrentIndex(0)

	#============================================================================ 1
	def loadPatientsDB(self):
		self.tableWidget1.setRowCount(0)
		for i in [self.IdBox1,self.FirstNameBox1,self.LastNameBox1]:
			i.setText('')

		#self.setStyleSheet("background-image: url(image2.png);")
		self.setCurrentIndex(1)

	def SearchBID1(self):
		self.SearchById(self.IdBox1,self.tableWidget1,self.FirstNameBox1,self.LastNameBox1)

	def SearchById(self,IDBox,tableWidget,FirstNameBox,LastNameBox):
		FirstNameBox.setText('')
		LastNameBox.setText('')
		print('...searchByID Running')
		try:
			patId=int(IDBox.text())
		except:
			pass
		data=funktions.sucheID(patId)
		self.insertMultiRowInPatientsTable(data,tableWidget)

	def SearchBN1(self):
		self.SearchByName(self.FirstNameBox1,self.LastNameBox1,self.tableWidget1,self.IdBox1)

	def SearchByName(self,FirstNameBox,LastNameBox,tableWidget,IdBox):
		IdBox.setText('')
		print('...searchByName Running')
		firstName=FirstNameBox.text()
		lastName=LastNameBox.text()
		data=funktions.sucheName(firstName,lastName)
		self.insertMultiRowInPatientsTable(data,tableWidget)

	#get all patients from database and put them in table 
	def AllPatients(self):
		data=funktions.AllPatientDB()
		self.insertMultiRowInPatientsTable(data,self.tableWidget1)

	# in: list of rows data || out: put the rows data in tableWidget 
	def insertMultiRowInPatientsTable (self,m,table):
		print(m)
		table.setRowCount(0)
		for i in m:
			print('i = ',i)
			self.insertOneRowInPatientsTable(list(i),table)
	
	# in: one row data of table || out: put data of one row in a row of table 
	def insertOneRowInPatientsTable (self,x,table):
		print(x)
		numRows = table.rowCount()
		table.insertRow(numRows)
		for i in range(len(x)):
			table.setItem(numRows,i,QTableWidgetItem(str(x[i])))
		# self.tableWidget1.setItem(numRows,0, QTableWidgetItem(' '+str(x[0]))) #id
		# self.tableWidget1.setItem(numRows,1, QTableWidgetItem(x[1])) #first
		# self.tableWidget1.setItem(numRows,2, QTableWidgetItem(x[2])) #last
		# self.tableWidget1.setItem(numRows,3, QTableWidgetItem(x[3])) #father
		# self.tableWidget1.setItem(numRows,4, QTableWidgetItem(x[4])) #lastVisit

	# 
	def deleteSelected (self):
		#get the the index of selected row
		x=self.tableWidget1.currentRow()

		#get the Id of selected row || and get it to delete function "loschen"
		y=self.tableWidget1.item(x,0).text()
		funktions.loschen(y)

		#remove row from tableWidget
		self.tableWidget1.removeRow(x)


	#============================================================================ 2
	def loadNewPatient(self):
		self.setCurrentIndex(2)

	#Add new patient to DB 
	def AddToPatientsTableDB(self):
		# fill the id of the new patient with max id in table plus 1
		patId=funktions.MaxIdPatientsTable()+1

		# fill the rest of data of the new patient
		firstName=self.FirstNameBox2.text()
		lastName=self.LastNameBox2.text()
		father=self.FatherNameBox2.text()						
		BirthDate=self.BirthDateBox2.text()

		# reset text Boxes
		self.FirstNameBox2.setText('')
		self.LastNameBox2.setText('')
		self.FatherNameBox2.setText('')
		self.BirthDateBox2.setText('')

		# put data in Data List and pass it to neuPat funktion to add patient to DB
		Data=[patId,firstName,lastName,father,BirthDate]
		funktions.neuPat(Data)

		# if all thing right, display success window
		self.loadNewPatientS()
		# if there is any wrong, display Error window 
		#self.loadNewPatientE()

	#============================================================================ 3
	def loadNewPatientS(self):
		self.setCurrentIndex(3)

	#============================================================================ 4
	def loadNewPatientE(self):
		self.setCurrentIndex(4)

	#============================================================================ 5
	#set right data and load page 

	# in:selected row || out:Pat Id of selected row
	def get_selected_id(self,table,x):
		y=table.item(x,0).text()
		try:
			patId=int(y)
		except Exception as e:
			print("... ",e)
		return(patId)

	def loadViewPatient(self):
		#get index of selected row (x)
		x=self.tableWidget1.currentRow()

		if (x<0):
			self.errorIfNoSelect()
		else:
			patId=self.get_selected_id(self.tableWidget1,x)
			self.setPatData(patId,self.Id_value5,self.Full_Name_value5,self.Birth_value5)
			self.setImgData(patId,self.MedicalImageTable5)
			self.setPulData(patId,self.Records_table_5)
			self.setCurrentIndex(5)


	# set patient Data in page
	def setPatData(self,patId,idV,fullnameV,BirthV):
		#get data from DB
		data=funktions.sucheID(patId)[0]

		#set the data to the view_detail page
		idV.setText(str(data[0]))
		FullName=str(data[1]+" "+data[2])
		fullnameV.setText(FullName)
		BirthV.setText(data[4])

	#set list of medical images
	def setImgData(self,patId,table):
		imgData=funktions.AllMedicalImg(str(patId))
		self.insertMultiRowInPatientsTable(imgData,table)

	#set list of pulse records
	def setPulData(self,patId,table):
		sigData=funktions.AllSignals(str(patId))
		self.insertMultiRowInPatientsTable(sigData,table)

	def errorIfNoSelect(self):
		self.msgCreator()c
		self.msg.label.setText('You have to select patient to view details')



	#============================================================================ 6
	def loadAddMedImg(self):
		x=self.tableWidget1.currentRow()
		if (x<0):
			self.errorIfNoSelect()
		else:
			self.patId=self.get_selected_id(self.tableWidget1,x)
			self.setPatData(self.patId,self.Id_value5,self.Full_Name_value6,self.BirthDateValue6)
			self.setCurrentIndex(6)

	
	def setImage6(self):
		fileName=self.setImage(self.graphicsView6)
		self.ImageNameValue6.setText(fileName.split('/')[-1])
		self.ImagePathValue6.setText('/'.join(fileName.split('/')[:-1]))

	def setImage(self,graphview):
		fileName,_ = QFileDialog.getOpenFileName(None,"Select Image","","Image Files (*.png *.jpg *.jpeg *.bmp")
		if fileName:
			pixmap0 = QPixmap(fileName)
			pixmap0 = pixmap0.scaled(graphview.width(), graphview.height(), Qt.KeepAspectRatio)
			graphview.setPixmap(pixmap0)
			graphview.setAlignment(Qt.AlignCenter)
			return(fileName)

	def AddImgDB(self):
		nowDate=datetime.date.today().isoformat()
		print(nowDate)
		Data=[str(self.patId), self.ImgTypeCombo6.currentText(), nowDate, self.ImagePathValue6.text()]
		print(Data)
		funktions.neuImg(Data)


	#============================================================================ 9
	def loadPulseRecordingC(self):
		self.tableWidget9.setRowCount(0)
		for i in [self.IdBox9,self.FirstNameBox9,self.LastNameBox9]:
			i.setText('')
			
		self.setCurrentIndex(10)

	def SearchBID9(self):
		self.SearchById(self.IdBox9,self.tableWidget9,self.FirstNameBox9,self.LastNameBox9)

	def SearchBN9(self):
		self.SearchByName(self.FirstNameBox9,self.LastNameBox9,self.tableWidget9,self.IdBox9)



	#============================================================================ 10
	def loadPulseRecordingM(self):
		x=self.tableWidget9.currentRow()
		if (x<0):
			self.errorIfNoSelect()
		else:
			self.patId=self.get_selected_id(self.tableWidget9,x)
			self.setPatData(self.patId,self.Id10,self.Full_Name_value10,self.Birth_value10)
			self.setCurrentIndex(11)




	#============================================================================ 7
	def loadMedImgProcessingC(self):
		self.MedicalImageTable7.setRowCount(0)
		self.PatientTable7.setRowCount(0)
		for i in [self.IdBox7,self.FirstNameBox7,self.LastNameBox7]:
			i.setText('')
		self.setCurrentIndex(7)

	def SearchBID7(self):
		self.SearchById(self.IdBox7,self.PatientTable7,self.FirstNameBox7,self.LastNameBox7)

	def SearchBN7(self):
		self.SearchByName(self.FirstNameBox7,self.LastNameBox7,self.PatientTable7,self.IdBox7)

	def SetImgData7(self):
		x=self.PatientTable7.currentRow()
		id7=self.get_selected_id(self.PatientTable7,x)	
		self.setImgData(id7,self.MedicalImageTable7)

	#============================================================================ 8
	def loadMedImgProcessingM(self):
		self.setCurrentIndex(9)

	#============================================================================ 12
	def loadMedImgProcessingCF(self):
		self.setCurrentIndex(8)


	#choose image from hard disk
	def setImage12(self):
		fileName=self.setImage(self.graphicsViewO8)
		if fileName:
			self.loadMedImgProcessingM()


	#==========================================================================
	#==========================================================================
	
	def msgCreator(self):
		# Try to use self.msg (which is empty msg window ) if not exist (create it) 
		try:
			self.msg.show()
		except:
			self.msg = QWidget()
			loadUi('s3.ui',self.msg)
			self.msg.closeButton.clicked.connect(self.msg.close)
			self.msg.show()


#إنشاء main و اسناده إلى name 
if __name__=="__main__":
	app=QApplication(sys.argv)
	w1=Main()
	w1.show()
	sys.exit(app.exec_())

