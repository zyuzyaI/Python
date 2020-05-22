import sys 
from PyQt5 import QtWidgets

class MenuItemsButton(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Menu Items Button")
		self.resize(400, 300)

		data_seasons = [
			{"summer": ["June", "July", "August"]},
			{"autumn": ["September", "October", "November"]},
			{"winter": ["December", "January", "February"]},
			{"spring": ["March", "April", "May"]},
			"Weather"
		]

		btn = QtWidgets.QPushButton("Click Me", self)
		btn.setStyleSheet("""font-size:25px;""")
		btn.move(50, 50)
		btn.resize(150,100)

		# set menu to button
		menu = QtWidgets.QMenu()
		menu.triggered.connect(lambda x: print(x.text()))
		btn.setMenu(menu)

		self.addMenu(data_seasons, menu)

	def addMenu(self, data, menuObj):
		if isinstance(data, dict):
			for k, v in data.items():
				subMenu = QtWidgets.QMenu(k, menuObj)
				menuObj.addMenu(subMenu)
				self.addMenu(v, subMenu)
		elif isinstance(data, list):
			for element in data:
				self.addMenu(element, menuObj)
		else:
			action = menuObj.addAction(data)
			action.setIconVisibleInMenu(False)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	demo = MenuItemsButton()
	demo.show()

	sys.exit(app.exec_())