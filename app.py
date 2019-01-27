import sys
from PyQt5.QtCore import pyqtSlot 
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.uic import loadUi

##########################################################
class Main(QWidget):
	def __init__(self):
		super().__init__()
		loadUi('gui/Main.ui',self)


#######################################################
class PatientsDB(QWidget):
	def __init__(self):
		super().__init__()
		loadUi('gui/PatientsDB.ui',self)

#######################################################
class PulseRecordingC(QWidget):
	def __init__(self):
		super().__init__()
		loadUi('gui/PulseRecordingC.ui',self)


#######################################################
class PulseRecordingM(QWidget):
	def __init__(self):
		super().__init__()
		loadUi('gui/PulseRecordingM.ui',self)


#######################################################

#the Object of Class will be the same name plus 'Q'
#tha Load function will be the same name of Class but in the begining 'load'
class ess():
	def __init__(self):
		self.MainQ=Main()
		self.PatientsDBQ=PatientsDB()
		self.PulseRecordingC=PulseRecordingC()
		self.PulseRecordingM=PulseRecordingM()

		self.loadMain()


	def loadMain(self):
		self.PatientsDBQ.close()
		self.MainQ.show()
		self.MainQ.PatientsDB.clicked.connect(self.loadPatientsDB)
		self.MainQ.PulseRecording.clicked.connect(self.loadPulseRecordingC)



	def loadPatientsDB(self):
		self.MainQ.close()
		self.PatientsDBQ.show()
		self.PatientsDBQ.Back.clicked.connect(self.loadMain)


	def loadPulseRecordingC(self):
		self.MainQ.close()
		self.PulseRecordingC.show()
		self.PulseRecordingC.Back.clicked.connect(self.loadMain)


	def loadPulseRecordingM(self):
		self.PulseRecordingC.close()
		self.PulseRecordingM.show()
		self.PulseRecordingM.Back.clicked.connect(self.loadMain)
		self.PulseRecordingM.Main.clicked.connect(self.loadMain)

#######################################################
#######################################################


if __name__=="__main__":
	app=QApplication(sys.argv)
	w1=ess()
	sys.exit(app.exec_())

