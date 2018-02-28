#coding:utf8

#显示用时以及计算打字速度的线程的类脚本

import threading
import time

# 创建此实例时，需要传入一个run_window(QtWidgets.QWidget对象)
# running是启动和关闭thread的标志。设置为false，则关闭线程。
class thread_show_time_speed(threading.Thread):
	def __init__(self,run_window):
		super(thread_show_time_speed,self).__init__()
		self.run_window = run_window
		self.running = True
		
		self.waiting = False
		
		self.words = 0 #字数初始化 //用于计算打字速度

	def run(self):
		time_start =	time.time()
		self.repeat = True
		while self.running:
			if self.waiting == False:
				seconds = self.time_used(time_start,time.time())
				if self.repeat:
					self.repeat = False
				else:
					if self.words > 0:
						self.words-=1

				if seconds: 
					self.run_window.type_speed_set.setText('%.2f0字/秒'%(self.words/seconds))
			time.sleep(0.5)
		
	#在run_window界面的用时Label处 显示用时
	#返回已花的时间(秒) int型
	def time_used(self,time1,time2):
		time_used = time2 - time1
		all_seconds = time_used
		hours_used = int(time_used // 3600 )
		time_used = time_used % 3600
		minutes_used = int(time_used // 60)
		seconds_used = int(time_used % 60)
		
		time_used = str(hours_used)+'时'+str(minutes_used)+'分'+str(seconds_used)+'秒'
		self.run_window.time_used_set.setText(time_used)
		return int(all_seconds)
	
	#用于计算英文打字速度
	def add_number(self):
		self.words+=1
	
	#用于计算汉字打字速度
	def add_type_number(self,num):
		self.words+=num
	
	#用于终止线程运行及self.words初始化
	def terminate(self):
		self.words = 0
		self.running = False
		
	def wait(self):
		self.waiting = True
