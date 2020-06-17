import sys
from PyQt5 import QtWidgets, QtCore

class Table(QtWidgets.QTableWidget):
	def __init__(self):
		super().__init__(1,5)
		self.setHorizontalHeaderLabels(list("ABCDE"))
		self.verticalHeader().setDefaultSectionSize(50)
		self.horizontalHeader().setDefaultSectionSize(150)
		self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

	def _addRow(self):
		rowCount = self.rowCount()
		self.insertRow(rowCount)

	def _removeRow(self):
		if self.rowCount() > 0:
			self.removeRow(self.rowCount()-1) 

	def _copyRow(self):
		self.insertRow(self.rowCount())
		rowCount = self.rowCount()
		columnCount = self.columnCount()

		for j in range(columnCount):
			if not self.item(rowCount-2, j) is None:
				self.setItem(rowCount-1, j, QtWidgets.QTableWidgetItem(self.item(
					rowCount-2,j).text()))

class AppDemo(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.resize(1000, 600)

		mainLayout = QtWidgets.QHBoxLayout()

		table = Table()
		mainLayout.addWidget(table)

		buttonLayout = QtWidgets.QVBoxLayout()

		buttonNew = QtWidgets.QPushButton("New")
		buttonNew.clicked.connect(table._addRow)
		buttonLayout.addWidget(buttonNew)

		buttonCopy = QtWidgets.QPushButton("Copy")
		buttonCopy.clicked.connect(table._copyRow)
		buttonLayout.addWidget(buttonCopy)

		buttonRemove = QtWidgets.QPushButton("Remove")
		buttonRemove.clicked.connect(table._removeRow)
		buttonLayout.addWidget(buttonRemove, alignment=QtCore.Qt.AlignTop)


		mainLayout.addLayout(buttonLayout)
		self.setLayout(mainLayout)

if __name__ == "__main__":
	app =QtWidgets.QApplication(sys.argv)

	app.setStyleSheet('QPushButton{font-size: 20px; width: 200px; height: 50px}') 

	demo = AppDemo()
	demo.show()

	sys.exit(app.exec_())
