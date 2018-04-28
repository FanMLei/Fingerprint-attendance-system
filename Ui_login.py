# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\fml\Desktop\Eric\login.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import my_icon_rc
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(430, 328)
        Dialog.setMaximumSize(QtCore.QSize(430, 328))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/finger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-1, -1, 431, 180))
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 280, 191, 31))
        self.pushButton_3.setStyleSheet("border-image: url(:/icon/OK.png);")
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/OK.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(160, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(115, 40, 200, 90))
        self.textBrowser.setTabletTracking(False)
        self.textBrowser.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.textBrowser.setStyleSheet("background-image: url(:/icon/name.png);")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 235, 191, 28))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 200, 191, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 10, 24, 24))
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/minisize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(400, 10, 24, 24))
        self.pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 200, 61, 61))
        self.label_2.setStyleSheet("\n"
"image: url(:/icon/Default head image.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(305, 201, 25, 25))
        self.pushButton_4.setStyleSheet("background-image: url(:/icon/delete.png);")
        self.pushButton_4.setText("")
        self.pushButton_4.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(305, 236, 25, 25))
        self.pushButton_5.setStyleSheet("background-image: url(:/icon/delete.png);")
        self.pushButton_5.setText("")
        self.pushButton_5.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 290, 27, 24))
        self.pushButton_6.setStyleSheet("background-image: url(:/icon/register.PNG);")
        self.pushButton_6.setText("")
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(380, 280, 47, 47))
        self.pushButton_7.setStyleSheet("background-image: url(:/icon/finger_login.jpg);\n"
"background-image: url(:/icon/finger_login.png);")
        self.pushButton_7.setText("")
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "用户登录"))
        self.lineEdit.setText(_translate("Dialog", "1"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
