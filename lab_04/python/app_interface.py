# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab_04_interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setStyleSheet("background-color: rgb(255, 233, 183);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1600, 900))
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(12, 11, 1569, 882))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(7, 7, 10, 10)
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setVerticalSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(5, 11, 1195, 869)
        self.canvas = QtWidgets.QGraphicsView(self.scene, self.widget)
        self.canvas.setMinimumSize(QtCore.QSize(1200, 880))
        self.canvas.setMaximumSize(QtCore.QSize(1200, 880))
        self.canvas.setStyleSheet("background-color: rgb(246, 255, 252);")
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 0, 0, 1, 1)
        self.splitter_10 = QtWidgets.QSplitter(self.widget)
        self.splitter_10.setOrientation(QtCore.Qt.Vertical)
        self.splitter_10.setHandleWidth(8)
        self.splitter_10.setObjectName("splitter_10")
        self.alg_box = QtWidgets.QComboBox(self.splitter_10)
        self.alg_box.setMinimumSize(QtCore.QSize(351, 41))
        self.alg_box.setMaximumSize(QtCore.QSize(351, 16777215))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.alg_box.setFont(font)
        self.alg_box.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);")
        self.alg_box.setObjectName("alg_box")
        self.alg_box.addItem("")
        self.alg_box.addItem("")
        self.alg_box.addItem("")
        self.alg_box.addItem("")
        self.alg_box.addItem("")
        self.alg_box.addItem("")
        self.splitter_11 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_11.setMinimumSize(QtCore.QSize(351, 41))
        self.splitter_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setHandleWidth(29)
        self.splitter_11.setObjectName("splitter_11")
        self.figure_box = QtWidgets.QComboBox(self.splitter_11)
        self.figure_box.setMinimumSize(QtCore.QSize(161, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.figure_box.setFont(font)
        self.figure_box.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);")
        self.figure_box.setObjectName("figure_box")
        self.figure_box.addItem("")
        self.figure_box.addItem("")
        self.color_box = QtWidgets.QComboBox(self.splitter_11)
        self.color_box.setMinimumSize(QtCore.QSize(161, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.color_box.setFont(font)
        self.color_box.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);")
        self.color_box.setObjectName("color_box")
        self.color_box.addItem("")
        self.color_box.addItem("")
        self.color_box.addItem("")
        self.color_box.addItem("")
        self.color_box.addItem("")
        self.color_box.addItem("")
        self.color_box.addItem("")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_6.setMinimumSize(QtCore.QSize(351, 0))
        self.splitter_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setHandleWidth(29)
        self.splitter_6.setObjectName("splitter_6")
        self.label_cx = QtWidgets.QLabel(self.splitter_6)
        self.label_cx.setMinimumSize(QtCore.QSize(161, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_cx.setFont(font)
        self.label_cx.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_cx.setObjectName("label_cx")
        self.label_cy = QtWidgets.QLabel(self.splitter_6)
        self.label_cy.setMinimumSize(QtCore.QSize(161, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_cy.setFont(font)
        self.label_cy.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_cy.setObjectName("label_cy")
        self.splitter = QtWidgets.QSplitter(self.splitter_10)
        self.splitter.setMinimumSize(QtCore.QSize(351, 41))
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(29)
        self.splitter.setObjectName("splitter")
        self.entry_cx = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_cx.setFont(font)
        self.entry_cx.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_cx.setObjectName("entry_cx")
        self.entry_cy = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_cy.setFont(font)
        self.entry_cy.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_cy.setObjectName("entry_cy")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_7.setMinimumSize(QtCore.QSize(351, 0))
        self.splitter_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setHandleWidth(29)
        self.splitter_7.setObjectName("splitter_7")
        self.label_a = QtWidgets.QLabel(self.splitter_7)
        self.label_a.setMinimumSize(QtCore.QSize(161, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_a.setFont(font)
        self.label_a.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_a.setObjectName("label_a")
        self.label_b = QtWidgets.QLabel(self.splitter_7)
        self.label_b.setMinimumSize(QtCore.QSize(161, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_b.setFont(font)
        self.label_b.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_b.setObjectName("label_b")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_2.setMinimumSize(QtCore.QSize(351, 41))
        self.splitter_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(29)
        self.splitter_2.setObjectName("splitter_2")
        self.entry_a = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_a.setFont(font)
        self.entry_a.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_a.setObjectName("entry_a")
        self.entry_b = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_b.setFont(font)
        self.entry_b.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(211, 215, 207);")
        self.entry_b.setObjectName("entry_b")
        self.curve_btn = QtWidgets.QPushButton(self.splitter_10)
        self.curve_btn.setMinimumSize(QtCore.QSize(351, 51))
        self.curve_btn.setMaximumSize(QtCore.QSize(351, 16777215))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.curve_btn.setFont(font)
        self.curve_btn.setStyleSheet("background-color: rgb(0, 140, 0);\n"
"color: rgb(255, 255, 255)")
        self.curve_btn.setObjectName("curve_btn")
        self.splitter_8 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_8.setMinimumSize(QtCore.QSize(351, 0))
        self.splitter_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setHandleWidth(29)
        self.splitter_8.setObjectName("splitter_8")
        self.label_starta = QtWidgets.QLabel(self.splitter_8)
        self.label_starta.setMinimumSize(QtCore.QSize(161, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_starta.setFont(font)
        self.label_starta.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_starta.setObjectName("label_starta")
        self.label_startb = QtWidgets.QLabel(self.splitter_8)
        self.label_startb.setMinimumSize(QtCore.QSize(161, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_startb.setFont(font)
        self.label_startb.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_startb.setObjectName("label_startb")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_3.setMinimumSize(QtCore.QSize(351, 41))
        self.splitter_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setHandleWidth(29)
        self.splitter_3.setObjectName("splitter_3")
        self.entry_starta = QtWidgets.QLineEdit(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_starta.setFont(font)
        self.entry_starta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_starta.setObjectName("entry_starta")
        self.entry_startb = QtWidgets.QLineEdit(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_startb.setFont(font)
        self.entry_startb.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_startb.setObjectName("entry_startb")
        self.splitter_9 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_9.setMinimumSize(QtCore.QSize(351, 0))
        self.splitter_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setHandleWidth(29)
        self.splitter_9.setObjectName("splitter_9")
        self.label_num = QtWidgets.QLabel(self.splitter_9)
        self.label_num.setMinimumSize(QtCore.QSize(161, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_num.setFont(font)
        self.label_num.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_num.setObjectName("label_num")
        self.label_step = QtWidgets.QLabel(self.splitter_9)
        self.label_step.setMinimumSize(QtCore.QSize(161, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_step.setFont(font)
        self.label_step.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_step.setObjectName("label_step")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_4.setMinimumSize(QtCore.QSize(351, 41))
        self.splitter_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setHandleWidth(29)
        self.splitter_4.setObjectName("splitter_4")
        self.entry_num = QtWidgets.QLineEdit(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_num.setFont(font)
        self.entry_num.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_num.setObjectName("entry_num")
        self.entry_step = QtWidgets.QLineEdit(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_step.setFont(font)
        self.entry_step.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entry_step.setObjectName("entry_step")
        self.spectre_btn = QtWidgets.QPushButton(self.splitter_10)
        self.spectre_btn.setMinimumSize(QtCore.QSize(351, 51))
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
        self.label = QtWidgets.QLabel(self.splitter_10)
        self.label.setText("")
        self.label.setObjectName("label")
        self.ctime_btn = QtWidgets.QPushButton(self.splitter_10)
        self.ctime_btn.setMinimumSize(QtCore.QSize(351, 51))
        self.ctime_btn.setMaximumSize(QtCore.QSize(351, 16777215))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ctime_btn.setFont(font)
        self.ctime_btn.setStyleSheet("background-color: rgb(0, 140, 0);\n"
"color: rgb(255, 255, 255)")
        self.ctime_btn.setObjectName("ctime_btn")
        self.etime_btn = QtWidgets.QPushButton(self.splitter_10)
        self.etime_btn.setMinimumSize(QtCore.QSize(351, 51))
        self.etime_btn.setMaximumSize(QtCore.QSize(351, 16777215))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.etime_btn.setFont(font)
        self.etime_btn.setStyleSheet("background-color: rgb(0, 140, 0);\n"
"color: rgb(255, 255, 255)")
        self.etime_btn.setObjectName("etime_btn")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_5.setMinimumSize(QtCore.QSize(351, 0))
        self.splitter_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setHandleWidth(9)
        self.splitter_5.setObjectName("splitter_5")
        self.clear_btn = QtWidgets.QPushButton(self.splitter_5)
        self.clear_btn.setMinimumSize(QtCore.QSize(0, 51))
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
        self.exit_btn.setMinimumSize(QtCore.QSize(0, 51))
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
        self.gridLayout.addWidget(self.splitter_10, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Построение эллипсов"))
        self.alg_box.setCurrentText(_translate("MainWindow", "Выберите алгоритм..."))
        self.alg_box.setItemText(0, _translate("MainWindow", "Выберите алгоритм..."))
        self.alg_box.setItemText(1, _translate("MainWindow", "Библиотечная функция"))
        self.alg_box.setItemText(2, _translate("MainWindow", "По каноническому ур-ю"))
        self.alg_box.setItemText(3, _translate("MainWindow", "По параметрическому ур-ю"))
        self.alg_box.setItemText(4, _translate("MainWindow", "Алгоритм Брезенхема"))
        self.alg_box.setItemText(5, _translate("MainWindow", "Алгоритм средней точки"))
        self.figure_box.setCurrentText(_translate("MainWindow", "Эллипс"))
        self.figure_box.setItemText(1, _translate("MainWindow", "Окружность"))
        self.figure_box.setItemText(0, _translate("MainWindow", "Эллипс"))
        self.color_box.setCurrentText(_translate("MainWindow", "Выбор цвета..."))
        self.color_box.setItemText(0, _translate("MainWindow", "Выбор цвета..."))
        self.color_box.setItemText(1, _translate("MainWindow", "Красный"))
        self.color_box.setItemText(2, _translate("MainWindow", "Синий"))
        self.color_box.setItemText(3, _translate("MainWindow", "Черный"))
        self.color_box.setItemText(4, _translate("MainWindow", "Розовый"))
        self.color_box.setItemText(5, _translate("MainWindow", "Оранжевый"))
        self.color_box.setItemText(6, _translate("MainWindow", "Цвет фона"))
        self.label_cx.setText(_translate("MainWindow", "Х центра"))
        self.label_cy.setText(_translate("MainWindow", "Y центра"))
        self.label_a.setText(_translate("MainWindow", "Полуось\n"
"а эллипса"))
        self.label_b.setText(_translate("MainWindow", "Полуось\n"
"b эллипса"))
        self.curve_btn.setText(_translate("MainWindow", "Построить кривую"))
        self.label_starta.setText(_translate("MainWindow", "Начальная\n"
"полуось а"))
        self.label_startb.setText(_translate("MainWindow", "Начальная\n"
"полуось b "))
        self.label_num.setText(_translate("MainWindow", "Количество\n"
"кривых"))
        self.label_step.setText(_translate("MainWindow", "Шаг изменения\n"
"полуоси а"))
        self.spectre_btn.setText(_translate("MainWindow", "Вывести спектр кривых"))
        self.ctime_btn.setText(_translate("MainWindow", "Время генерации окружности"))
        self.etime_btn.setText(_translate("MainWindow", "Время генерации эллипса"))
        self.clear_btn.setText(_translate("MainWindow", "Очистить"))
        self.exit_btn.setText(_translate("MainWindow", "Выход"))