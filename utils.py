# [file name]: utils.py
# [file content begin]
import random

def generate_expression(settings):
    operators = ['+', '-', '*', '/']
    op = random.choice(operators)
    
    if op == '+':
        # 使用加法设置
        x_min = settings["add"]["x_min"]
        x_max = settings["add"]["x_max"]
        y_min = settings["add"]["y_min"]
        y_max = settings["add"]["y_max"]
        
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        result = x + y
    elif op == '-':
        # 使用减法设置
        x_min = settings["sub"]["x_min"]
        x_max = settings["sub"]["x_max"]
        y_min = settings["sub"]["y_min"]
        y_max = settings["sub"]["y_max"]
        
        # 确保结果非负
        x = random.randint(max(x_min, y_min), x_max)
        y = random.randint(y_min, min(y_max, x))  # y不超过x
        result = x - y
    elif op == '*':
        # 使用乘法设置
        x_min = settings["mul"]["x_min"]
        x_max = settings["mul"]["x_max"]
        y_min = settings["mul"]["y_min"]
        y_max = settings["mul"]["y_max"]

        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        result = x * y
        
        result = x * y
    else:  # division
        # 使用除法设置
        y_min = settings["div"]["y_min"]
        y_max = settings["div"]["y_max"]
        result_min = settings["div"]["result_min"]
        result_max = settings["div"]["result_max"]
        
        # 确保结果为整数
        y = random.randint(y_min, y_max)
        result = random.randint(result_min, result_max)
        x = y * result
    
    return f"{x} {op} {y}", result
# [file content end]