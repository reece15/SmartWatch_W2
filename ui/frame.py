# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 683)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_ob = QtWidgets.QLabel(self.centralwidget)
        self.label_ob.setGeometry(QtCore.QRect(70, 120, 320, 320))
        self.label_ob.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_ob.setText("")
        self.label_ob.setObjectName("label_ob")
        self.btn_trans = QtWidgets.QPushButton(self.centralwidget)
        self.btn_trans.setGeometry(QtCore.QRect(420, 280, 75, 23))
        self.btn_trans.setObjectName("btn_trans")
        self.label_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(530, 120, 320, 320))
        self.label_pic.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_pic.setText("")
        self.label_pic.setObjectName("label_pic")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 470, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(660, 470, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 330, 121, 41))
        self.label_5.setObjectName("label_5")
        self.label_ob_info = QtWidgets.QLabel(self.centralwidget)
        self.label_ob_info.setGeometry(QtCore.QRect(80, 490, 771, 161))
        self.label_ob_info.setText("")
        self.label_ob_info.setObjectName("label_ob_info")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(70, 60, 71, 16))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "表盘文件转换 V1.1   by reece"))
        self.btn_trans.setText(_translate("MainWindow", "更新OB文件"))
        self.label_3.setText(_translate("MainWindow", "OB文件"))
        self.label_4.setText(_translate("MainWindow", "图片文件"))
        self.label_5.setText(_translate("MainWindow", "图片文件写入OB文件"))
        self.checkBox.setText(_translate("MainWindow", "背景黑色"))

