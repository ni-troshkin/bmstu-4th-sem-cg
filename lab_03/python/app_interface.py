# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab_03_interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setStyleSheet("background-color: rgb(205, 235, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1600, 900))
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 10, 1581, 882))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(7, 7, 10, 10)
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(5, 11, 1195, 869)
        self.canvas = QtWidgets.QGraphicsView(self.scene, self.widget)
        self.canvas.setMinimumSize(QtCore.QSize(1200, 880))
        self.canvas.setMaximumSize(QtCore.QSize(1200, 880))
        self.canvas.setStyleSheet("background-color: rgb(212, 255, 191);")
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 0, 0, 1, 1)
        self.splitter_11 = QtWidgets.QSplitter(self.widget)
        self.splitter_11.setMinimumSize(QtCore.QSize(351, 880))
        self.splitter_11.setMaximumSize(QtCore.QSize(351, 16777215))
        self.splitter_11.setOrientation(QtCore.Qt.Vertical)
        self.splitter_11.setHandleWidth(11)
        self.splitter_11.setObjectName("splitter_11")
        self.line_alg = QtWidgets.QComboBox(self.splitter_11)
        self.line_alg.setMinimumSize(QtCore.QSize(351, 0))
        self.line_alg.setMaximumSize(QtCore.QSize(351, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.line_alg.setFont(font)
        self.line_alg.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);")
        self.line_alg.setObjectName("line_alg")
        self.line_alg.addItem("")
        self.line_alg.addItem("")
        self.line_alg.addItem("")
        self.line_alg.addItem("")
        self.line_alg.addItem("")
        self.line_alg.addItem("")
        self.line_alg.addItem("")
        self.line_color = QtWidgets.QComboBox(self.splitter_11)
        self.line_color.setMinimumSize(QtCore.QSize(351, 0))
        self.line_color.setMaximumSize(QtCore.QSize(351, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.line_color.setFont(font)
        self.line_color.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);")
        self.line_color.setObjectName("line_color")
        self.line_color.addItem("")
        self.line_color.addItem("")
        self.line_color.addItem("")
        self.line_color.addItem("")
        self.line_color.addItem("")
        self.line_color.addItem("")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_6.setMinimumSize(QtCore.QSize(351, 0))
        self.splitter_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setHandleWidth(29)
        self.splitter_6.setObjectName("splitter_6")
        self.label_sx = QtWidgets.QLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_sx.setFont(font)
        self.label_sx.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_sx.setObjectName("label_sx")
        self.label_sy = QtWidgets.QLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_sy.setFont(font)
        self.label_sy.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_sy.setObjectName("label_sy")
        self.splitter = QtWidgets.QSplitter(self.splitter_11)
        self.splitter.setMinimumSize(QtCore.QSize(351, 0))
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(29)
        self.splitter.setObjectName("splitter")
        self.entry_sx = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_sx.setFont(font)
        self.entry_sx.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_sx.setObjectName("entry_sx")
        self.entry_sy = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_sy.setFont(font)
        self.entry_sy.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_sy.setObjectName("entry_sy")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_7.setMinimumSize(QtCore.QSize(351, 0))
        self.splitter_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setHandleWidth(29)
        self.splitter_7.setObjectName("splitter_7")
        self.label_ex = QtWidgets.QLabel(self.splitter_7)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_ex.setFont(font)
        self.label_ex.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_ex.setObjectName("label_ex")
        self.label_ey = QtWidgets.QLabel(self.splitter_7)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_ey.setFont(font)
        self.label_ey.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_ey.setObjectName("label_ey")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_2.setMinimumSize(QtCore.QSize(351, 0))
        self.splitter_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(29)
        self.splitter_2.setObjectName("splitter_2")
        self.entry_ex = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_ex.setFont(font)
        self.entry_ex.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_ex.setObjectName("entry_ex")
        self.entry_ey = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_ey.setFont(font)
        self.entry_ey.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_ey.setObjectName("entry_ey")
        self.line_btn = QtWidgets.QPushButton(self.splitter_11)
        self.line_btn.setMinimumSize(QtCore.QSize(351, 0))
        self.line_btn.setMaximumSize(QtCore.QSize(351, 16777215))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.line_btn.setFont(font)
        self.line_btn.setStyleSheet("background-color: rgb(0, 140, 0);\n"
"color: rgb(255, 255, 255)")
        self.line_btn.setObjectName("line_btn")
        self.splitter_10 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_10.setMinimumSize(QtCore.QSize(351, 0))
        self.splitter_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setHandleWidth(29)
        self.splitter_10.setObjectName("splitter_10")
        self.spectre_alg = QtWidgets.QComboBox(self.splitter_10)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spectre_alg.setFont(font)
        self.spectre_alg.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);")
        self.spectre_alg.setObjectName("spectre_alg")
        self.spectre_alg.addItem("")
        self.spectre_alg.addItem("")
        self.spectre_alg.addItem("")
        self.spectre_alg.addItem("")
        self.spectre_alg.addItem("")
        self.spectre_alg.addItem("")
        self.spectre_color = QtWidgets.QComboBox(self.splitter_10)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spectre_color.setFont(font)
        self.spectre_color.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);")
        self.spectre_color.setObjectName("spectre_color")
        self.spectre_color.addItem("")
        self.spectre_color.addItem("")
        self.spectre_color.addItem("")
        self.spectre_color.addItem("")
        self.spectre_color.addItem("")
        self.spectre_color.addItem("")
        self.spectre_color.addItem("")
        self.splitter_8 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_8.setMinimumSize(QtCore.QSize(351, 0))
        self.splitter_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setHandleWidth(29)
        self.splitter_8.setObjectName("splitter_8")
        self.label_cx = QtWidgets.QLabel(self.splitter_8)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_cx.setFont(font)
        self.label_cx.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_cx.setObjectName("label_cx")
        self.label_cy = QtWidgets.QLabel(self.splitter_8)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_cy.setFont(font)
        self.label_cy.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_cy.setObjectName("label_cy")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_3.setMinimumSize(QtCore.QSize(351, 0))
        self.splitter_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setHandleWidth(29)
        self.splitter_3.setObjectName("splitter_3")
        self.entry_cx = QtWidgets.QLineEdit(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_cx.setFont(font)
        self.entry_cx.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_cx.setObjectName("entry_cx")
        self.entry_cy = QtWidgets.QLineEdit(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_cy.setFont(font)
        self.entry_cy.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_cy.setObjectName("entry_cy")
        self.splitter_9 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_9.setMinimumSize(QtCore.QSize(351, 0))
        self.splitter_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setHandleWidth(29)
        self.splitter_9.setObjectName("splitter_9")
        self.label_len = QtWidgets.QLabel(self.splitter_9)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_len.setFont(font)
        self.label_len.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_len.setObjectName("label_len")
        self.label_angle = QtWidgets.QLabel(self.splitter_9)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_angle.setFont(font)
        self.label_angle.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_angle.setObjectName("label_angle")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_4.setMinimumSize(QtCore.QSize(351, 0))
        self.splitter_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setHandleWidth(29)
        self.splitter_4.setObjectName("splitter_4")
        self.entry_len = QtWidgets.QLineEdit(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_len.setFont(font)
        self.entry_len.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_len.setObjectName("entry_len")
        self.entry_angle = QtWidgets.QLineEdit(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_angle.setFont(font)
        self.entry_angle.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_angle.setObjectName("entry_angle")
        self.spectre_btn = QtWidgets.QPushButton(self.splitter_11)
        self.spectre_btn.setMinimumSize(QtCore.QSize(351, 0))
        self.spectre_btn.setMaximumSize(QtCore.QSize(351, 16777215))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.spectre_btn.setFont(font)
        self.spectre_btn.setStyleSheet("background-color: rgb(0, 140, 0);\n"
"color: rgb(255, 255, 255)")
        self.spectre_btn.setObjectName("spectre_btn")
        self.time_btn = QtWidgets.QPushButton(self.splitter_11)
        self.time_btn.setMinimumSize(QtCore.QSize(351, 0))
        self.time_btn.setMaximumSize(QtCore.QSize(351, 16777215))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.time_btn.setFont(font)
        self.time_btn.setStyleSheet("background-color: rgb(0, 140, 0);\n"
"color: rgb(255, 255, 255)")
        self.time_btn.setObjectName("time_btn")
        self.step_btn = QtWidgets.QPushButton(self.splitter_11)
        self.step_btn.setMinimumSize(QtCore.QSize(351, 0))
        self.step_btn.setMaximumSize(QtCore.QSize(351, 16777215))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.step_btn.setFont(font)
        self.step_btn.setStyleSheet("background-color: rgb(0, 140, 0);\n"
"color: rgb(255, 255, 255)")
        self.step_btn.setObjectName("step_btn")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_5.setMinimumSize(QtCore.QSize(351, 0))
        self.splitter_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setHandleWidth(9)
        self.splitter_5.setObjectName("splitter_5")
        self.clear_btn = QtWidgets.QPushButton(self.splitter_5)
        self.clear_btn.setMaximumSize(QtCore.QSize(171, 16777215))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.clear_btn.setFont(font)
        self.clear_btn.setStyleSheet("background-color: rgb(0, 0, 140);\n"
"color: rgb(255, 255, 255)")
        self.clear_btn.setObjectName("clear_btn")
        self.exit_btn = QtWidgets.QPushButton(self.splitter_5)
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("background-color: rgb(140, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.exit_btn.setObjectName("exit_btn")
        self.gridLayout.addWidget(self.splitter_11, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Построение отрезков"))
        self.line_alg.setCurrentText(_translate("MainWindow", "Выберите алгоритм..."))
        self.line_alg.setItemText(0, _translate("MainWindow", "Выберите алгоритм..."))
        self.line_alg.setItemText(1, _translate("MainWindow", "Библиотечный алгоритм"))
        self.line_alg.setItemText(2, _translate("MainWindow", "ЦДА"))
        self.line_alg.setItemText(3, _translate("MainWindow", "Алгоритм Брезенхема"))
        self.line_alg.setItemText(4, _translate("MainWindow", "Брезенхем целочисленный"))
        self.line_alg.setItemText(5, _translate("MainWindow", "Брезенхем с устранением"))
        self.line_alg.setItemText(6, _translate("MainWindow", "Алгоритм Ву"))
        self.line_color.setCurrentText(_translate("MainWindow", "Выберите цвет..."))
        self.line_color.setItemText(0, _translate("MainWindow", "Выберите цвет..."))
        self.line_color.setItemText(1, _translate("MainWindow", "Красный"))
        self.line_color.setItemText(2, _translate("MainWindow", "Синий"))
        self.line_color.setItemText(3, _translate("MainWindow", "Черный"))
        self.line_color.setItemText(4, _translate("MainWindow", "Розовый"))
        self.line_color.setItemText(5, _translate("MainWindow", "Оранжевый"))
        self.label_sx.setText(_translate("MainWindow", "Х начала"))
        self.label_sy.setText(_translate("MainWindow", "Y начала"))
        self.label_ex.setText(_translate("MainWindow", "Х конца"))
        self.label_ey.setText(_translate("MainWindow", "Y конца"))
        self.line_btn.setText(_translate("MainWindow", "Построить отрезок"))
        self.spectre_alg.setCurrentText(_translate("MainWindow", "Алгоритм..."))
        self.spectre_alg.setItemText(0, _translate("MainWindow", "Алгоритм..."))
        self.spectre_alg.setItemText(1, _translate("MainWindow", "ЦДА"))
        self.spectre_alg.setItemText(2, _translate("MainWindow", "Брезенхем"))
        self.spectre_alg.setItemText(3, _translate("MainWindow", "Брез. целочисленный"))
        self.spectre_alg.setItemText(4, _translate("MainWindow", "Брез. с устранением"))
        self.spectre_alg.setItemText(5, _translate("MainWindow", "Ву"))
        self.spectre_color.setCurrentText(_translate("MainWindow", "Выбор цвета..."))
        self.spectre_color.setItemText(0, _translate("MainWindow", "Выбор цвета..."))
        self.spectre_color.setItemText(6, _translate("MainWindow", "Цвет фона"))
        self.spectre_color.setItemText(1, _translate("MainWindow", "Красный"))
        self.spectre_color.setItemText(2, _translate("MainWindow", "Синий"))
        self.spectre_color.setItemText(3, _translate("MainWindow", "Черный"))
        self.spectre_color.setItemText(4, _translate("MainWindow", "Розовый"))
        self.spectre_color.setItemText(5, _translate("MainWindow", "Оранжевый"))
        self.label_cx.setText(_translate("MainWindow", "Х центра"))
        self.label_cy.setText(_translate("MainWindow", "Y центра"))
        self.label_len.setText(_translate("MainWindow", "Длина отрезков"))
        self.label_angle.setText(_translate("MainWindow", "Шаг угла (в ॰)"))
        self.spectre_btn.setText(_translate("MainWindow", "Вывести спектр"))
        self.time_btn.setText(_translate("MainWindow", "Исследование времени"))
        self.step_btn.setText(_translate("MainWindow", "Исследование ступенчатости"))
        self.clear_btn.setText(_translate("MainWindow", "Очистить"))
        self.exit_btn.setText(_translate("MainWindow", "Выход"))
