import re
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='AimerYoung@0207',
    database='teachersys',
    cursorclass=pymysql.cursors.DictCursor
)

def check_quotes(input_string):
    if input_string is None:
        return False

    # 方法一：使用正则表达式
    if re.search(r"[\'\"]", input_string):
        return True

    # 方法二：使用字符串方法
    if "'" in input_string or '"' in input_string:
        return True

    return False

def check_date_format(input_string):
    pattern = r'^\d{4}-\d{2}-\d{2}$'  # 匹配形式为 "xxxx-xx-xx" 的正则表达式

    if re.match(pattern, input_string):
        return True
    else:
        return False
    
def check_year_format(input_string):
    pattern = r'^\d{4}$'  # 匹配形式为 "xxxx" 的正则表达式

    if re.match(pattern, input_string):
        return True
    else:
        return False
