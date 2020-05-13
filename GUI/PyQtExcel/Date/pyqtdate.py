import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget
import win32com.client as win32

# xlApp = win32.Dispatch("Excel.Application")
xlApp = win32.Dispatch("Calc.Application")
xlApp.visible = True 

class DatePyQtExcel(QCalendarWidget):
	def __init__(self):
		super().__init__()
		self.clicked.connect(self.insert_date)

	def insert_date(self, date):
		# return stare value(date)
		try:
			print(date.toPyDate().strftime('%m-%d-%Y'))
			xlApp.Selection.value = date.toPyDate().strftime('%m-%d-%Y')

		except Exception as e:
			print(e)

# if __name__ == "__main_":
app =QApplication(sys.argv)

demo = DatePyQtExcel()
demo.show()

sys.exit(app.exec_())