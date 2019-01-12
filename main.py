from gui.main_gui import *
from gui.Patients_DB import *
import sys


class main0:
	def main(self):
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()

		Patients_DB=Ui_Patients_DB()
		ui = Ui_MainWindow(Patients_DB,Patients_DB,Patients_DB,MainWindow)

		ui.setupUi(MainWindow)
		MainWindow.show()
		sys.exit(app.exec_())


if __name__ == "__main__":
	main0=main0()
	main0.main()