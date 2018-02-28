# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/python/typer/ui_en_wordwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_en_wordwindow(object):
    def setupUi(self, en_wordwindow):
        en_wordwindow.setObjectName("en_wordwindow")
        en_wordwindow.resize(999, 554)
        en_wordwindow.setMinimumSize(QtCore.QSize(999, 554))
        en_wordwindow.setMaximumSize(QtCore.QSize(999, 554))
        font = QtGui.QFont()
        font.setFamily("黑体")
        en_wordwindow.setFont(font)
        en_wordwindow.setStyleSheet("color=rgb(255, 0, 0)")
        self.en_word_input = QtWidgets.QLineEdit(en_wordwindow)
        self.en_word_input.setGeometry(QtCore.QRect(320, 250, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.en_word_input.setFont(font)
        self.en_word_input.setText("")
        self.en_word_input.setMaxLength(20)
        self.en_word_input.setObjectName("en_word_input")
        self.warning_set = QtWidgets.QLabel(en_wordwindow)
        self.warning_set.setGeometry(QtCore.QRect(360, 330, 311, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.warning_set.setFont(font)
        self.warning_set.setStyleSheet("color:red")
        self.warning_set.setText("")
        self.warning_set.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.warning_set.setObjectName("warning_set")
        self.en_word_set = QtWidgets.QLabel(en_wordwindow)
        self.en_word_set.setGeometry(QtCore.QRect(370, 130, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.en_word_set.setFont(font)
        self.en_word_set.setObjectName("en_word_set")
        self.label_3 = QtWidgets.QLabel(en_wordwindow)
        self.label_3.setGeometry(QtCore.QRect(40, 510, 41, 21))
        self.label_3.setObjectName("label_3")
        self.time_used_set = QtWidgets.QLabel(en_wordwindow)
        self.time_used_set.setGeometry(QtCore.QRect(100, 510, 101, 21))
        self.time_used_set.setObjectName("time_used_set")
        self.label_5 = QtWidgets.QLabel(en_wordwindow)
        self.label_5.setGeometry(QtCore.QRect(240, 510, 41, 21))
        self.label_5.setObjectName("label_5")
        self.type_speed_set = QtWidgets.QLabel(en_wordwindow)
        self.type_speed_set.setGeometry(QtCore.QRect(290, 510, 141, 21))
        self.type_speed_set.setObjectName("type_speed_set")

        self.retranslateUi(en_wordwindow)
        QtCore.QMetaObject.connectSlotsByName(en_wordwindow)

    def retranslateUi(self, en_wordwindow):
        _translate = QtCore.QCoreApplication.translate
        en_wordwindow.setWindowTitle(_translate("en_wordwindow", "Form"))
        self.en_word_input.setPlaceholderText(_translate("en_wordwindow", "start here..."))
        self.en_word_set.setText(_translate("en_wordwindow", "place holder"))
        self.label_3.setText(_translate("en_wordwindow", "用时:"))
        self.time_used_set.setText(_translate("en_wordwindow", "0时0分0秒"))
        self.label_5.setText(_translate("en_wordwindow", "速度:"))
        self.type_speed_set.setText(_translate("en_wordwindow", "0字/秒"))

