#coding:utf8

#英文单词练习模式

from ui_ch_wordwindow import Ui_ch_wordwindow
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QMessageBox
from class_thread_show_time_speed import thread_show_time_speed
import datetime
import os
import re

#继承QWidget类，以及基本ui类
class ui_ch_wordwindow(QtWidgets.QWidget,Ui_ch_wordwindow):
	degree1_signal = QtCore.pyqtSignal(str) #定义简单难度的字符信号
	degree2_signal = QtCore.pyqtSignal(str) #定义中等难度的字符信号
	degree3_signal = QtCore.pyqtSignal(str) #定义困难难度的字符信号
	def __init__(self,mainwindow): 
		super(ui_ch_wordwindow,self).__init__()
		self.setupUi(self) #初始化基本ui
		self.mainwindow = mainwindow
		
		#给输入框textchange事件绑定word_judge函数
		self.ch_word_input.textChanged.connect(self.word_judge) 
		self.number = 15 #设置单词库上限 默认15
		
		self.restart = True
		
		self.thread = thread_show_time_speed(self) #实例化线程
		self.load_data() #欲载入练习数据
		
		#给菜单栏难度选择绑定信号发射函数
		self.mainwindow.action_ch_word_low.triggered.connect(self.d1_emit)
		self.mainwindow.action_ch_word_mid.triggered.connect(self.d2_emit)
		self.mainwindow.action_ch_word_high.triggered.connect(self.d3_emit)
		#给难度发射信号绑定load_data函数
		self.degree1_signal.connect(self.load_data)
		self.degree2_signal.connect(self.load_data)
		self.degree3_signal.connect(self.load_data)
	
	#d系列信号的发射函数
	def d1_emit(self):
		self.degree1_signal.emit('low')
		self.mainwindow.action_ch_word_mid.setChecked(False)
		self.mainwindow.action_ch_word_high.setChecked(False)
	def d2_emit(self):
		self.degree2_signal.emit('mid')
		self.mainwindow.action_ch_word_low.setChecked(False)
		self.mainwindow.action_ch_word_high.setChecked(False)
	def d3_emit(self):
		self.degree3_signal.emit('high')
		self.mainwindow.action_ch_word_low.setChecked(False)
		self.mainwindow.action_ch_word_mid.setChecked(False)
	
	#载入练习数据函数，默认参数degree
	def load_data(self,degree='low'):
		self.data = [] #初始化单词库
		try:
			word_txt = open('./source/ch_word/ch_word_'+degree+'.txt','r')
			count = 0
			for line in word_txt:
				line = line.replace('\n','')
				line = line.split(' ')
				self.data+=[line]
				count+=1
				if count == self.number: break
			word_txt.close()
		except:
			print('error')
		self.prepare_work()
	
	#判断输入框的正确与否，错误就不可以继续输入，并且要提醒修改
	def word_judge(self):
		input_text = self.ch_word_input.text()
		model_text = self.ch_word_set.text()
		if self.restart:
			if input_text == '': return
			self.restart = False
			#开启thread，显示时间和打字速度。
			self.thread = thread_show_time_speed(self)
			self.thread.start()
			
		if model_text[:len(input_text)] != input_text:
			self.warning_set.setText('*输入错误, 注意修改')
			
			stylesheet = '#ch_word_input{border:1px solid red}'
			self.setStyleSheet(stylesheet)
			
			self.ch_word_input.setMaxLength(len(input_text))
		else:
			stylesheet = '#ch_word_input{border:1px}'
			self.setStyleSheet(stylesheet)
			
			self.warning_set.setText('')
			self.ch_word_input.setMaxLength(len(model_text))
			if model_text == input_text:
				self.word_count+=1
				if self.word_count == len(self.data):
					self.save_rank()
					self.thread.wait()
					r = QMessageBox.information(self,('Congradulations!'),('\n\n\t恭喜你通关了一次单词练习!\t\t\t\n\n\t\t再接再励吧!\t\n\n\t(Ok:再来一次 | Cancel：选择其他模式)\t\n'),QMessageBox.StandardButtons(QMessageBox.Ok|QMessageBox.Cancel))
					self.thread.terminate()
					if r == QMessageBox.Cancel:
						self.hide()
						self.mainwindow.radio_blank_menu.setChecked(True)
						self.restart = True
						return
					else:
						self.time_used_set.setText('0时0分0秒')
						self.type_speed_set.setText('0字/秒')
						self.word_count = 0
						self.restart = True
				self.thread.add_type_number(len(model_text)+2)
				self.ch_word_input.setText('')
				self.ch_word_set.setText(self.data[self.word_count][0])
				self.ch_pinyin_set.setText(self.data[self.word_count][1])
	
	#通关完一次后保存记录
	def save_rank(self):
		#得到本次通关的记录，存入temp_data中,[0]为用时，1为速度，2为存储的日期，3为总秒数
		temp_data = []
		marktime = datetime.datetime.now().strftime("%Y.%m.%d_%H:%M:%S")
		speed = self.type_speed_set.text()
		time = self.time_used_set.text()
		pat = '([0-9]{,2})时([0-9]{,2})分([0-9]{,2})秒'
		r = re.compile(pat).findall(time)[0]
		whole_seconds = int(r[0])*3600+int(r[1])*60+int(r[2])
		temp_data.append(time)
		temp_data.append(speed)
		temp_data.append(marktime)
		temp_data.append(str(whole_seconds))
	
		file_path = './source/rank/ch_word_'
	
		if self.mainwindow.action_ch_word_low.isChecked():
			rank_degree = 'low'
		elif self.mainwindow.action_ch_word_mid.isChecked():
			rank_degree = 'mid'
		elif self.mainwindow.action_ch_word_high.isChecked():
			rank_degree = 'high'
		
		file_path = file_path + rank_degree + '.txt'
		
		data = [] #data是所有纪录数据的list形式。二维数组
		
		if os.path.exists(file_path):
			file = open(file_path,'r')
			for line in file:
				line = line.replace('\n','')
				line = line.split(' ')
				data.append(line)
			file.close()

		insert = False
		
		for i in range(len(data)):
			if int(data[i][3]) >= int(temp_data[3]):
				data.insert(i , temp_data)
				insert = True
				break

		if len(data) == 0:
			data.append(temp_data)
			insert = True
		
		if insert == False and len(data) < 5:
			data.append(temp_data)
		
		file = open(file_path,'w')
		count = 0
		for i in range(len(data)):
			line = ' '.join(data[i])
			line+='\n'
			file.write(line)
			count+=1
			if count == 5: break
		file.close()

	#每次重新开始进行的预准备工作
	def prepare_work(self):
		self.ch_word_input.setText('')
		if self.thread: 
			self.thread.terminate()
		self.word_count = 0 #初始化单词计数器
		self.ch_word_set.setText(self.data[self.word_count][0])
		self.ch_pinyin_set.setText(self.data[self.word_count][1])
		self.ch_word_input.setText('')
		self.ch_word_input.setFocus()
		self.time_used_set.setText('0时0分0秒')
		self.type_speed_set.setText('0字/秒')
	
	#重新show方法，每次调用的时候都重制一次当前界面
	def show(self):
		super().show()
		self.prepare_work()
	
	#重写hide方法，每次调用都会终止线程
	def hide(self):
		super().hide()
		self.ch_word_input.setText('')
		if self.thread.running:
			self.thread.terminate()
		
if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = ui_ch_wordwindow()
	window.show()
	sys.exit(app.exec_())
