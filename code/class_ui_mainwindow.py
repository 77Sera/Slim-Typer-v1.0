#coding:utf8

#这是程序的主窗口的类脚本

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui_mainwindow import Ui_mainwindow
from class_ui_keyboardwindow import ui_keyboardwindow #导入键盘练习窗口
from class_ui_en_wordwindow import ui_en_wordwindow #导入英文单词练习窗口
from class_ui_ch_wordwindow import ui_ch_wordwindow #导入中文词语练习窗口
from class_ui_en_sentencewindow import ui_en_sentencewindow #导入英文句子练习窗口
from class_ui_ch_sentencewindow import ui_ch_sentencewindow #导入中文句子练习窗口
from class_ui_rankwindow import ui_rankwindow #导入查看纪录窗口

#继承QtWidgets.QMainWindow类，以及在designer中的基本ui设计Ui_mainwindow
class ui_mainwindow(QtWidgets.QMainWindow,Ui_mainwindow):
	def __init__(self):
		super(ui_mainwindow,self).__init__()
		self.setupUi(self)
		self.radio_blank_menu.hide()
		self.radio_blank.hide()
		self.btn_back.hide()
		
		#应用ui样式
		stylesheet = self.load_qss('./qss/main_qss.txt')
		self.setStyleSheet(stylesheet)
		
		#生成子窗口实例
		self.keyboardwindow = ui_keyboardwindow(self)
		self.en_wordwindow = ui_en_wordwindow(self)
		self.ch_wordwindow = ui_ch_wordwindow(self)
		self.en_sentencewindow = ui_en_sentencewindow(self)
		self.ch_sentencewindow = ui_ch_sentencewindow(self)
		self.rankwindow = ui_rankwindow(self)

		#单选按钮的事件绑定(change_model)，用以选择打字模式
		self.radio_ch_word.clicked.connect(self.change_model)
		self.radio_ch_sentence.clicked.connect(self.change_model)
		self.radio_en_word.clicked.connect(self.change_model)
		self.radio_en_sentence.clicked.connect(self.change_model)
		self.radio_blank_menu.clicked.connect(self.change_model)
		
		#将菜单栏的关于选项绑定about_software函数
		self.action_about.triggered.connect(self.about_software)
		
		#窗口初始化设定(为了应用ui)
		self.radio_key.clicked.connect(self.choose_model)
		self.radio_type.clicked.connect(self.choose_model)
		self.radio_blank.clicked.connect(self.choose_model)
		self.set_menu1()
		
		#将返回BACK按钮的点击事件绑定set_menu1函数
		self.btn_back.clicked.connect(self.set_menu1)
	
	#初始化界面设置，用以选择键盘熟悉练习和打字练习。
	def set_menu1(self):
		self.radio_ch_word.hide()
		self.radio_ch_sentence.hide()
		self.radio_en_word.hide()
		self.radio_en_sentence.hide()
		self.radio_blank_menu.setChecked(True)
		self.radio_key.show()
		self.radio_type.show()
		self.radio_blank.setChecked(True)
		self.label_welcome.show()
		self.btn_back.hide()
		self.en_wordwindow.hide()
		self.en_sentencewindow.hide()
		self.ch_sentencewindow.hide()
		self.ch_wordwindow.hide()
	
	#初始化打字练习选择界面，用以选择打字练习模式
	def set_menu2(self):
		self.radio_key.hide()
		self.radio_type.hide()
		self.label_welcome.hide()
		self.radio_blank.setChecked(True)
		self.radio_ch_word.show()
		self.radio_ch_sentence.show()
		self.radio_en_word.show()
		self.radio_en_sentence.show()
		self.btn_back.show()
	
	#这是初始化界面(2个选择按钮)的时候，此2按钮对应触发此函数
	def choose_model(self):
		#若选中键盘熟悉模式，则将其他按钮屏蔽，然后载入键盘练习窗口
		if self.radio_key.isChecked():
			self.radio_key.hide()
			self.radio_type.hide()
			self.label_welcome.hide()
			self.grid_widget.addWidget(self.keyboardwindow)
			self.keyboardwindow.show()
		#若为打字练习模式，则进行打字练习选择界面初始化
		elif self.radio_type.isChecked():
			self.set_menu2()
		
	#根据打字练习模式按钮改变子窗口
	def change_model(self):
		if self.radio_en_word.isChecked():
			self.en_sentencewindow.hide()
			self.ch_sentencewindow.hide()
			self.ch_wordwindow.hide()
			self.grid_widget.addWidget(self.en_wordwindow)
			self.en_wordwindow.show()
		elif self.radio_ch_word.isChecked():
			self.en_wordwindow.hide()
			self.ch_sentencewindow.hide()
			self.en_sentencewindow.hide()
			self.grid_widget.addWidget(self.ch_wordwindow)
			self.ch_wordwindow.show()
		elif self.radio_en_sentence.isChecked():
			self.en_wordwindow.hide()
			self.ch_wordwindow.hide()
			self.ch_sentencewindow.hide()
			self.grid_widget.addWidget(self.en_sentencewindow)
			self.en_sentencewindow.show()
		elif self.radio_ch_sentence.isChecked():
			self.en_wordwindow.hide()
			self.ch_wordwindow.hide()
			self.en_sentencewindow.hide()
			self.grid_widget.addWidget(self.ch_sentencewindow)
			self.ch_sentencewindow.show()
		elif self.radio_blank_menu.isChecked():
			self.ch_wordwindow.hide()
			self.ch_sentencewindow.hide()
			self.en_wordwindow.hide()
			self.en_sentencewindow.hide()

	#此为菜单栏"关于"选项的执行函数，用提示框形式介绍软件
	def about_software(self):
		content = '\n\n\t软件名称: Slim Typer v1.0 快捷打字练习软件\t\n\n\t作者: sera\'s group\t\t\n\n\t版本: v1.0\t\n\n\t主要库: PyQt5\t\t\n\n\t用途: 熟悉键盘，打字练习\t\t\n\n\t功能: 成绩纪录, 多种练习模式\t\t\n\n'

		QMessageBox.information(self,('The Typer infor'),(content),QMessageBox.StandardButtons())
	
	#加载txt后缀的qss样式，如qss.txt，输入参数为qss.txt的路径(str)，返回stylesheet(str)
	def load_qss(self,qss_path):
		stylesheet = ''
		try:
			file = open(qss_path,'r')
			stylesheet = ''
			for line in file:
				stylesheet+=line
		except:
			print('qss improt error')
		return stylesheet
