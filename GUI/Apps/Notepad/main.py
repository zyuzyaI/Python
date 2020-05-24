import sys, os
from PyQt5 import QtWidgets, QtGui, QtCore, QtPrintSupport 

class AppDemo(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		# self.setWindowTitle("My Notepad")
		self.setWindowIcon(QtGui.QIcon("./images/notepad.ico"))

		self.screenWidth, self.screenHeight = self.geometry().width(), self.geometry().height()
		self.resize(self.screenWidth, self.screenHeight)

		self.filterTypes = "Text Document (*.txt);; Python (*.py);; Markdown (*.md)"

		self.path = None 

		fixedFont = QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont)
		fixedFont.setPointSize(12)

		mainLayout = QtWidgets.QVBoxLayout()

		# editor
		self.editor = QtWidgets.QPlainTextEdit()
		self.editor.setFont(fixedFont)
		mainLayout.addWidget(self.editor)

		# create status bar
		self.statusBar = self.statusBar()

		# app container
		container = QtWidgets.QWidget()
		container.setLayout(mainLayout)
		self.setCentralWidget(container)

		# ----------------------------------
		# File Menus
		# ----------------------------------
		fileMenu = self.menuBar().addMenu("&File")

		# ----------------------------------
		# File Menus
		# ----------------------------------
		fileToolBar = QtWidgets.QToolBar("File")
		fileToolBar.setIconSize(QtCore.QSize(60,60))
		self.addToolBar(QtCore.Qt.BottomToolBarArea, fileToolBar)

		"""
		open, save, saveAs
		"""

		openFileAction = QtWidgets.QAction(QtGui.QIcon("./images/open_file.ico"),
											 "Open File...",
											 self)
		openFileAction.setStatusTip("Open file")
		openFileAction.setShortcut(QtGui.QKeySequence.Open)
		openFileAction.triggered.connect(self.fileOpen) 

		saveFileAction = self.createAction(self, "./images/save_file.ico", 
											"Save File", "Save File", 
											self.fileSave)
		saveFileAction.setShortcut(QtGui.QKeySequence.Save)

		saveFileAsAction = self.createAction(self, "./images/save_as_file.ico", 
											"Save File", "Save File As...", 
											self.fileSaveAs)
		saveFileAsAction.setShortcut(QtGui.QKeySequence("Ctrl+Shift+S"))

		fileMenu.addActions([openFileAction, saveFileAction, saveFileAsAction])
		fileToolBar.addActions([openFileAction, saveFileAction, saveFileAsAction])

		# Print Action (Print Document)
		printAction = self.createAction(self, "./images/printer.ico",
										"Print File", "Print File",
										self.printFile)
		printAction.setShortcut(QtGui.QKeySequence.Print)
		fileMenu.addAction(printAction)
		fileToolBar.addAction(printAction)

		# ----------------------------------
		# Edit Menus
		# ----------------------------------
		editMenu = self.menuBar().addMenu("&Edit")

		# ----------------------------------
		# Edit ToolBar
		# ----------------------------------
		editToolBar = QtWidgets.QToolBar("Edit")
		editToolBar.setIconSize(QtCore.QSize(60,60))
		self.addToolBar(QtCore.Qt.BottomToolBarArea, editToolBar)

		# Undo, Redo Actions
		undoAction = self.createAction(self, "./images/undo.ico", 
						"Undo", "Undo", self.editor.undo)
		undoAction.setShortcut(QtGui.QKeySequence.Undo)

		redoAction = self.createAction(self, "./images/redo.ico", 
						"Redo", "Redo", self.editor.redo)
		redoAction.setShortcut(QtGui.QKeySequence.Redo)

		editMenu.addActions([undoAction, redoAction])
		editToolBar.addActions([undoAction, redoAction])

		# Clear action
		clearAction = self.createAction(self, "./images/clear.ico",
							"Clear", "Clear", self.clearContent)
		editMenu.addAction(clearAction)
		editToolBar.addAction(clearAction)

		#cut, copy, paste, select all
		cutAction = self.createAction(self, "./images/cut.ico",
							"Cut", "Cut", self.editor.cut)
		copyAction = self.createAction(self, "./images/copy.ico",
							"Copy", "Copy", self.editor.copy)
		pasteAction = self.createAction(self, "./images/paste.ico",
							"Paste", "Paste", self.editor.paste)
		selectAllAction = self.createAction(self, "./images/selectAll.ico",
							"Select All", "Select All", self.editor.selectAll)

		cutAction.setShortcut(QtGui.QKeySequence.Cut)
		copyAction.setShortcut(QtGui.QKeySequence.Copy)
		pasteAction.setShortcut(QtGui.QKeySequence.Paste)
		selectAllAction.setShortcut(QtGui.QKeySequence.SelectAll)

		editMenu.addActions([cutAction, copyAction, pasteAction, selectAllAction])
		editToolBar.addActions([cutAction, copyAction, pasteAction, selectAllAction])

		# add separator
		editMenu.addSeparator()
		editToolBar.addSeparator()

		# add wrap text
		wrapTextAction = self.createAction(self, "./images/wrap.ico",
							"Wrap Text", "Wrap Text", self.toggleWrapText)
		wrapTextAction.setShortcut("Ctrl+Shift+W")
		editMenu.addAction(wrapTextAction)
		editToolBar.addAction(wrapTextAction)

		self.updateTitle()

	def toggleWrapText(self):
		self.editor.setLineWrapMode(not self.editor.lineWrapMode())

	def clearContent(self):
		self.editor.setPlainText("")

	def fileOpen(self):
		path, _ = QtWidgets.QFileDialog.getOpenFileName(
					parent=self,
					caption="Open file",
					directory="",
					filter=self.filterTypes)
		if path:
			try:
				with open(path, "r") as f:
					text = f.read()
			except Exception as e:
				self.dialogMessage(str(e))
			else:
				self.path = path 
				self.editor.setPlainText(text)
				self.updateTitle()

	def fileSave(self):
		if self.path is None:
			self.fileSaveAs()
		else:
			try:
				text = self.editor.toPlainText()
				with open(self.path, "w") as f:
					f.write(text)
					f.close()
			except Exception as e:
				self.dialogMessage(str(e))

	def fileSaveAs(self):
		path, _ = QtWidgets.QFileDialog.getSaveFileName(
					parent=self,
					caption="save file",
					directory="",
					filter=self.filterTypes)
		text = self.editor.toPlainText()

		if not path:
			return
		else:
			try:
				with open(path, "w") as f:
					f.writer(text)
			except Exception as e:
				self.dialogMessage(str(e))
			else:
				self.path = path 
				self.updateTitle()

	def printFile(self):
		printDialog = QtPrintSupport.QPrintDialog()
		if printDialog.exec_():
			self.editor.print_(printDialog.printer())

	def updateTitle(self):
		self.setWindowTitle("{0} - NotepadX".format(os.path.basename(self.path) if self.path else "Untitled"))

	def dialogMessage(self, message):
		dlg = QtWidgets.QMessageBox(self)
		dlg.setText(message)
		dlg.setIcon(QtWidgets.QMessageBox.Critical)
		dlg.show()


	def createAction(self, parent, iconPath, actionName, statusTip, triggeredMethod):
		action = QtWidgets.QAction(QtGui.QIcon(iconPath), actionName, parent)
		action.setStatusTip(statusTip)
		action.triggered.connect(triggeredMethod)
		return action



if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	demo = AppDemo()
	demo.show()

	sys.exit(app.exec_())