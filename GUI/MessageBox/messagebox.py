import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class ExempleApp(QWidget):
	def __init__(self):
		super().__init__()

	def closeEvent(self, event):
		reply = QMessageBox.question(self, "Window close", "Are you sure want to close the window?",
					QMessageBox.Yes | QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
			print("Window closed")

		else:
			event.ignore()


if __name__ == "__main__":
	app = QApplication(sys.argv)

	demo = ExempleApp()
	demo.show()

	sys.exit(app.exec_())