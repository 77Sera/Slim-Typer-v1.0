#coding:utf8

#中文句子练习模式的窗口类

from PyQt5 import QtWidgets,QtCore
from ui_ch_sentencewindow import Ui_ch_sentencewindow
from PyQt5.QtWidgets import QMessageBox
from class_thread_show_time_speed import thread_show_time_speed
import datetime
import os
import re

class ui_ch_sentencewindow(QtWidgets.QWidget,Ui_ch_sentencewindow):
	sentence1_signal = QtCore.pyqtSignal(int) #定义s1的数字信号
	sentence2_signal = QtCore.pyqtSignal(int) #定义s2的数字信号
	sentence3_signal = QtCore.pyqtSignal(int) #定义s3的数字信号
	degree1_signal = QtCore.pyqtSignal(str) #定义简单难度的字符信号
	degree2_signal = QtCore.pyqtSignal(str) #定义中等难度的字符信号
	degree3_signal = QtCore.pyqtSignal(str) #定义困难难度的字符信号
	#需要传QMainWindow对象参数
	def __init__(self,mainwindow):
		super(ui_ch_sentencewindow,self).__init__()
		self.setupUi(self) #应用基本ui

		#私有变量初始化及设定
		self.mainwindow = mainwindow
		self.thread = thread_show_time_speed(self) #实例化线程
		self.number = 6#设置句子库上限
		self.sentence_count = 0

		self.load_data() #载入练习数据

		#给输入框1,2,3textchanged时间绑定各自的信号发射函数
		self.sentence1_input.textChanged.connect(self.s1_emit)
		self.sentence2_input.textChanged.connect(self.s2_emit)
		self.sentence3_input.textChanged.connect(self.s3_emit)
		#s1，2，3input绑定sentence_judge函数
		self.sentence1_signal.connect(self.sentence_judge)
		self.sentence2_signal.connect(self.sentence_judge)
		self.sentence3_signal.connect(self.sentence_judge)
		
		#给菜单栏句子难度选择绑定字符信号发射
		self.mainwindow.action_ch_sentence_low.triggered.connect(self.d1_emit)
		self.mainwindow.action_ch_sentence_mid.triggered.connect(self.d2_emit)
		self.mainwindow.action_ch_sentence_high.triggered.connect(self.d3_emit)
		#难度选择信号绑定load_data函数
		self.degree1_signal.connect(self.load_data)
		self.degree2_signal.connect(self.load_data)
		self.degree3_signal.connect(self.load_data)

	#对应的信号发射函数，同时将其它菜单难度选项设为未选中状态
	def d1_emit(self):
		self.degree1_signal.emit('low')
		self.mainwindow.action_ch_sentence_mid.setChecked(False)
		self.mainwindow.action_ch_sentence_high.setChecked(False)
	def d2_emit(self):
		self.degree2_signal.emit('mid')
		self.mainwindow.action_ch_sentence_low.setChecked(False)
		self.mainwindow.action_ch_sentence_high.setChecked(False)
	def d3_emit(self):
		self.degree3_signal.emit('high')
		self.mainwindow.action_ch_sentence_low.setChecked(False)
		self.mainwindow.action_ch_sentence_mid.setChecked(False)

	#载入练习数据函数，默认难度为'low'
	def load_data(self,degree='low'):
		self.data = []
		try:
			sentence_txt = open('./source/ch_sentence/ch_sentence_'+degree+'.txt','r')
			count = 0
			for line in sentence_txt:
				line = line.replace('\n','')
				line = line.replace('  ','')
				line = line.replace(',','')
				line = line.replace('.','')
				self.data.append(line)
				count+=1
				if count == self.number: break
			sentence_txt.close()
		except:
			print('error')
		self.prepare_work()

	#对应s系列信号的发射函数
	def s1_emit(self):
		self.sentence1_signal.emit(1)
	def s2_emit(self):
		self.sentence2_signal.emit(2)
	def s3_emit(self):
		self.sentence3_signal.emit(3)

	#当句子的输入框变化时执行此函数，输入参数order(int)指明第几行输入框
	def sentence_judge(self,order):
		#判断当前输入框、输入model、预警框
		if order == 1:
			qss_sentence_input = 'sentence1_input'
			sentence_set = self.sentence1_set
			sentence_input = self.sentence1_input
			warning_set = self.warning1_set
		elif order == 2:
			qss_sentence_input = 'sentence2_input'
			sentence_set = self.sentence2_set
			sentence_input = self.sentence2_input
			warning_set = self.warning2_set
		elif order == 3:
			qss_sentence_input = 'sentence3_input'
			sentence_set = self.sentence3_set
			sentence_input = self.sentence3_input
			warning_set = self.warning3_set
		
		if sentence_input == '': return
		
		#开启计时线程，若已经启动(else)则计算此时输入了多少字符
		if self.restart:
			self.restart = False
			self.thread = thread_show_time_speed(self)
			self.thread.start()
		else:
			x = len(sentence_input.text())
			if x > self.type_count: #若当前打的字比之前存储的type_count多，就加上差值
				self.thread.add_type_number(x-self.type_count)
			else: #否则就说明已经切换到下一行输入框，所以直接加x，+2为字数矫正。考虑0.5秒内可能的损失字符数
				self.thread.add_type_number(x+2)
			self.type_count = x #将类变量type_count值被x赋值
			
		input_text = sentence_input.text() #获取当前输入框文本
		model_text = sentence_set.text() #获取当前正确文本
		
		#若正确文本不等于输入文本，则为输错
		if model_text[:len(input_text)] != input_text:
			warning_set.setText('*输错了!')
			
			#应用输错的qss样式
			stylesheet = '#'+qss_sentence_input+'{border:1px solid red}'
			self.setStyleSheet(stylesheet)
			
			#同时设定当前最大输入字数
			sentence_input.setMaxLength( len(input_text) )
		else:
			warning_set.setText('')
			
			#应用未输错的样式
			stylesheet = '#'+qss_sentence_input+'{border:1px}'
			self.setStyleSheet(stylesheet)
			
			#恢复最大字数为默认值。
			sentence_input.setMaxLength(len(model_text))
			#若正确文本和输入文本完全相同，则进行判断，若当前总输入文本未结束就切换到下一行，否则切换到下一个文本
			if model_text == input_text:
				if order == 1:
					self.sentence1_input.setEnabled(False)
					if self.sentence2_set.text() != '':
						self.sentence2_input.setEnabled(True)
						self.sentence2_input.setFocus()
						self.sentence2_input.setMaxLength(len(self.sentence2_set.text()))
					else:
						self.check_data()
				elif order == 2:
					self.sentence2_input.setEnabled(False)
					if self.sentence3_set.text() != '':
						self.sentence3_input.setEnabled(True)
						self.sentence3_input.setFocus()
						self.sentence3_input.setMaxLength(len(self.sentence3_set.text()))
					else:
						self.check_data()
				elif order == 3:
					self.check_data()
	
	# 将打字练习窗口界面初始化
	def prepare_work(self):
		self.sentence1_input.setText('')
		self.sentence2_input.setText('')
		self.sentence3_input.setText('')
		self.thread.terminate()
		self.restart = True
		self.sentence_count = 0
		self.type_count = 0 #用于计算打字速度中的每秒字数
		self.prepare_sentence_set(self.data[self.sentence_count])
		self.warning1_set.setText('')
		self.warning2_set.setText('')
		self.warning3_set.setText('')
		self.time_used_set.setText('0时0分0秒')
		self.type_speed_set.setText('0字/秒')
			
	#检查是否已经打完所有句子，是则congradulations，否则切换至下一句
	def check_data(self):
		self.sentence_count+=1
		if self.sentence_count == len(self.data):
			self.save_rank()
			self.thread.wait()
			r = QMessageBox.information(self,('Congradulations!'),('\n\n\t恭喜你通关了一次句子练习!\t\t\t\n\n\t\t再接再励吧!\t\n\n\t(Ok:再来一次 | Cancel：选择其他模式)\t\n'),QMessageBox.StandardButtons(QMessageBox.Ok|QMessageBox.Cancel))
			self.thread.terminate() #表示已通关练习，停止计时线程
			if r == QMessageBox.Cancel:
				self.hide()
				self.mainwindow.radio_blank_menu.setChecked(True)
			else:
				self.sentence1_input.setText('')
				self.sentence2_input.setText('')
				self.sentence3_input.setText('')
				self.prepare_work()
		else:
			self.prepare_sentence_set(self.data[self.sentence_count])

	# 对于传递过来的句子，进行拼写界面初始化设置
	def prepare_sentence_set(self,sentence):
		if len(sentence) > 52: #需要有三行文本的情况
			self.sentence1_set.setText(sentence[:26].strip())
			self.sentence2_set.setText(sentence[26:52].strip())
			self.sentence3_set.setText(sentence[52:].strip())
			self.sentence2_input.show()
			self.sentence3_input.show()
			self.sentence1_input.setEnabled(True)
			self.sentence2_input.setEnabled(False)
			self.sentence3_input.setEnabled(False)
		elif len(sentence) > 26: #两行文本
			self.sentence1_set.setText(sentence[:26].strip())
			self.sentence2_set.setText(sentence[26:].strip())
			self.sentence2_input.show()
			self.sentence3_set.setText('')
			self.sentence3_input.hide()
			self.sentence1_input.setEnabled(True)
			self.sentence2_input.setEnabled(False)
		else: #一行文本
			self.sentence1_set.setText(sentence.strip())
			self.sentence2_set.setText('')
			self.sentence3_set.setText('')
			self.sentence2_input.hide()
			self.sentence3_input.hide()
			self.sentence1_input.setEnabled(True)

		self.sentence1_input.setText('')
		self.sentence2_input.setText('')
		self.sentence3_input.setText('')
		self.sentence1_input.setFocus()
		
	#通关完一次后，自动保存当前记录，加上历史纪录，会取前五项最好的进行保存。
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
	
	
		file_path = './source/rank/ch_sentence_'
	
		if self.mainwindow.action_ch_sentence_low.isChecked():
			rank_degree = 'low'
		elif self.mainwindow.action_ch_sentence_mid.isChecked():
			rank_degree = 'mid'
		elif self.mainwindow.action_ch_sentence_high.isChecked():
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
			if int(data[i][3]) > int(temp_data[3]):
				data.insert(i , temp_data)
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
		
	def show(self):
		super().show()
		self.prepare_work()
		
	def hide(self):
		super().hide()
		self.sentence1_input.setText('')
		self.sentence2_input.setText('')
		self.sentence3_input.setText('')
		if self.thread.running:
			self.thread.terminate()

if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = ui_ch_sentencewindow()
	window.show()
	sys.exit(app.exec_())
