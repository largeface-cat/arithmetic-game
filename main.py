# [file name]: main.py
# [file content begin]
import sys
import time
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

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
        self.time_left = settings["game_time"]
        self.game_active = True

        # 添加计时相关变量
        self.last_time = "N/A"  # 上一题用时
        self.total_time_used = 0  # 总用时(毫秒)
        self.question_count = 0  # 题目计数
        self.start_time = None  # 当前题目开始时间
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

        # 连接按钮信号
        self.play_again_btn.clicked.connect(self.restart_game)

        # 保存设置引用
        self.game_settings = settings
    
    def generate_new_expression(self):
        self.start_time = time.time()
        self.expression, self.correct_answer = generate_expression(self.settings)
        self.Display.setText(self.expression)
        self.UserInput.clear()
        self.UserInput.setFocus()  # 自动聚焦到输入框
    
    def check_answer(self):
        flag = False
        if not self.game_active:
            return
            
        try:
            user_answer = int(self.UserInput.text())
            if user_answer == self.correct_answer:
                self.score += 1
                flag = True
            else:
                self.score -= 1
        except ValueError:
            # 输入不是整数，扣分
            self.score -= 1
        self.ScoreLabel.setText(f"Score: {self.score}")
        if self.start_time is not None:
            if flag:
                end_time = time.time()
                question_time = int((end_time - self.start_time) * 1000)  # 转换为毫秒
                self.last_time = f"{question_time} ms"
                self.LastTimeLabel.setText(f"Last interval: {self.last_time}")
                
                # 更新总用时
                self.total_time_used += question_time
                self.question_count += 1
            else:
                self.LastTimeLabel.setText(f"Last interval: N/A")
        
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
            
            # 计算平均每分用时
            if self.score > 0:
                avg_time_per_point = self.total_time_used / self.score
                avg_text = f"Avg time/score: {int(avg_time_per_point)} ms"
            else:
                avg_text = "Avg time/score: N/A"
            self.Display.setFont(QFont("Arial", 16))
            self.Display.setText(
                f"Final score: {self.score}\n{avg_text}"
            )
            
            # 禁用输入框
            self.UserInput.clear()
            self.UserInput.setEnabled(False)
            
            # 显示游戏结束按钮
            self.game_over_widget.setVisible(True)
    def restart_game(self):
        # 重置游戏状态
        self.score = 0
        self.time_left = self.game_settings["game_time"]
        self.game_active = True
        self.total_time_used = 0
        self.question_count = 0
        self.last_time = "N/A"
        
        # 更新UI
        self.ScoreLabel.setText("Score: 0")
        self.LastTimeLabel.setText("Last interval: N/A")
        self.CountDownLabel.setText(f"Time: {self.time_left}s")
        self.UserInput.setEnabled(True)
        self.game_over_widget.setVisible(False)
        self.Display.setFont(QFont("Arial", 24))
        # 重新开始计时器
        self.timer.start(1000)
        
        # 生成新算式
        self.generate_new_expression()

def main():
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

if __name__ == "__main__":
    main()
# [file content end]