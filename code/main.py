from class_ui_mainwindow import ui_mainwindow
from PyQt5 import QtWidgets

if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = ui_mainwindow()
	window.show()
	sys.exit(app.exec_())
