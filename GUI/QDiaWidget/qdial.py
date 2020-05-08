import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDial, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont 

class Demo(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("QDial Demo")
		self.setGeometry(300, 300, 500, 500)

		self.dial = QDial()
		self.dial.setMaximum(100)
		self.dial.setMinimum(0)
		self.dial.setValue(0)
		self.dial.valueChanged.connect(self.print_dial_value)

		self.label = QLabel("Dial Value is " + str(self.dial.value()))
		self.label.setFont(QFont("Open Sans", 20))

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.dial)
		self.layout.addWidget(self.label)

		self.setLayout(self.layout)

	def print_dial_value(self):
		self.label.setText("Dial Value is " + str(self.dial.value()))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())