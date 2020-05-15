import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, 
							QLineEdit, QGridLayout, QMessageBox)

class LoginFormApp(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Login Form")
		self.resize(500, 120)

		layout = QGridLayout()

		labelName = QLabel('<font size="4"> Username </font>') 
		self.lineEditUsername = QLineEdit()
		self.lineEditUsername.setPlaceholderText("Please enter your username")
		layout.addWidget(labelName, 0, 0)
		layout.addWidget(self.lineEditUsername, 0, 1)

		labelPassword = QLabel('<font size="4"> Password </font>')
		self.lineEditPassword = QLineEdit()
		self.lineEditPassword.setPlaceholderText("Please enter your password")
		layout.addWidget(labelPassword, 1, 0)
		layout.addWidget(self.lineEditPassword, 1, 1)

		buttonLogin = QPushButton("Login")
		buttonLogin.clicked.connect(self.checkPassword)
		layout.addWidget(buttonLogin, 2, 0, 1, 2)
		layout.setRowMinimumHeight(2, 75)

		self.setLayout(layout)

	def checkPassword(self):
		msg = QMessageBox()
		# print(self.lineEditUsername.text(), "  ", self.lineEditPassword.text())
		if self.lineEditUsername.text() == "username" and self.lineEditPassword.text() == "sometext":
			msg.setText("Success")
			msg.exec_()
			app.close()
		else:
			msg.setText("Incorrect")
			msg.exec_()


if __name__ == "__main__":
	app = QApplication(sys.argv)

	demo = LoginFormApp() 
	demo.show()

	sys.exit(app.exec_())