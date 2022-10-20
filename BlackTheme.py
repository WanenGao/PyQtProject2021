import os

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import jieba
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont, QPalette, QIcon, QBrush, QCursor, QTextCursor
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView, QTableWidgetItem, QTableWidget, QMainWindow, QLineEdit
import pandas as pd
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import pygame
import time

class Ui_nihao(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_nihao,self).__init__()
        # 小框在屏幕的位置
        self.left = 1600
        self.top = 10
        self.width = 120
        self.height = 50
        self.setObjectName("nihao")
        self.resize(100, 50)
        self.setWindowTitle("单号")
        self.number = QLineEdit(self)
        desktop = QApplication.desktop()
        self.number.move(10, 5)
        self.number.resize(100, 40)
        self.setGeometry(desktop.width()*0.01, desktop.height()*0.55, self.width, self.height)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


class XX(QMainWindow):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.haoN = Ui_nihao()
        self.haoN.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # 置顶
        self.haoN.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.haoN.show()
        self.haoN.number.home(False)  # 移动光标到最左边

        self.haoN.number.setFocus()
        # cursor = self.haoN.number.textCursor()
        # cursor.movePosition(QTextCursor.End)  # 还可以有别的位置
        # self.haoN.setTextCursor(cursor)
        self.left = 10
        self.top = 670
        self.width = 320
        self.height = 200
        print("nihao")
        desktop = QApplication.desktop()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(desktop.width()*0.001, desktop.height()*0.6, self.width, self.height)
        #MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.resize(549, 380)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet('''
            QWidget#centralwidget{border-radius:10px;}
        ''')
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 55, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130,55, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 80, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 180, 80, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 95, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.df = pd.read_excel("./Example.xlsx")
        self.name = ''

        def messageDialog():
            # 核心功能代码就两行，可以加到需要的地方
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有该单号')
            msg_box.exec_()

        def danhao_finish_slot1():
            if self.danhao.hasFocus() or self.haoN.number.hasFocus():
                if self.danhao.hasFocus() and self.danhao.text() is not self.haoN.number.text() and self.danhao.text():
                    dh = self.danhao.text()
                elif self.haoN.number.hasFocus() and self.haoN.number.text() is not self.danhao.text() and self.haoN.number.text():
                    dh = self.haoN.number.text()
                else:
                    if self.danhao.text():
                        dh = self.danhao.text()
                    else:
                        dh = self.haoN.number.text()
                self.danhao.setText(dh)
                self.haoN.number.setText(dh)
                print(dh)
                print(self.df)
                self.df["订单号"] = self.df["订单号"].apply(str)
                print(dh in self.df["订单号"].values)
                if dh in self.df["订单号"].values:
                    print(type(dh))
                    self.name = self.df[self.df["订单号"]==dh].iloc[0,1]
                    # self.name = self.df.query('订单号=='+dh).iloc[0,1]
                    self.fengxianzhi.setStyleSheet("color: black;")
                    self.fengxianzhi.setText(str(round(self.df[self.df["订单号"]==dh].iloc[0, 5])))
                    if int(self.fengxianzhi.text()) > 90:

                        self.dengji.setStyleSheet("color: red;")
                        self.fengxianzhi.setStyleSheet("color: red;")
                        self.yingduifangan.setText("ABCD")

                        MainWindow.showNormal()
                        # MainWindow.showMaximized()
                        pygame.init()
                        track = pygame.mixer.music.load(r"./music.mp3")
                        pygame.mixer.music.play(loops=3, start=0.0)
                        pygame.mixer.music.set_volume(0.5) #音量 0.0到1.0
                        # time.sleep(5)
                        # pygame.mixer.music.stop()
                    else:
                        if int(self.fengxianzhi.text()) > 80:
                            self.dengji.setStyleSheet("color: orange;")
                            self.fengxianzhi.setStyleSheet("color: orange;")
                            self.yingduifangan.setText("ABC")
                        else:
                            if int(self.fengxianzhi.text()) > 60:
                                # self.dengji.setStyleSheet("color: yellow;")
                                # self.fengxianzhi.setStyleSheet("color: yellow;")
                                self.dengji.setStyleSheet("QLineEdit{color:rgb(204,204,51);}")
                                self.fengxianzhi.setStyleSheet("QLineEdit{color:rgb(204,204,51);}")
                                self.yingduifangan.setText("AB")
                            else:
                                self.fengxianzhi.setStyleSheet("color: black;")
                                self.dengji.setStyleSheet("color: black;")
                                self.yingduifangan.setText("无")
                    self.dengji.setText(str(round(self.df[self.df["订单号"]==dh].iloc[0, 6]))+"级")
                    print(self.name)
                    MainWindow.showNormal()
                    finish_slot()
                elif self.danhao is None:
                    #do nothing
                    print()
                else:
                    messageDialog()
                    self.danhao.clear()
                    self.haoN.number.clear()
                    self.fencikuang.setRowCount(0)
                    self.fencikuang.clearContents()
                    self.miaoshu.clear()
                    self.dengji.clear()
                    self.fengxianzhi.clear()
                    self.yingduifangan.clear()


        def danhao_finish_slot2(danhao):
            self.danhao.setText(danhao)
            dh = self.danhao.text()
            #print(danhao)
            print(dh)
            print(self.df)
            self.name = self.df.query('订单号==' + str(dh)).iloc[0, 1]
            self.fengxianzhi.setStyleSheet("color: black;")
            self.fengxianzhi.setText(str(round(self.df.query('订单号==' + str(dh)).iloc[0, 5])))
            self.dengji.setStyleSheet("color: black;")
            self.dengji.setText(str(round(self.df.query('订单号==' + str(dh)).iloc[0, 6])) + "级")
            print(self.name)
            finish_slot()
        # def danhao_finish_slot2():
        #     self.browser.page().runJavaScript('getdanhao();', js_callback)


        self.danhao = QtWidgets.QLineEdit(self.centralwidget)
        self.danhao.setGeometry(QtCore.QRect(75, 70, 221, 30))
        self.danhao.setObjectName("danhao")
        self.danhao.setPlaceholderText("请输入单号")
        self.danhao.setStyleSheet('''QLineEdit{
        border:1px solid gray;
        width:300px;
        border-top-right-radius: 10px;
        border-bottom-right-radius: 10px;
        padding:20x 4px;
        }
        ''')

        self.sound = QSound('music.mp3')
        self.sound.setLoops(QSound.Infinite)  # 1

        #self.play_btn.clicked.connect(self.sound.play)
        #self.stop_btn.clicked.connect(self.sound.stop)


        #self.danhao.editingFinished.connect(danhao_finish_slot1)
        self.danhao.editingFinished.connect(danhao_finish_slot1)
        #self.danhao.textEdited.connect(danhao_finish_slot1)
        #self.haoN.number.textEdited.connect(danhao_finish_slot1)
        self.haoN.number.editingFinished.connect(danhao_finish_slot1)
        #danhao_finish_slot2()
        #self.signal1.connect(execute)


        self.changelist = pd.DataFrame({'物品名称':[],'修改':[]})

        self.fencikuang = QTableWidget(self.centralwidget)


        self.fencikuang.verticalHeader().setHidden(True)
        self.fencikuang.setStyleSheet('''QTableWidget{
                    color:#DCDCDC;
                    background:#444444;
                    border:1px solid #242424;
                    alternate-background-color:#525252;/*交错颜色*/
                    gridline-color:#242424;
                    }
                    QTableWidget::item:selected{
color:#DCDCDC;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);
}

/*
悬浮item*/
QTableWidget::item:hover{
background:#5B5B5B;
}
/*表头*/
QHeaderView::section{
text-align:center;
background:#5E5E5E;
padding:3px;
margin:0px;
color:#DCDCDC;
border:1px solid #242424;
border-left-width:0;
}



/*表右侧的滑条*/
QScrollBar:vertical{
background:#484848;
padding:0px;
border-radius:6px;
max-width:12px;
}

/*滑块*/
QScrollBar::handle:vertical{
background:#CCCCCC;
}
/*
滑块悬浮，按下*/
QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{
background:#A7A7A7;
}
/*
滑块已经划过的区域*/
QScrollBar::sub-page:vertical{
background:444444;
}

/*
滑块还没有划过的区域*/
QScrollBar::add-page:vertical{
background:5B5B5B;
}

/*页面下移的按钮*/
QScrollBar::add-line:vertical{
background:none;
}
/*页面上移的按钮*/
QScrollBar::sub-line:vertical{
background:none;
}
                        ''')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fencikuang.setFont(font)

        self.fencikuang.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置表格的选取方式是行选取
        self.fencikuang.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置选取方式为单个选取

        self.fencikuang.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.fencikuang.setGeometry(QtCore.QRect(340, 0, 211, 351))
        self.fencikuang.setObjectName("fencikuang")

        self.fencikuang.setRowCount(0)
        self.fencikuang.setColumnCount(2)
        self.fencikuang.setHorizontalHeaderLabels(['物品名称', '修改'])
        # self.fencikuang.setStyleSheet('''QTableWidget{
        #
        #
        #                                         }
        #                                         ''')

        self.seg_list = []
        # 描述内容分词
        def finish_slot():
            ms = self.name
            self.miaoshu.setText(ms)
            print(ms)
            import jieba  # 需要另外加载一个词性标注模块
            jieba.set_dictionary(".\dict.txt")
            jieba.initialize()
            import jieba.posseg
            #string = '其实大家买手机就是看个心情，没必要比来比去的。'
            seg = jieba.posseg.cut(ms)
            l = []
            for i in seg:
                if i.flag == 'n':
                    l.append(i.word)
            print(l)

            self.seg_list = l

            self.fencikuang.setRowCount(len(self.seg_list))
            self.fencikuang.setColumnCount(2)
            self.fencikuang.setHorizontalHeaderLabels(['物品名称', '修改'])

            for row in range(len(self.seg_list)):
                for column in range(2):
                    item = QStandardItem('row %s,column %s' % (row, column))
                    self.fencikuang.setItem(row, 0, QTableWidgetItem(self.seg_list[row]))

            for row in range(len(self.seg_list)):
                item = QTableWidgetItem(self.seg_list[row])
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.fencikuang.setItem(row,0,item)

            # update
            def table_update():
                row_select = self.fencikuang.selectedItems()
                if len(row_select) == 0 or row_select[1].text()=='':
                    return
                id = row_select[0].text()
                new_name = row_select[1].text()
                print("物品名称: {}, 修改: {}".format(id, new_name))
                df2 = pd.DataFrame([[id, new_name]], columns=('物品名称','修改'))
                if any(self.changelist['物品名称'] == id):
                    index = self.changelist[self.changelist["物品名称"]==str(id)].index.tolist()[0]
                    print(index)
                    self.changelist.iat[index,1] = new_name
                else:
                    self.changelist = self.changelist.append(df2, ignore_index=True)
                print(self.changelist)

            self.fencikuang.itemChanged.connect(table_update)


        self.miaoshu = QtWidgets.QTextEdit(self.centralwidget)
        self.miaoshu.setGeometry(QtCore.QRect(75, 130, 221, 30))#20, 130,55, 30
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(10)
        self.miaoshu.setFont(font)
        self.miaoshu.setObjectName("miaoshu")
        self.miaoshu.setStyleSheet('''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
                padding:20x 4px;
                }
                ''')


        self.fengxianzhi = QtWidgets.QLineEdit(self.centralwidget)
        self.fengxianzhi.setGeometry(QtCore.QRect(90, 180, 71, 60)) #20, 180, 80, 60
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.fengxianzhi.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        self.fengxianzhi.setFont(font)
        self.fengxianzhi.setObjectName("fengxianzhi")
        self.fengxianzhi.setStyleSheet('''QLineEdit{
                                        border:1px solid gray;
                                        width:300px;
                                        border-top-right-radius: 10px;
                                        border-bottom-right-radius: 10px;
                                        padding:20x 4px;
                                        }
                                        ''')

        self.dengji = QtWidgets.QLineEdit(self.centralwidget)
        self.dengji.setGeometry(QtCore.QRect(230, 180, 65, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.dengji.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.dengji.setFont(font)
        self.dengji.setObjectName("dengji")
        self.dengji.setStyleSheet('''QLineEdit{
                                border:1px solid gray;
                                width:300px;
                                border-top-right-radius: 10px;
                                border-bottom-right-radius: 10px;
                                padding:20x 4px;
                                }
                                ''')

        self.yingduifangan = QtWidgets.QTextEdit(self.centralwidget)
        self.yingduifangan.setGeometry(QtCore.QRect(115, 270, 181, 30))#20, 270, 75, 30
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yingduifangan.setFont(font)
        self.yingduifangan.setObjectName("yingduifangan")
        self.yingduifangan.setStyleSheet('''QLineEdit{
                        border:1px solid gray;
                        width:300px;
                        border-top-right-radius: 10px;
                        border-bottom-right-radius: 10px;
                        padding:20x 4px;
                        }
                        ''')
            

        @pyqtSlot()
        def tijiao():
            global danhao0
            self.changelist[['物品名称']].to_csv('result1.csv', mode='a', header=False)
            self.changelist.to_csv('result2.csv', mode='a', header=False)
            self.fencikuang.setRowCount(0)
            self.fencikuang.clearContents()
            self.danhao.clear()
            self.haoN.number.clear()
            self.miaoshu.clear()
            self.dengji.clear()
            self.fengxianzhi.clear()
            self.changelist.drop(self.changelist.index, inplace=True)
            self.yingduifangan.clear()
            danhao0 = ''
            # cursor = self.danhao.textCursor()
            # cursor.movePosition(QTextCursor.End)  # 还可以有别的位置
            # self.danhao.setTextCursor(cursor)
            MainWindow.showMinimized()
            self.sound.stop()
            #MainWindow.setWindowFlags(Qt.WindowStaysOnBottomHint)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 320, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect( lambda:tijiao())
        # spin_icon = qtawesome.icon('fa5s.microphone-alt', color='white')
        # self.pushButton.setIcon(spin_icon)  # 设置图标
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setStyleSheet('''QPushButton{border:none;}
                QPushButton:hover{color:white;
                            border:2px solid #F3F3F5;
                            border-radius:35px;
                            background:darkGray;}''')



        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "风险识别"))
        self.label.setText(_translate("MainWindow", "单号"))
        # self.label.setStyleSheet('''QLabel{color:darkGray;background:white;border:2px solid #F3F3F5;border-radius:100px;
        #                 font-size:12pt; font-weight:400;} ''')
        self.label.setStyleSheet('''QLabel{color:#232C51;
        background:white;
        border-top:1px solid darkGray;
        border-bottom:1px solid darkGray;
        border-right:1px solid darkGray;
        border-top-left-radius:10px;
        border-bottom-left-radius:10px;} ''')

        self.label_2.setText(_translate("MainWindow", "描述"))
        self.label_2.setStyleSheet('''QLabel{color:#232C51;
        background:white;
        border-top:1px solid darkGray;
        border-bottom:1px solid darkGray;
        border-right:1px solid darkGray;
        border-top-left-radius:10px;
        border-bottom-left-radius:10px;} ''')
        self.label_3.setText(_translate("MainWindow", "风险值"))
        self.label_3.setStyleSheet('''QLabel{color:#232C51;
                        background:white;
                        border-top:1px solid darkGray;
                        border-bottom:1px solid darkGray;
                        border-right:1px solid darkGray;
                        border-top-left-radius:10px;
                        border-bottom-left-radius:10px;} ''')
        self.label_4.setText(_translate("MainWindow", "等级"))
        self.label_4.setStyleSheet('''QLabel{color:#232C51;
                        background:white;
                        border-top:1px solid darkGray;
                        border-bottom:1px solid darkGray;
                        border-right:1px solid darkGray;
                        border-top-left-radius:10px;
                        border-bottom-left-radius:10px;} ''')
        self.label_5.setText(_translate("MainWindow", "应对方案"))
        self.label_5.setStyleSheet('''QLabel{color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;} ''')
        self.pushButton.setText(_translate("MainWindow", "确定"))
        #self.miaoshu.setText(_translate("MainWindow", "枕头立刻进入可俯瞰发来的佛教而外来人口虽然"))
        #self.fengxianzhi.setText(_translate("MainWindow", "90"))
        #self.dengji.setText(_translate("MainWindow", "二级"))
        #self.yingduifangan.setText(_translate("MainWindow", "拿去检验"))
        self.label_6.setText(_translate("MainWindow", "风险识别"))
        MainWindow.setWindowOpacity(0.9)  # 设置窗口透明度
        # Ui_MainWindow3.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        pe = QPalette()
        MainWindow.setAutoFillBackground(True)
        pe.setColor(QPalette.Window,Qt.lightGray)  # 设置背景色
        # pe.setColor(QPalette.Background,Qt.blue)
        MainWindow.setPalette(pe)



