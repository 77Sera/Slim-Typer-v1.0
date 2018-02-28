#coding:utf8

# "本地记录"这个窗口的类脚本

from PyQt5 import QtWidgets
from ui_rankwindow import Ui_rankwindow

class ui_rankwindow(QtWidgets.QWidget,Ui_rankwindow):
	#创建实例时需有参数QMainWindow对象
	def __init__(self,mainwindow):
		super(ui_rankwindow,self).__init__()
		self.setupUi(self) #初始化ui
		self.radio_blank.hide()
		self.mainwindow = mainwindow
		
		#类变量
		self.rank_model = 'ch_word_' #rank的模式
		self.rank_degree = '' #rank的难度
		
		#给cbbox选择模式框的改变选项事件绑定change_model函数
		self.cbbox_model.currentTextChanged.connect(self.change_model)
		
		#给单选按钮（初级中级高级）的点击事件添加change_degree函数
		self.radio_low.clicked.connect(self.change_degree)
		self.radio_mid.clicked.connect(self.change_degree)
		self.radio_high.clicked.connect(self.change_degree)
		self.radio_blank.clicked.connect(self.change_degree)
		
		#给菜单栏的"纪录"选项也就是action_offline_rank添加 self.show函数
		self.mainwindow.action_offline_rank.triggered.connect(self.show)
	
	#根据combobox的变化来决定类变量self.rank_model的值
	def change_model(self):
		current_text = self.cbbox_model.currentText()
		if current_text == '中文词语模式':
			self.rank_model = 'ch_word_'
		elif current_text == '中文句子模式':
			self.rank_model = 'ch_sentence_'
		elif current_text == '英文单词模式':
			self.rank_model = 'en_word_'
		elif current_text == '英文句子模式':
			self.rank_model = 'en_sentence_'
		
		#每当改变combobox时，就将空白按钮设置成被选中状态，并且清空纪录显示
		self.radio_blank.setChecked(True)
		for i in range(1,6):
				self.set_blank(i)
	
	#根据难度按钮的选择，改变类变量self.rank_degree的值
	def change_degree(self):
		if self.radio_low.isChecked():
			self.rank_degree = 'low'
		elif self.radio_mid.isChecked():
			self.rank_degree = 'mid'
		elif self.radio_high.isChecked():
			self.rank_degree = 'high'
		elif self.radio_blank.isChecked():
			for i in range(1,6):
				self.set_blank(i)
			return
		#当得到了rank_degree的值后，就执行一次获取纪录
		self.get_rank()
	
	#获取本地纪录函数
	def get_rank(self):
		try:
			#将两个类变量结合起来赋值给file_path，也就是要载入的对应纪录文本
			file_path = './source/rank/'+self.rank_model+self.rank_degree+'.txt'
			#这里因为是windows环境下，没有对目标文本进行utf8编码处理，所以会在linux下有问题，需要自行转换。encoding='utf8'，在windows下转换会报编码error
			f = open(file_path,'r')
			i = 1
			for line in f:
				line = line.replace('\n','')
				data = line.split(' ')
				self.set_rank(i,data)
				i+=1
			#i-=1
			while i <= 5:
				self.set_blank(i)
				i+=1
		except Exception as e:
			print('rank open error')
			raise e
	
	#此函数将成绩显示在gui界面上
	#输入参数num是指输入在第几行，data是一个list元素，[0]为用时，[1]为完成速度，[2]为记录时间
	def set_rank(self,num,data):
		if num == 1:
			self.rank_time_set1.setText(data[0])
			self.rank_speed_set1.setText(data[1])
			self.rank_marktime_set1.setText(data[2])
		elif num == 2:
			self.rank_time_set2.setText(data[0])
			self.rank_speed_set2.setText(data[1])
			self.rank_marktime_set2.setText(data[2])
		elif num == 3:
			self.rank_time_set3.setText(data[0])
			self.rank_speed_set3.setText(data[1])
			self.rank_marktime_set3.setText(data[2])
		elif num == 4:
			self.rank_time_set4.setText(data[0])
			self.rank_speed_set4.setText(data[1])
			self.rank_marktime_set4.setText(data[2])
		elif num == 5:
			self.rank_time_set5.setText(data[0])
			self.rank_speed_set5.setText(data[1])
			self.rank_marktime_set5.setText(data[2])
	
	#将对应行的纪录清除的函数，输入参数num是int型。即对应行数
	def set_blank(self,num):
		if num == 1:
			self.rank_time_set1.setText('')
			self.rank_speed_set1.setText('   无')
			self.rank_marktime_set1.setText('')
		elif num == 2:
			self.rank_time_set2.setText('')
			self.rank_speed_set2.setText('   无')
			self.rank_marktime_set2.setText('')
		elif num == 3:
			self.rank_time_set3.setText('')
			self.rank_speed_set3.setText('   无')
			self.rank_marktime_set3.setText('')
		elif num == 4:
			self.rank_time_set4.setText('')
			self.rank_speed_set4.setText('   无')
			self.rank_marktime_set4.setText('')
		elif num == 5:
			self.rank_time_set5.setText('')
			self.rank_speed_set5.setText('   无')
			self.rank_marktime_set5.setText('')
	
	#载入qss文本的函数，实现本窗口的ui样式。
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
	
	#重写show函数，在show时载入样式并清空所有纪录。
	def show(self):
		for i in range(1,6):
			self.set_blank(i)
		stylesheet = self.load_qss('./qss/rank_qss.txt')
		self.setStyleSheet(stylesheet)
		super().show()
	
	#重写hide函数，在hide时选中radio_blank
	def hide(self):
		self.radio_blank.setChecked(True)
		super().hide()
