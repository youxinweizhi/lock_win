# -*- coding: utf-8 -*-
#by:youxinweizhi
import ctypes,time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtNetwork import QUdpSocket, QHostAddress

class Ui_Form():
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(230, 50)
        Form.setMinimumSize(QtCore.QSize(230, 50))
        Form.setMaximumSize(QtCore.QSize(230, 50))
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 201, 22))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color:red")
        #程序添加的
        self.status=0
        self.udpSocket = QUdpSocket()     #创建socket
        self.udpSocket.bind(8848)

        self.retranslateUi(Form)
        self.udpSocket.readyRead.connect(self.handleRecv)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def handleRecv(self):
        buf = bytes()
        buf, ip, port = self.udpSocket.readDatagram(1024)
        message = buf.decode()
        self.label_2.setText("distance: %s"%message+" "+"time: "+str(time.strftime("%H:%M:%S",time.localtime())))
        try:
            if len(message)<=8:
                if int(message) >80:
                    if self.status==0:
                        res=ctypes.windll.user32.LockWorkStation()
                        self.status=res
                        print(res)
                    else:
                        pass
                else:
                    self.status=0
            else:
                pass
        except ValueError:
            pass

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Auto Lock"))
        Form.setWindowIcon(QtGui.QIcon('Lock.ico'))

if __name__ == '__main__':
    import  sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())