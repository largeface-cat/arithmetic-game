# [file name]: main.py
# [file content begin]
import sys
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

from gui import Ui_MainWindow
from utils import generate_expression
from settings_window import SettingsWindow  # 导入设置窗口

class MathGameWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, settings):
        super().__init__()
        self.setupUi(self)
        
        # 保存用户设置
        self.settings = settings
        
        # 初始化游戏状态
        self.score = 0
        self.time_left = 120  # 120秒倒计时
        self.game_active = True
        
        # 设置UI
        self.CountDownLabel.setText(f"Time: {self.time_left}s")
        self.ScoreLabel.setText("Score: 0")
        
        # 生成第一个算式
        self.generate_new_expression()
        
        # 连接信号
        self.UserInput.returnPressed.connect(self.check_answer)
        
        # 设置定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # 每秒更新一次
    
    def generate_new_expression(self):
        """使用用户设置生成新算式"""
        self.expression, self.correct_answer = generate_expression(self.settings)
        self.Display.setText(self.expression)
        self.UserInput.clear()
        self.UserInput.setFocus()  # 自动聚焦到输入框
    
    def check_answer(self):
        if not self.game_active:
            return
            
        try:
            user_answer = int(self.UserInput.text())
            if user_answer == self.correct_answer:
                self.score += 1
            else:
                self.score -= 1
            self.ScoreLabel.setText(f"Score: {self.score}")
        except ValueError:
            # 输入不是整数，不计分
            pass
        
        # 生成新算式
        self.generate_new_expression()
    
    def update_timer(self):
        if not self.game_active:
            return
            
        self.time_left -= 1
        self.CountDownLabel.setText(f"Time: {self.time_left}s")
        
        if self.time_left <= 0:
            self.game_active = False
            self.timer.stop()
            self.Display.setText(f"Final Score: {self.score}")
            self.UserInput.clear()
            self.UserInput.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 显示设置窗口
    settings_dialog = SettingsWindow()
    if settings_dialog.exec_() != QDialog.Accepted:
        sys.exit(0)  # 用户取消，退出程序
    
    # 获取用户设置
    game_settings = settings_dialog.get_settings()
    
    # 显示主游戏窗口
    window = MathGameWindow(game_settings)
    window.show()
    app.exec()
# [file content end]