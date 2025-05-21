# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWidgets import QMessageBox # для всплывающего окна


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_result = QLabel(self.centralwidget)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setGeometry(QRect(0, 0, 400, 50))
        font = QFont()
        font.setFamily(u"MS Mincho")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet(u"background-color: rgb(48, 96, 71);\n"
"color: rgb(255, 255, 255)")
        self.label_result.setMargin(10)
        self.btn_zero = QPushButton(self.centralwidget)
        self.btn_zero.setObjectName(u"btn_zero")
        self.btn_zero.setGeometry(QRect(0, 330, 150, 70))
        font1 = QFont()
        font1.setPointSize(30)
        self.btn_zero.setFont(font1)
        self.btn_zero.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.btn_equal = QPushButton(self.centralwidget)
        self.btn_equal.setObjectName(u"btn_equal")
        self.btn_equal.setGeometry(QRect(150, 330, 150, 70))
        self.btn_equal.setFont(font1)
        self.btn_equal.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setGeometry(QRect(0, 236, 100, 94))
        self.btn_7.setFont(font1)
        self.btn_7.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setGeometry(QRect(0, 142, 100, 94))
        self.btn_4.setFont(font1)
        self.btn_4.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setGeometry(QRect(0, 48, 100, 94))
        self.btn_1.setFont(font1)
        self.btn_1.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setGeometry(QRect(100, 236, 100, 94))
        self.btn_8.setFont(font1)
        self.btn_8.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setGeometry(QRect(100, 48, 100, 94))
        self.btn_2.setFont(font1)
        self.btn_2.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setGeometry(QRect(100, 142, 100, 94))
        self.btn_5.setFont(font1)
        self.btn_5.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setGeometry(QRect(200, 48, 100, 94))
        self.btn_3.setFont(font1)
        self.btn_3.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setGeometry(QRect(200, 142, 100, 94))
        self.btn_6.setFont(font1)
        self.btn_6.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setGeometry(QRect(200, 236, 100, 94))
        self.btn_9.setFont(font1)
        self.btn_9.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        self.btn_plus.setGeometry(QRect(300, 48, 100, 94))
        self.btn_plus.setFont(font1)
        self.btn_plus.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.btn_minus = QPushButton(self.centralwidget)
        self.btn_minus.setObjectName(u"btn_minus")
        self.btn_minus.setGeometry(QRect(300, 142, 100, 94))
        self.btn_minus.setFont(font1)
        self.btn_minus.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.btn_raise = QPushButton(self.centralwidget)
        self.btn_raise.setObjectName(u"btn_raise")
        self.btn_raise.setGeometry(QRect(300, 236, 100, 94))
        self.btn_raise.setFont(font1)
        self.btn_raise.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.btn_fission = QPushButton(self.centralwidget)
        self.btn_fission.setObjectName(u"btn_fission")
        self.btn_fission.setGeometry(QRect(300, 330, 100, 70))
        self.btn_fission.setFont(font1)
        self.btn_fission.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"color: rgb(0, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.add_function() # запуск функции обработки

        self.is_equal = False # флаг резета
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.label_result.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_raise.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_fission.setText(QCoreApplication.translate("MainWindow", u"/", None))

 # тут начинается логика программы

    def add_function(self):
        self.btn_zero.clicked.connect(lambda: self.write_number(self.btn_zero.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_raise.clicked.connect(lambda: self.write_number(self.btn_raise.text()))
        self.btn_fission.clicked.connect(lambda: self.write_number(self.btn_fission.text()))

        self.btn_equal.clicked.connect(self.results)

    def write_number(self, number):
      if self.label_result.text() == "0" or self.is_equal:
           self.label_result.setText(number)
           self.is_equal = False
      else:     
        self.label_result.setText(self.label_result.text() + number)
    def results(self):
     if not self.is_equal:
      res = eval(self.label_result.text())
      self.label_result.setText("Result: " + str(res))
      self.is_equal = True
     else:
        error = QMessageBox()
        error.setWindowTitle("error")
        error.setText("don push '=' again")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Reset)
        error.setDefaultButton(QMessageBox.Ok)
        error.setInformativeText("I have no idea")
        error.setDetailedText("More information")

        error.buttonClicked.connect(self.popup_action)

        error.exec_()
 
    def popup_action (self, btn):
     if btn.text() == "Ok":
        print ("Ok")
     elif btn.text() == "Reset":
      self.label_result.setText("")
      self.is_equal = False

    # retranslateUi

# тут заканчивается логика

# во время запуска скрипта pyside2-uic функция main не добовляется 
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
