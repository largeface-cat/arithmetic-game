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
        self.CountDownLabel.setGeometry(QtCore.QRect(420, 50, 300, 30))
        self.CountDownLabel.setObjectName("CountDownLabel")
        self.CountDownLabel.setFont(QtGui.QFont("Arial", 14))
        
        # 分数标签
        self.ScoreLabel = QtWidgets.QLabel(self.centralwidget)
        self.ScoreLabel.setGeometry(QtCore.QRect(420, 100, 300, 30))
        self.ScoreLabel.setObjectName("ScoreLabel")
        self.ScoreLabel.setFont(QtGui.QFont("Arial", 14))

        # 上一题用时标签
        self.LastTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.LastTimeLabel.setGeometry(QtCore.QRect(420, 150, 300, 30))
        self.LastTimeLabel.setObjectName("LastTimeLabel")
        self.LastTimeLabel.setFont(QtGui.QFont("Arial", 12))
        self.LastTimeLabel.setText("Last interval: N/A")
        
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

        # 游戏结束按钮区域
        self.game_over_widget = QtWidgets.QWidget(self.centralwidget)
        self.game_over_widget.setGeometry(QtCore.QRect(150, 300, 400, 150))
        self.game_over_widget.setObjectName("game_over_widget")
        self.game_over_layout = QtWidgets.QVBoxLayout(self.game_over_widget)
        self.game_over_layout.setAlignment(QtCore.Qt.AlignCenter)

        # Play Again 按钮
        self.play_again_btn = QtWidgets.QPushButton("Play Again")
        self.play_again_btn.setFixedSize(200, 50)
        self.play_again_btn.setFont(QtGui.QFont("Arial", 12))
        self.game_over_layout.addWidget(self.play_again_btn, 0, QtCore.Qt.AlignCenter)

        # Relaunch 按钮
        # self.relaunch_btn = QtWidgets.QPushButton("Relaunch")
        # self.relaunch_btn.setFixedSize(200, 50)
        # self.relaunch_btn.setFont(QtGui.QFont("Arial", 12))
        # self.game_over_layout.addWidget(self.relaunch_btn, 0, QtCore.Qt.AlignCenter)

        # 初始隐藏游戏结束按钮
        self.game_over_widget.setVisible(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Arithmetic game"))
        self.CountDownLabel.setText(_translate("MainWindow", "Time: 120s"))
        self.ScoreLabel.setText(_translate("MainWindow", "Score: 0"))
        self.LastTimeLabel.setText(_translate("MainWindow", "Last interval: N/A"))
        self.TitleLabel.setText(_translate("MainWindow", "Arithmetic game"))
# [file content end]