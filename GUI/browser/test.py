import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
	app = QApplication(sys.argv)

	web = QWebEngineView()
	web.load(QUrl("https://www.olx.ua"))
	web.show()

	sys.exit(app.exec_())