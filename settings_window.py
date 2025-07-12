# [file name]: settings_window.py
# [file content begin]
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QGridLayout, QLabel, QLineEdit, 
    QPushButton, QGroupBox, QMessageBox, QCheckBox, QComboBox, QHBoxLayout
)
from PyQt5.QtCore import Qt

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Game Settings")
        self.setFixedSize(800, 600)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        # 添加自定义帮助按钮
        self.help_btn = QPushButton("?", self)
        self.help_btn.setGeometry(self.width() - 30, 0, 20, 20)
        self.help_btn.setStyleSheet("""
            QPushButton {
                font-weight: bold;
                font-size: 14px;
                border-radius: 5px;
                background-color: #3498db;
                color: white;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.help_btn.clicked.connect(self.show_help_dialog)
        
        # 默认值
        self.defaults = {
            "add": {"x_min": 1, "x_max": 199, "y_min": 1, "y_max": 199},
            "sub": {"x_min": 1, "x_max": 199, "y_min": 1, "y_max": 199},
            "mul": {"x_min": 1, "x_max": 99, "y_min": 1, "y_max": 19},
            "div": {"y_min": 1, "y_max": 99, "result_min": 1, "result_max": 19}
        }
        
        self.settings = self.defaults.copy()
        self.init_ui()
    
    def init_ui(self):
        main_layout = QVBoxLayout()
        
        # 加法设置组
        add_group = QGroupBox("Addition Settings")
        add_layout = QGridLayout()
        
        add_layout.addWidget(QLabel("x min:"), 0, 0)
        self.add_x_min = QLineEdit(str(self.defaults["add"]["x_min"]))
        add_layout.addWidget(self.add_x_min, 0, 1)
        
        add_layout.addWidget(QLabel("x max:"), 1, 0)
        self.add_x_max = QLineEdit(str(self.defaults["add"]["x_max"]))
        add_layout.addWidget(self.add_x_max, 1, 1)
        
        add_layout.addWidget(QLabel("y min:"), 0, 2)
        self.add_y_min = QLineEdit(str(self.defaults["add"]["y_min"]))
        add_layout.addWidget(self.add_y_min, 0, 3)
        
        add_layout.addWidget(QLabel("y max:"), 1, 2)
        self.add_y_max = QLineEdit(str(self.defaults["add"]["y_max"]))
        add_layout.addWidget(self.add_y_max, 1, 3)
        
        add_group.setLayout(add_layout)
        main_layout.addWidget(add_group)
        
        # 减法设置组
        sub_group = QGroupBox("Subtraction Settings")
        sub_layout = QGridLayout()
        
        sub_layout.addWidget(QLabel("x min:"), 0, 0)
        self.sub_x_min = QLineEdit(str(self.defaults["sub"]["x_min"]))
        sub_layout.addWidget(self.sub_x_min, 0, 1)
        
        sub_layout.addWidget(QLabel("x max:"), 1, 0)
        self.sub_x_max = QLineEdit(str(self.defaults["sub"]["x_max"]))
        sub_layout.addWidget(self.sub_x_max, 1, 1)
        
        sub_layout.addWidget(QLabel("y min:"), 0, 2)
        self.sub_y_min = QLineEdit(str(self.defaults["sub"]["y_min"]))
        sub_layout.addWidget(self.sub_y_min, 0, 3)
        
        sub_layout.addWidget(QLabel("y max:"), 1, 2)
        self.sub_y_max = QLineEdit(str(self.defaults["sub"]["y_max"]))
        sub_layout.addWidget(self.sub_y_max, 1, 3)
        
        sub_group.setLayout(sub_layout)
        main_layout.addWidget(sub_group)
        
        # 乘法设置组
        mul_group = QGroupBox("Multiplication Settings")
        mul_layout = QGridLayout()
        
        mul_layout.addWidget(QLabel("x min:"), 0, 0)
        self.mul_x_min = QLineEdit(str(self.defaults["mul"]["x_min"]))
        mul_layout.addWidget(self.mul_x_min, 0, 1)
        
        mul_layout.addWidget(QLabel("x max:"), 1, 0)
        self.mul_x_max = QLineEdit(str(self.defaults["mul"]["x_max"]))
        mul_layout.addWidget(self.mul_x_max, 1, 1)

        mul_layout.addWidget(QLabel("y min:"), 0, 2)
        self.mul_y_min = QLineEdit(str(self.defaults["mul"]["y_min"]))
        mul_layout.addWidget(self.mul_y_min, 0, 3)

        mul_layout.addWidget(QLabel("y max:"), 1, 2)
        self.mul_y_max = QLineEdit(str(self.defaults["mul"]["y_max"]))
        mul_layout.addWidget(self.mul_y_max, 1, 3)
        
        mul_group.setLayout(mul_layout)
        main_layout.addWidget(mul_group)
        
        # 除法设置组
        div_group = QGroupBox("Division Settings")
        div_layout = QGridLayout()
        
        div_layout.addWidget(QLabel("y min:"), 0, 0)
        self.div_y_min = QLineEdit(str(self.defaults["div"]["y_min"]))
        div_layout.addWidget(self.div_y_min, 0, 1)
        
        div_layout.addWidget(QLabel("y max:"), 1, 0)
        self.div_y_max = QLineEdit(str(self.defaults["div"]["y_max"]))
        div_layout.addWidget(self.div_y_max, 1, 1)
        
        div_layout.addWidget(QLabel("Result min:"), 0, 2)
        self.div_result_min = QLineEdit(str(self.defaults["div"]["result_min"]))
        div_layout.addWidget(self.div_result_min, 0, 3)
        
        div_layout.addWidget(QLabel("Result max:"), 1, 2)
        self.div_result_max = QLineEdit(str(self.defaults["div"]["result_max"]))
        div_layout.addWidget(self.div_result_max, 1, 3)
        
        div_group.setLayout(div_layout)
        main_layout.addWidget(div_group)
        
        # 添加运算符选择复选框
        self.add_enabled = QCheckBox("Enable +", self)
        self.add_enabled.setChecked(True)
        add_layout.addWidget(self.add_enabled, 0, 4)

        self.sub_enabled = QCheckBox("Enable -", self)
        self.sub_enabled.setChecked(True)
        sub_layout.addWidget(self.sub_enabled, 0, 4)

        self.mul_enabled = QCheckBox("Enable *", self)
        self.mul_enabled.setChecked(True)
        mul_layout.addWidget(self.mul_enabled, 0, 4)

        self.div_enabled = QCheckBox("Enable /", self)
        self.div_enabled.setChecked(True)
        div_layout.addWidget(self.div_enabled, 0, 4)

        # 添加时间选择下拉框
        time_group = QGroupBox("Time Settings")
        time_layout = QHBoxLayout()

        time_layout.addWidget(QLabel("Duration:"))
        self.time_combo = QComboBox()
        self.time_combo.addItems(["30s", "60s", "120s", "300s"])
        self.time_combo.setCurrentIndex(2)  # 默认选择120s
        time_layout.addWidget(self.time_combo)

        time_group.setLayout(time_layout)
        main_layout.addWidget(time_group)

        # 开始按钮
        self.start_btn = QPushButton("Start Game")
        self.start_btn.clicked.connect(self.validate_and_start)
        self.start_btn.setFixedHeight(40)
        main_layout.addWidget(self.start_btn)
        
        self.setLayout(main_layout)
    
    def validate_and_start(self):
        """验证所有输入值是否合法"""
        try:
            # 验证加法设置
            add_x_min = int(self.add_x_min.text())
            add_x_max = int(self.add_x_max.text())
            add_y_min = int(self.add_y_min.text())
            add_y_max = int(self.add_y_max.text())
            
            # 验证减法设置
            sub_x_min = int(self.sub_x_min.text())
            sub_x_max = int(self.sub_x_max.text())
            sub_y_min = int(self.sub_y_min.text())
            sub_y_max = int(self.sub_y_max.text())
            
            # 验证乘法设置
            mul_x_min = int(self.mul_x_min.text())
            mul_x_max = int(self.mul_x_max.text())
            mul_y_min = int(self.mul_y_min.text())
            mul_y_max = int(self.mul_y_max.text())
                        
            # 验证除法设置
            div_y_min = int(self.div_y_min.text())
            div_y_max = int(self.div_y_max.text())
            div_result_min = int(self.div_result_min.text())
            div_result_max = int(self.div_result_max.text())
            
            # 检查所有值是否为正整数
            all_values = [
                add_x_min, add_x_max, add_y_min, add_y_max,
                sub_x_min, sub_x_max, sub_y_min, sub_y_max,
                mul_x_min, mul_x_max, mul_y_min, mul_y_max,
                div_y_min, div_y_max, div_result_min, div_result_max
            ]
            
            if any(val <= 0 for val in all_values):
                raise ValueError("All values must be positive integers")
            
            # 检查范围是否有效 (min <= max)
            if ((self.add_enabled.isChecked() and (add_x_min > add_x_max or add_y_min > add_y_max)) or
                (self.sub_enabled.isChecked() and (sub_x_min > sub_x_max or sub_y_min > sub_y_max)) or
                (self.mul_enabled.isChecked() and (mul_x_min > mul_x_max or mul_y_min > mul_y_max)) or
                (self.div_enabled.isChecked() and (div_y_min > div_y_max or div_result_min > div_result_max))):
                raise ValueError("Min values must be less than or equal to max values")
            
            # 检查至少有一个运算符被选中
            if (not self.add_enabled.isChecked() and 
                not self.sub_enabled.isChecked() and 
                not self.mul_enabled.isChecked() and 
                not self.div_enabled.isChecked()):
                raise ValueError("Must activate at least one operator")

            # 保存启用的运算符
            enabled_ops = []
            if self.add_enabled.isChecked():
                enabled_ops.append('+')
            if self.sub_enabled.isChecked():
                enabled_ops.append('-')
            if self.mul_enabled.isChecked():
                enabled_ops.append('*')
            if self.div_enabled.isChecked():
                enabled_ops.append('/')

            # 保存时间设置
            time_text = self.time_combo.currentText()
            if time_text == "30s":
                game_time = 30
            elif time_text == "60s":
                game_time = 60
            elif time_text == "120s":
                game_time = 120
            else:  # 300秒
                game_time = 300

            # 保存设置
            self.settings = {
                "enabled_ops": enabled_ops,
                "game_time": game_time,
                "add": {
                    "x_min": add_x_min,
                    "x_max": add_x_max,
                    "y_min": add_y_min,
                    "y_max": add_y_max
                },
                "sub": {
                    "x_min": sub_x_min,
                    "x_max": sub_x_max,
                    "y_min": sub_y_min,
                    "y_max": sub_y_max
                },
                "mul": {
                    "x_min": mul_x_min,
                    "x_max": mul_x_max,
                    "y_min": mul_y_min,
                    "y_max": mul_y_max
                },

                "div": {
                    "y_min": div_y_min,
                    "y_max": div_y_max,
                    "result_min": div_result_min,
                    "result_max": div_result_max
                }
            }
            
            self.accept()  # 关闭对话框并返回接受状态
            
        except ValueError as e:
            QMessageBox.warning(self, "Invalid Input", 
                                f"Please check inputs.\nError: {str(e)}")
    
    def get_settings(self):
        """返回用户设置"""
        return self.settings

    def show_help_dialog(self):
        """显示自定义帮助对话框"""
        help_dialog = QMessageBox(self)
        help_dialog.setWindowTitle("Help")
        help_dialog.setTextFormat(Qt.RichText)
        help_dialog.setText("""
            <h3>Game Help</h3>
            <p><b>Addition</b>: Set the range of two numbers in addition</p>
            <p><b>Subtraction</b>: Set the range of two numbers in subtraction (result is always non-negative)</p>
            <p><b>Multiplication</b>: Set the range of two numbers in multiplication</p>
            <p><b>Division</b>: Set the range of divisor and result (result is always an integer)</p>
            <p>All values must be positive integers, and min ≤ max</p>
            <p><b>Author</b>: lsh</p>
            <a href="https://github.com/largeface-cat">Github</a>
            """)
        # 添加自定义按钮
        help_dialog.addButton("OK", QMessageBox.AcceptRole)
        help_dialog.exec()

# [file content end]