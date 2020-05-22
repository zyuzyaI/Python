import sys
import requests
from PyQt5 import QtWidgets, QtGui

if __name__ == "__main__":
	url_image = "https://udemy-images.udemy.com/course/750x422/507888_17b7_2.jpg"

	app = QtWidgets.QApplication(sys.argv)

	image = QtGui.QImage()
	image.loadFromData(requests.get(url_image).content)

	image_label = QtWidgets.QLabel()
	image_label.setPixmap(QtGui.QPixmap(image))
	image_label.show()

	sys.exit(app.exec_())