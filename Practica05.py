# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtDeclarative import QDeclarativeView
from PyQt4.QtCore import QUrl, QObject, pyqtSignal
from datetime import datetime, date, time, timedelta
import calendar

class Test(QtGui.QWidget):
	def __init__(self):
		super(Test, self).__init__()
		self.setWindowIcon(QtGui.QIcon('flag.png'))
		self.initUI()
flaginitUI(self):
		self.button = QtGui.QPushButton("Aprietame")
		self.button.setIcon(QtGui.QIcon('flag.png'))
		self.setWindowIcon(QtGui.QIcon('flag.png'))
		self.button.clicked.connect(self.imprime)
		self.grid = QtGui.QGridLayout()
		self.grid.addWidget(self.button)
		self.setLayout(self.grid)
		self.setGeometry(500, 200, 500, 200) #Coordenadas y tamaño de la ventana
		self.port_label1 = QtGui.QLabel(QtGui.QApplication.translate("self", 'Ignacio Allende', None, QtGui.QApplication.UnicodeUTF8), self)
		self.port_label2 = QtGui.QLabel(QtGui.QApplication.translate("self", 'Miguel Hidalgo Y Costilla', None, QtGui.QApplication.UnicodeUTF8), self)
		self.port_label3 = QtGui.QLabel(QtGui.QApplication.translate("self", 'Vicente Guerrero', None, QtGui.QApplication.UnicodeUTF8), self)
		self.grid.addWidget(self.port_label1, 0, 0)
		self.grid.addWidget(self.port_label2, 0, 1)
		self.grid.addWidget(self.port_label3, 0, 2)
		self.setWindowTitle("!Viva México!")
		self.grid.addWidget(self.button, 1, 1)
		
		self.show()

	def imprime(self,button):
		date1 = datetime.now()   
		yer = date1.year 
		if date1.month <= 9 and date1.day < 15 :
			yer2 = yer
		else:
			yer2 = yer + 1
		date2 = datetime(yer2, 9, 16, 0, 0, 0)  
		restaFechas = date2 - date1
		cadena = "Faltan "+str(restaFechas.days)  + " dias y "+ str(restaFechas.seconds)+ " seg." + " Para el 15 de septiembre"
		self.button.setText(str(cadena))

if __name__ == '__main__':
	app = QtGui.QApplication([])
	app.setWindowIcon(QtGui.QIcon('flag.png'))
	test = Test()
	sys.exit(app.exec_())
