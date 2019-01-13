from gui.main_gui import *
from gui.Patients_DB import *
from gui.PulseRecording1 import *
from gui.PulseRecording2 import *

import sys


class main0:
	def main(self):
		app = QtWidgets.QApplication(sys.argv)
		QMW = QtWidgets.QMainWindow()

		Patients_DB=Ui_Patients_DB()
		PulseRecording1=Ui_PulseRecording1()

		ui = Ui_MainWindow(Patients_DB,Patients_DB,PulseRecording1,QMW)

		ui.setupUi(QMW)
		QMW.show()
		sys.exit(app.exec_())


if __name__ == "__main__":
	main0=main0()
	main0.main()