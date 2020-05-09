import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction

class CreateMenuBar(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Menu Bar Demo")
		self.resize(600, 500)

		self.menuBar = self.menuBar()

		fileMenu = self.menuBar.addMenu("File")
		editMenu = self.menuBar.addMenu("Edit")
		undoDeleteMenu = editMenu.addMenu("Undo delete")

		helpMenu = self.menuBar.addMenu("Help")

		exit_action = QAction("Exit App", self)
		exit_action.setShortcut("Ctrl+Q")
		exit_action.triggered.connect(lambda: QApplication.quit())

		fileMenu.addAction(exit_action)

		yes_action = QAction("Yes", self)
		no_action = QAction("No", self)
		undoDeleteMenu.addAction(yes_action)
		undoDeleteMenu.addAction(no_action)

if __name__ == "__main__":
	app = QApplication(sys.argv)

	demo = CreateMenuBar()
	demo.show()

	sys.exit(app.exec_())