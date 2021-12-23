import os
import sys

import pymysql
from PyQt5.QtWidgets import *

from mainUI import Ui_MainWindow


# from PyQt5.Qt5 import *

# 主窗口
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # print(sys.argv[1], sys.argv[2], sep='   ')
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.ls = []
        # 连接
        self.connect = pymysql.Connect(host='localhost', port=3306, user=sys.argv[1], password=sys.argv[2],
                                       database='passwords',
                                       charset='utf8')
        # 显示
        self.cursor = self.connect.cursor()  # 执行完毕返回的结果集默认以元组显示

        self.listWidget.itemDoubleClicked.connect(self.getup)
        self.pushButton_2.clicked.connect(self.insert)
        self.pushButton_6.clicked.connect(self.getstart)
        self.pushButton.clicked.connect(self.delete)
        self.pushButton_3.clicked.connect(self.updates)
        self.pushButton_5.clicked.connect(self.saveAndExit)

    @staticmethod
    def insert():
        os.system(
            f'E:\\python\\pycharm\\passwordmanager\\venv\\Scripts\\python.exe E:\\python\\pycharm\\passwordmanager\\insert.py {sys.argv[1]} {sys.argv[2]}')

    def delete(self):
        itemList = self.listWidget.selectedItems()
        # print(itemList)
        for i in itemList:
            sql = f'delete from pw where platform = "{i.text()}"'
            self.cursor.execute(sql)
        msg_box = QMessageBox(QMessageBox.Information, '成功', '删除成功')
        msg_box.exec_()
        self.connect.commit()

    def updates(self):
        itemList = self.listWidget.selectedItems()
        for i in itemList:
            try:
                platform = i.text()
                for j in self.ls:
                    if j[0] == platform:
                        user_name = j[1]
                        password = j[2]
                        addition = j[3]
                        break
                os.system(
                    f'E:\\python\\pycharm\\passwordmanager\\venv\\Scripts\\python.exe E:\\python\\pycharm\\passwordmanager\\update.py {sys.argv[1]} {sys.argv[2]} {platform} {user_name} {password} {addition}')
            except:
                msg_box = QMessageBox(QMessageBox.Warning, '错误', '出现了一些错误！')
                msg_box.exec_()

    def getstart(self):
        try:
            self.cursor.close()
            self.connect.close()
        except:
            pass
        self.connect = pymysql.Connect(host='localhost', port=3306, user=sys.argv[1], password=sys.argv[2],
                                       database='passwords',
                                       charset='utf8')
        self.cursor = self.connect.cursor()  # 执行完毕返回的结果集默认以元组显示
        self.listWidget.clear()
        sql = "select * from pw"
        self.cursor.execute(sql)
        self.ls = self.cursor.fetchall()
        # print(self.ls)
        for i in self.ls:
            self.listWidget.addItem(i[0])

    def getup(self, item):
        for i in self.ls:
            if i[0] == item.text():
                msg_box = QMessageBox(QMessageBox.Information, '信息', f'账号：{i[1]}\n密码：{i[2]}\n备注：{i[3]}')
                msg_box.exec_()
                break

    def saveAndExit(self):
        self.cursor.close()
        self.connect.close()
        self.close()
        exit(0)


if __name__ == '__main__':
    # 初始化APP
    app = QApplication(sys.argv)

    # 创建主窗口
    win = MainWindow()

    # 绘制窗口
    win.show()

    # 循环绘制
    sys.exit(app.exec_())
