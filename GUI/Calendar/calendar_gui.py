import sys 
from datetime import datetime 
import calendar 
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget 
from PyQt5.QtCore import QDate 

class CalendarDemo(QWidget):
	global currentYear, currentMonth 

	currentYear = datetime.now().year
	currentMonth = datetime.now().month 

	def __init__(self):
		super().__init__()
		self.setWindowTitle("Calendar PyQt5 & Python")
		self.setGeometry(300, 300, 450, 300)
		self.initUI()

	def initUI(self):
		self.calendar = QCalendarWidget(self)
		self.calendar.move(20, 20)
		self.calendar.setGridVisible(True)

		self.calendar.setMinimumDate(QDate(currentYear, currentMonth - 1, 1))
		self.calendar.setMaximumDate(QDate(currentYear, currentMonth + 1, 
				calendar.monthrange(currentYear, currentMonth)[1]))

		self.calendar.setSelectedDate(QDate(currentYear, currentMonth, 1))

		self.calendar.clicked.connect(self.printDateInfo)

	def printDateInfo(self, qDate):
		print("{0}/{1}/{2}".format(qDate.month(), qDate.day(), qDate.year()))
		print("Day Number of the year: {}".format(qDate.dayOfYear()))
		print("Day Number of the week: {}".format(qDate.dayOfWeek()))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	demo = CalendarDemo()
	demo.show()
	sys.exit(app.exec_())