import sys
from PyQt5 import QtWidgets, QtGui

class DependedComboBox(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Depended Combo Box")
		self.resize(700,100)

		mainLayout = QtWidgets.QHBoxLayout()

		self.model = QtGui.QStandardItemModel()

		# seasons
		self.comboSeasons = QtWidgets.QComboBox()
		self.comboSeasons.setFixedSize(325,50)
		self.comboSeasons.setFont(QtGui.QFont("", 12))
		self.comboSeasons.setModel(self.model)

		# months
		self.comboMonths = QtWidgets.QComboBox()
		self.comboMonths.setFixedSize(325,50)
		self.comboMonths.setFont(QtGui.QFont("", 12))
		self.comboMonths.setModel(self.model)

		# add data
		for k, v in data_seasons.items():
			season = QtGui.QStandardItem(k)
			self.model.appendRow(season)
			for value in v:
				month = QtGui.QStandardItem(value)
				season.appendRow(month)

		self.comboSeasons.currentIndexChanged.connect(self.updateSeasonIndex)
		self.updateSeasonIndex(0)

		mainLayout.addWidget(self.comboSeasons)
		mainLayout.addWidget(self.comboMonths)
		self.setLayout(mainLayout)

	def updateSeasonIndex(self, index):
		indx = self.model.index(index, 0 , self.comboSeasons.rootModelIndex())
		self.comboMonths.setRootModelIndex(indx)
		self.comboMonths.setCurrentIndex(0)



data_seasons = {
			"summer": ["June", "July", "August"],
			"autumn": ["September", "October", "November"],
			"winter": ["December", "January", "February"],
			"spring": ["March", "April", "May"],
		}

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	demo = DependedComboBox()
	demo.show()

	sys.exit(app.exec_())