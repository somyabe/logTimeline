# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/sagarw720/Documents/FirstProject/first.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(20, 130, 221, 16))
        self.label.setLineWidth(2)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 191, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 211, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 126, 331, 19))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.duration_set_button = QtWidgets.QSpinBox(self.centralwidget)
        self.duration_set_button.setEnabled(True)
        self.duration_set_button.setGeometry(QtCore.QRect(250, 190, 33, 19))
        self.duration_set_button.setMouseTracking(False)
        self.duration_set_button.setWrapping(True)
        self.duration_set_button.setReadOnly(False)
        self.duration_set_button.setAccelerated(True)
        self.duration_set_button.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.duration_set_button.setKeyboardTracking(True)
        self.duration_set_button.setMinimum(1)
        self.duration_set_button.setMaximum(6)
        self.duration_set_button.setSingleStep(1)
        self.duration_set_button.setProperty("value", 1)
        self.duration_set_button.setDisplayIntegerBase(10)
        self.duration_set_button.setObjectName("duration_set_button")
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(250, 250, 56, 17))
        self.run_button.setObjectName("run_button")
        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_button.setGeometry(QtCore.QRect(250, 160, 56, 17))
        self.browse_button.setObjectName("browse_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter starting date and time:"))
        self.label_2.setText(_translate("MainWindow", "Select file:"))
        self.label_3.setText(_translate("MainWindow", "Duration(in hours):"))
        self.run_button.setText(_translate("MainWindow", "Run"))
        self.browse_button.setText(_translate("MainWindow", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

