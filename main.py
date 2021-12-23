import sys
import os

import pymysql

from PyQt5.QtWidgets import *

from loginUI import Ui_MainWindow as loginUi
# -p E:\python\pycharm\passwordmanager\venv\Lib\site-packages

# 主窗口
class loginWindow(QMainWindow, loginUi):
    def __init__(self):
        super(loginWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.exit)
        self.pushButton.clicked.connect(self.connect)

    def connect(self):
        un = self.lineEdit.text()
        pw = self.lineEdit_2.text()
        if un == '' or pw == '':
            msg_box = QMessageBox(QMessageBox.Warning, '错误', '账号或密码不可为空')
            msg_box.exec_()
        else:
            # print("un : ", un)
            # print("pw : ", pw)
            # pyinstaller -c -F -w main.py -p E:\python\pycharm\passwordmanager\venv\Lib\site-packages
            try:
                connect = pymysql.Connect(host='localhost', port=3306, user=un, password=pw, database='passwords',
                                          charset='utf8')
                print("success")
                connect.close()
                self.close()
                os.system(
                    f"E:\\python\\pycharm\\passwordmanager\\venv\\Scripts\\python.exe E:\\python\\pycharm\\passwordmanager\\mainWindow.py {un} {pw}")

            except pymysql.err.OperationalError:
                msg_box = QMessageBox(QMessageBox.Warning, '错误', '密码错误')
                msg_box.exec_()
            except:
                msg_box = QMessageBox(QMessageBox.Warning, '错误', '其他错误')
                msg_box.exec_()

    @staticmethod
    def exit():
        exit(0)


if __name__ == '__main__':
    # 初始化APP
    app = QApplication(sys.argv)

    # 创建主窗口
    win = loginWindow()

    # 绘制窗口
    win.show()

    # 循环绘制
    sys.exit(app.exec_())
