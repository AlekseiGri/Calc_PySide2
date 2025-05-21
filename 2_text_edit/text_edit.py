from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QFileDialog

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Editor text")
        self.setGeometry(300,250,350,200)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit) 

        self.createMenuBar()



    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("File", self)
        self.menuBar.addMenu(fileMenu)

        fileMenu.addAction('Open', self.action_clicked)
        fileMenu.addAction('Save', self.action_clicked)

    @Slot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == "Open":
            fname = QFileDialog.getOpenFileName(self)[0]

            try:
                f = open(fname, 'r')
                with f: 
                    data = f.read()
                    self.text_edit.setText(data)

                f.close()
            except FileNotFoundError: 
                print ("No such file")


        elif action.text() == "Save":
            fname = QFileDialog.getSaveFileName(self)[0]
            try:
                f = open(fname, 'w')
                text =self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print ("No such file")
           


        # open_file = fileMenu.addMenu("Open")
        # open_file = fileMenu.addMenu("Save")


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()

