import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit 

class DragAndDrop(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Drag And Drop")
		self.resize(300, 150)
		self.initUI()

	def initUI(self):
		edit1 = QLineEdit("", self)
		edit1.setDragEnabled(True)
		edit1.move(20, 30)

		edit2 = QLineEdit("", self)
		edit2.setDragEnabled(False)
		edit2.move(20, 70) # left, top

		button = Button("&Button", self)
		button.move(190, 50)

class Button(QPushButton):
	def __init__(self, title, parent):
		super().__init__(title, parent)
		self.setAcceptDrops(True)

	def dragEnterEvent(self, event):
		if event.mimeData().hasFormat("text/plain"):
			event.accept()
		else:
			event.ignore()

	def dropEvent(self, event):
		print("Drop Event")
		self.setText(event.mimeData().text())

if __name__ == "__main__":
	app = QApplication(sys.argv)
	demo = DragAndDrop()
	demo.show()


	sys.exit(app.exec_())