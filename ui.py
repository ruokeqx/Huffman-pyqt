from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from huffman import HuffmanCoding
from mysocket import MySocket


class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(110, 200, 171, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(110, 110, 351, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 140, 171, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 170, 171, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 170, 171, 21))
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(290, 200, 171, 192))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 140, 171, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 410, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(470, 200, 171, 192))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 410, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 170, 171, 21))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 添加事件
        self.pushButton.clicked.connect(self.loadfile)
        self.pushButton_2.clicked.connect(self.huffmanencode)
        self.pushButton_3.clicked.connect(self.sendfile)
        self.pushButton_4.clicked.connect(self.recvfile)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Huffman Tree —— ruokeqx"))
        MainWindow.setWindowIcon(QtGui.QIcon('./ruokeqx.jpg'))
        # background
        palette = QtGui.QPalette()
        pix = Qt.QPixmap('./green.jpg')
        # pix = pix.scaled(self.width(), self.height())
        pix = pix.scaled(800, 600)
        palette.setBrush(Qt.QPalette.Background, Qt.QBrush(pix))
        MainWindow.setPalette(palette)

        self.lineEdit.setText(_translate("MainWindow", "无选中文件"))
        self.pushButton.setText(_translate("MainWindow", "选择文件"))
        self.label.setText(_translate("MainWindow", "文件内容："))
        self.label_2.setText(_translate("MainWindow", "编码结果："))
        self.pushButton_2.setText(_translate("MainWindow", "全文编码"))
        self.pushButton_3.setText(_translate("MainWindow", "发送文件"))
        self.pushButton_4.setText(_translate("MainWindow", "接收文件"))
        self.label_3.setText(_translate("MainWindow", "server端接收结果："))

    def loadfile(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, '打开文件', '.', '文本文件(*.txt)')
        filename = filepath.split('/')[-1]
        if filename != '':
            self.lineEdit.setText(filename)
            with open(filename, 'r')as f:
                filecontent = f.read()
                self.textBrowser.setText(filecontent)
        else:
            self.lineEdit.setText("无选中文件")

    def huffmanencode(self):
        filepath = self.lineEdit.text()
        h = HuffmanCoding(filepath)
        encoded_text = h.compress()
        self.textBrowser_2.setText(encoded_text)

    def sendfile(self):
        conn = MySocket()
        conn.sendfile('./huffman_test')

    def recvfile(self):
        self.textBrowser_3.setText("正在等待文件传输 请稍候")
        conn = MySocket()
        reverse_mapping = conn.recvfile()
        print(reverse_mapping)
        h = HuffmanCoding('huffman_test.txt')
        h.reverse_mapping = eval(reverse_mapping)
        decompressed_text = h.decompress('./huffman_test.bin')
        # print(decompressed_text)
        self.textBrowser_3.setText(decompressed_text)
