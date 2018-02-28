# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/python/typer/ui_ch_wordwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ch_wordwindow(object):
    def setupUi(self, ch_wordwindow):
        ch_wordwindow.setObjectName("ch_wordwindow")
        ch_wordwindow.resize(999, 554)
        ch_wordwindow.setMinimumSize(QtCore.QSize(999, 554))
        ch_wordwindow.setMaximumSize(QtCore.QSize(999, 554))
        font = QtGui.QFont()
        font.setFamily("黑体")
        ch_wordwindow.setFont(font)
        ch_wordwindow.setStyleSheet("color=rgb(255, 0, 0)")
        self.ch_word_input = QtWidgets.QLineEdit(ch_wordwindow)
        self.ch_word_input.setGeometry(QtCore.QRect(350, 250, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ch_word_input.setFont(font)
        self.ch_word_input.setText("")
        self.ch_word_input.setMaxLength(20)
        self.ch_word_input.setObjectName("ch_word_input")
        self.warning_set = QtWidgets.QLabel(ch_wordwindow)
        self.warning_set.setGeometry(QtCore.QRect(400, 310, 311, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.warning_set.setFont(font)
        self.warning_set.setStyleSheet("color:red")
        self.warning_set.setText("")
        self.warning_set.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.warning_set.setObjectName("warning_set")
        self.ch_word_set = QtWidgets.QLabel(ch_wordwindow)
        self.ch_word_set.setGeometry(QtCore.QRect(400, 80, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ch_word_set.setFont(font)
        self.ch_word_set.setObjectName("ch_word_set")
        self.label_3 = QtWidgets.QLabel(ch_wordwindow)
        self.label_3.setGeometry(QtCore.QRect(40, 510, 41, 21))
        self.label_3.setObjectName("label_3")
        self.time_used_set = QtWidgets.QLabel(ch_wordwindow)
        self.time_used_set.setGeometry(QtCore.QRect(100, 510, 101, 21))
        self.time_used_set.setObjectName("time_used_set")
        self.label_5 = QtWidgets.QLabel(ch_wordwindow)
        self.label_5.setGeometry(QtCore.QRect(240, 510, 41, 21))
        self.label_5.setObjectName("label_5")
        self.type_speed_set = QtWidgets.QLabel(ch_wordwindow)
        self.type_speed_set.setGeometry(QtCore.QRect(290, 510, 141, 21))
        self.type_speed_set.setObjectName("type_speed_set")
        self.ch_pinyin_set = QtWidgets.QLabel(ch_wordwindow)
        self.ch_pinyin_set.setGeometry(QtCore.QRect(400, 160, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ch_pinyin_set.setFont(font)
        self.ch_pinyin_set.setObjectName("ch_pinyin_set")

        self.retranslateUi(ch_wordwindow)
        QtCore.QMetaObject.connectSlotsByName(ch_wordwindow)

    def retranslateUi(self, ch_wordwindow):
        _translate = QtCore.QCoreApplication.translate
        ch_wordwindow.setWindowTitle(_translate("ch_wordwindow", "Form"))
        self.ch_word_input.setPlaceholderText(_translate("ch_wordwindow", "输入..."))
        self.ch_word_set.setText(_translate("ch_wordwindow", "词语"))
        self.label_3.setText(_translate("ch_wordwindow", "用时:"))
        self.time_used_set.setText(_translate("ch_wordwindow", "0时0分0秒"))
        self.label_5.setText(_translate("ch_wordwindow", "速度:"))
        self.type_speed_set.setText(_translate("ch_wordwindow", "0字/秒"))
        self.ch_pinyin_set.setText(_translate("ch_wordwindow", "pin yin"))

