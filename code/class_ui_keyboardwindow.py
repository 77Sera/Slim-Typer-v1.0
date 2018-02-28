#coding:utf8

#键盘熟悉模式窗口

from PyQt5 import QtWidgets
from ui_keyboardwindow import Ui_keyboardwindow

#继承QWidget类和基本ui类
class ui_keyboardwindow(QtWidgets.QWidget,Ui_keyboardwindow):
	def __init__(self,mainwindow): #输入参数为QMainWindow对象
		super(ui_keyboardwindow,self).__init__()
		self.setupUi(self) #初始化基本ui
		
		self.mainwindow = mainwindow
		
		#给返回按钮绑定back_menu1函数
		self.btn_back_menu1.clicked.connect(self.back_menu1)
		
		#给单选按钮绑定show_key函数
		self.radio_clear.hide()
		self.radio_a.clicked.connect(self.show_key)
		self.radio_b.clicked.connect(self.show_key)
		self.radio_c.clicked.connect(self.show_key)
		self.radio_d.clicked.connect(self.show_key)
		self.radio_e.clicked.connect(self.show_key)
		self.radio_f.clicked.connect(self.show_key)
		self.radio_g.clicked.connect(self.show_key)
		self.radio_h.clicked.connect(self.show_key)
		self.radio_i.clicked.connect(self.show_key)
		self.radio_j.clicked.connect(self.show_key)
		self.radio_k.clicked.connect(self.show_key)
		self.radio_l.clicked.connect(self.show_key)
		self.radio_m.clicked.connect(self.show_key)
		self.radio_n.clicked.connect(self.show_key)
		self.radio_o.clicked.connect(self.show_key)
		self.radio_p.clicked.connect(self.show_key)
		self.radio_q.clicked.connect(self.show_key)
		self.radio_r.clicked.connect(self.show_key)
		self.radio_s.clicked.connect(self.show_key)
		self.radio_t.clicked.connect(self.show_key)
		self.radio_u.clicked.connect(self.show_key)
		self.radio_v.clicked.connect(self.show_key)
		self.radio_w.clicked.connect(self.show_key)
		self.radio_x.clicked.connect(self.show_key)
		self.radio_y.clicked.connect(self.show_key)
		self.radio_z.clicked.connect(self.show_key)
	
	
	# 返回主页的函数
	def back_menu1(self):
		self.mainwindow.set_menu1()
		self.clear_checked()
		self.hide()
	
	#消息框显示某个按钮的选中情况
	def show_key(self):
		if self.radio_a.isChecked():
			self.mainwindow.statusbar.showMessage('按键: A ')
		if self.radio_b.isChecked():
			self.mainwindow.statusbar.showMessage('按键: B ')
		if self.radio_c.isChecked():
			self.mainwindow.statusbar.showMessage('按键: C ')
		if self.radio_d.isChecked():
			self.mainwindow.statusbar.showMessage('按键: D ')
		if self.radio_e.isChecked():
			self.mainwindow.statusbar.showMessage('按键: E ')
		if self.radio_f.isChecked():
			self.mainwindow.statusbar.showMessage('按键: F ')
		if self.radio_g.isChecked():
			self.mainwindow.statusbar.showMessage('按键: G ')
		if self.radio_h.isChecked():
			self.mainwindow.statusbar.showMessage('按键: H ')
		if self.radio_i.isChecked():
			self.mainwindow.statusbar.showMessage('按键: I ')
		if self.radio_j.isChecked():
			self.mainwindow.statusbar.showMessage('按键: J ')
		if self.radio_k.isChecked():
			self.mainwindow.statusbar.showMessage('按键: K ')
		if self.radio_l.isChecked():
			self.mainwindow.statusbar.showMessage('按键: L ')
		if self.radio_m.isChecked():
			self.mainwindow.statusbar.showMessage('按键: M ')
		if self.radio_n.isChecked():
			self.mainwindow.statusbar.showMessage('按键: N ')
		if self.radio_o.isChecked():
			self.mainwindow.statusbar.showMessage('按键: O ')
		if self.radio_p.isChecked():
			self.mainwindow.statusbar.showMessage('按键: P ')
		if self.radio_q.isChecked():
			self.mainwindow.statusbar.showMessage('按键: Q ')
		if self.radio_r.isChecked():
			self.mainwindow.statusbar.showMessage('按键: R ')
		if self.radio_s.isChecked():
			self.mainwindow.statusbar.showMessage('按键: S ')
		if self.radio_t.isChecked():
			self.mainwindow.statusbar.showMessage('按键: T ')
		if self.radio_u.isChecked():
			self.mainwindow.statusbar.showMessage('按键: U ')
		if self.radio_v.isChecked():
			self.mainwindow.statusbar.showMessage('按键: V ')
		if self.radio_w.isChecked():
			self.mainwindow.statusbar.showMessage('按键: W ')
		if self.radio_x.isChecked():
			self.mainwindow.statusbar.showMessage('按键: X ')
		if self.radio_y.isChecked():
			self.mainwindow.statusbar.showMessage('按键: Y ')
		if self.radio_z.isChecked():
			self.mainwindow.statusbar.showMessage('按键: Z ')
	
	#清除选中函数
	def clear_checked(self):
		self.radio_clear.setChecked(True)
	
	#重写show方法，show的同时清除选中按钮
	def show(self):
		super().show()
		self.clear_checked()
	
	#重写hide方法，hide同时清除消息框数据
	def hide(self):
		super().hide()
		self.mainwindow.statusbar.showMessage('')
