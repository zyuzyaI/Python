import sys 
from PyQt5 import QtWidgets, QtCore, QtGui

class ImageLabel(QtWidgets.QLabel):
	def __init__(self):
		super().__init__()

		self.setAlignment(QtCore.Qt.AlignCenter)
		self.setText("\n\n Drop Image Here \n\n")
		self.setStyleSheet("""
			QLabel{
				border: 4px dashed #aaa
			}
			""")

	def setPixmap(self, image):
		super().setPixmap(image)

class MyApp(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.resize(400, 300)
		self.setAcceptDrops(True)

		mainLayout = QtWidgets.QVBoxLayout()

		self.photoViewer = ImageLabel()
		mainLayout.addWidget(self.photoViewer)


		self.setLayout(mainLayout)

	def dragEnterEvent(self, event):
		if event.mimeData().hasImage:
			event.accept()
		else:
			event.ignore()

	def dragMoveEvent(self, event):
		if event.mimeData().hasImage:
			event.accept()
		else:
			event.ignore()

	def dropEvent(self, event):
		if event.mimeData().hasImage:
			event.setDropAction(QtCore.Qt.CopyAction)
			filePath = event.mimeData().urls()[0].toLocalFile()
			self.setImage(filePath)

			event.accept()
		else:
			event.ignore()
		
	def setImage(self, imagePath):
		self.photoViewer.setPixmap(QtGui.QPixmap(imagePath))

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	demo = MyApp()
	demo.show()

	sys.exit(app.exec_())