# [file name]: gui.py
# [file content begin]
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # 显示算式
        self.Display = QtWidgets.QTextBrowser(self.centralwidget)
        self.Display.setGeometry(QtCore.QRect(150, 70, 256, 192))
        self.Display.setObjectName("Display")
        self.Display.setFont(QtGui.QFont("Arial", 24))
        self.Display.setAlignment(QtCore.Qt.AlignCenter)
        
        # 用户输入
        self.UserInput = QtWidgets.QLineEdit(self.centralwidget)
        self.UserInput.setGeometry(QtCore.QRect(220, 340, 113, 40))
        self.UserInput.setObjectName("UserInput")
        self.UserInput.setFont(QtGui.QFont("Arial", 14))
        self.UserInput.setAlignment(QtCore.Qt.AlignCenter)
        
        # 倒计时标签
        self.CountDownLabel = QtWidgets.QLabel(self.centralwidget)
        self.CountDownLabel.setGeometry(QtCore.QRect(420, 50, 150, 30))
        self.CountDownLabel.setObjectName("CountDownLabel")
        self.CountDownLabel.setFont(QtGui.QFont("Arial", 14))
        
        # 分数标签
        self.ScoreLabel = QtWidgets.QLabel(self.centralwidget)
        self.ScoreLabel.setGeometry(QtCore.QRect(420, 100, 150, 30))
        self.ScoreLabel.setObjectName("ScoreLabel")
        self.ScoreLabel.setFont(QtGui.QFont("Arial", 14))
        
        # 添加游戏标题
        self.TitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.TitleLabel.setGeometry(QtCore.QRect(200, 10, 400, 40))
        self.TitleLabel.setObjectName("TitleLabel")
        self.TitleLabel.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # 菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        # 状态栏
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Math Game"))
        self.CountDownLabel.setText(_translate("MainWindow", "Time: 120s"))
        self.ScoreLabel.setText(_translate("MainWindow", "Score: 0"))
        self.TitleLabel.setText(_translate("MainWindow", "Math Game"))
# [file content end]