import sys 
from PyQt5 import QtWidgets, QtGui

class AppDemo(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.resize(300, 200)

		fnt = QtGui.QFont("Open Sans", 12)

		mainLayout = QtWidgets.QVBoxLayout()

		# input field
		self.input = QtWidgets.QLineEdit()
		self.input.setFixedHeight(50)
		self.input.setFont(fnt)
		self.input.editingFinished.connect(self.addEntry)
		mainLayout.addWidget(self.input)

		self.model = QtGui.QStandardItemModel()
		completer = QtWidgets.QCompleter(self.model, self)
		self.input.setCompleter(completer)

		self.console = QtWidgets.QTextEdit()
		self.console.setFont(fnt)
		mainLayout.addWidget(self.console)

		self.setLayout(mainLayout)

	def addEntry(self):
		entryItem = self.input.text()
		self.input.clear()
		self.console.append(entryItem)

		if not self.model.findItems(entryItem):
			self.model.appendRow(QtGui.QStandardItem(entryItem))


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	demo = AppDemo()
	demo.show()

	sys.exit(app.exec_())