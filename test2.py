import sys
from PyQt5.QtCore import pyqtSlot 
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.uic import loadUi


class LC2(QWidget):
	def __init__(self):
		super().__init__()
		loadUi('Patients_DB.ui',self)


class LC(QMainWindow):
	def __init__(self):
		super().__init__()
		loadUi('main_gui.ui',self)
		self.Patients_DB.clicked.connect(self.goto_PatientDB)

	@pyqtSlot()
	def goto_PatientDB (self):
		LC2_run()
		# self.window=LC2()
		# widget2=LC2()
		# widget2.show()

		# self.hide()
		# while self.count() > 0:
		# 	self.itemAt(0).setParent(None)		
		# loadUi('Patients_DB.ui',self)
		# self.show()

def LC_run():
	widget=LC()
	widget.show()

def LC2_run():
	widget=LC2()
	widget.show()



app=QApplication(sys.argv)
LC_run()
sys.exit(app.exec_())