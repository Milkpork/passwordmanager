import sys

import pymysql

from inputText import Ui_MainWindow
from PyQt5.QtWidgets import *


# 主窗口
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.lineEdit.setText(sys.argv[3])
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setText(sys.argv[4])
        self.lineEdit_3.setText(sys.argv[5])
        self.lineEdit_4.setText(sys.argv[6])

        self.pushButton.clicked.connect(self.update)

    def update(self):
        connect = pymysql.Connect(host='localhost', port=3306, user=sys.argv[1], password=sys.argv[2],
                                  database='passwords',
                                  charset='utf8')
        cursor = connect.cursor()  # 执行完毕返回的结果集默认以元组显示
        try:
            platform = self.lineEdit.text()
            user_name = self.lineEdit_2.text()
            password = self.lineEdit_3.text()
            if platform == '' or user_name == '' or password == '':
                raise ValueError
            addition = self.lineEdit_4.text() if self.lineEdit_4.text() != '' else 'null'
            sql = f'update pw set user_password="{password}", user_name="{user_name}", addition="{addition}" where platform="{platform}"'
            cursor.execute(sql)
            connect.commit()
            msg_box = QMessageBox(QMessageBox.Information, '成功', '修改成功')
            msg_box.exec_()
            cursor.close()
            connect.close()
            exit(0)
        except ValueError:
            msg_box = QMessageBox(QMessageBox.Information, '错误', '修改失败')
            msg_box.exec_()



if __name__ == '__main__':
    # 初始化APP
    app = QApplication(sys.argv)

    # 创建主窗口
    win = MainWindow()

    # 绘制窗口
    win.show()
    # 循环绘制
    sys.exit(app.exec_())
