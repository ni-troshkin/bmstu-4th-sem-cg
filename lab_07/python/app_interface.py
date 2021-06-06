# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab_07_design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(251, 252, 219);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(5, 11, 1582, 882))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(7, 7, 10, 10)
        self.gridLayout.setHorizontalSpacing(14)
        self.gridLayout.setObjectName("gridLayout")
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(5, 11, 1195, 869)
        self.canvas = QtWidgets.QGraphicsView(self.scene, self.widget)
        self.canvas.setMinimumSize(QtCore.QSize(1200, 880))
        self.canvas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 0, 0, 1, 1)
        self.splitter_8 = QtWidgets.QSplitter(self.widget)
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setHandleWidth(12)
        self.splitter_8.setObjectName("splitter_8")
        self.radio_cutter = QtWidgets.QRadioButton(self.splitter_8)
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.radio_cutter.setFont(font)
        self.radio_cutter.setChecked(True)
        self.radio_cutter.setObjectName("radio_cutter")
        self.radio_line = QtWidgets.QRadioButton(self.splitter_8)
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.radio_line.setFont(font)
        self.radio_line.setObjectName("radio_line")
        self.label = QtWidgets.QLabel(self.splitter_8)
        self.label.setText("")
        self.label.setObjectName("label")
        self.cutter_box = QtWidgets.QComboBox(self.splitter_8)
        self.cutter_box.setMaximumSize(QtCore.QSize(361, 51))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.cutter_box.setFont(font)
        self.cutter_box.setStyleSheet("selection-color: rgb(0, 0, 0);")
        self.cutter_box.setObjectName("cutter_box")
        self.cutter_box.addItem("")
        self.cutter_box.addItem("")
        self.cutter_box.addItem("")
        self.cutter_box.addItem("")
        self.cutter_box.addItem("")
        self.cutter_box.addItem("")
        self.cutter_box.addItem("")
        self.cutter_box.addItem("")
        self.border_label = QtWidgets.QLabel(self.splitter_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.border_label.sizePolicy().hasHeightForWidth())
        self.border_label.setSizePolicy(sizePolicy)
        self.border_label.setMinimumSize(QtCore.QSize(171, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.border_label.setFont(font)
        self.border_label.setAlignment(QtCore.Qt.AlignCenter)
        self.border_label.setObjectName("border_label")
        self.splitter = QtWidgets.QSplitter(self.splitter_8)
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(29)
        self.splitter.setObjectName("splitter")
        self.left_label = QtWidgets.QLabel(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_label.sizePolicy().hasHeightForWidth())
        self.left_label.setSizePolicy(sizePolicy)
        self.left_label.setMinimumSize(QtCore.QSize(166, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.left_label.setFont(font)
        self.left_label.setAlignment(QtCore.Qt.AlignCenter)
        self.left_label.setObjectName("left_label")
        self.top_label = QtWidgets.QLabel(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_label.sizePolicy().hasHeightForWidth())
        self.top_label.setSizePolicy(sizePolicy)
        self.top_label.setMinimumSize(QtCore.QSize(166, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.top_label.setFont(font)
        self.top_label.setAlignment(QtCore.Qt.AlignCenter)
        self.top_label.setObjectName("top_label")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(29)
        self.splitter_2.setObjectName("splitter_2")
        self.left_entry = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.left_entry.setFont(font)
        self.left_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.left_entry.setObjectName("left_entry")
        self.top_entry = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.top_entry.setFont(font)
        self.top_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.top_entry.setObjectName("top_entry")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setHandleWidth(29)
        self.splitter_3.setObjectName("splitter_3")
        self.right_label = QtWidgets.QLabel(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_label.sizePolicy().hasHeightForWidth())
        self.right_label.setSizePolicy(sizePolicy)
        self.right_label.setMinimumSize(QtCore.QSize(166, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.right_label.setFont(font)
        self.right_label.setAlignment(QtCore.Qt.AlignCenter)
        self.right_label.setObjectName("right_label")
        self.bottom_label = QtWidgets.QLabel(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_label.sizePolicy().hasHeightForWidth())
        self.bottom_label.setSizePolicy(sizePolicy)
        self.bottom_label.setMinimumSize(QtCore.QSize(166, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bottom_label.setFont(font)
        self.bottom_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bottom_label.setObjectName("bottom_label")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setHandleWidth(29)
        self.splitter_4.setObjectName("splitter_4")
        self.right_entry = QtWidgets.QLineEdit(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.right_entry.setFont(font)
        self.right_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.right_entry.setObjectName("right_entry")
        self.bottom_entry = QtWidgets.QLineEdit(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bottom_entry.setFont(font)
        self.bottom_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bottom_entry.setObjectName("bottom_entry")
        self.cutter_btn = QtWidgets.QPushButton(self.splitter_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cutter_btn.sizePolicy().hasHeightForWidth())
        self.cutter_btn.setSizePolicy(sizePolicy)
        self.cutter_btn.setMaximumSize(QtCore.QSize(16777215, 51))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cutter_btn.setFont(font)
        self.cutter_btn.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.cutter_btn.setObjectName("cutter_btn")
        self.label_2 = QtWidgets.QLabel(self.splitter_8)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line_box = QtWidgets.QComboBox(self.splitter_8)
        self.line_box.setMaximumSize(QtCore.QSize(361, 51))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.line_box.setFont(font)
        self.line_box.setStyleSheet("selection-color: rgb(0, 0, 0);")
        self.line_box.setObjectName("line_box")
        self.line_box.addItem("")
        self.line_box.addItem("")
        self.line_box.addItem("")
        self.line_box.addItem("")
        self.line_box.addItem("")
        self.line_box.addItem("")
        self.line_box.addItem("")
        self.line_box.addItem("")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setHandleWidth(29)
        self.splitter_5.setObjectName("splitter_5")
        self.x_label = QtWidgets.QLabel(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_label.sizePolicy().hasHeightForWidth())
        self.x_label.setSizePolicy(sizePolicy)
        self.x_label.setMinimumSize(QtCore.QSize(166, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.x_label.setFont(font)
        self.x_label.setAlignment(QtCore.Qt.AlignCenter)
        self.x_label.setObjectName("x_label")
        self.y_label = QtWidgets.QLabel(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_label.sizePolicy().hasHeightForWidth())
        self.y_label.setSizePolicy(sizePolicy)
        self.y_label.setMinimumSize(QtCore.QSize(166, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.y_label.setFont(font)
        self.y_label.setAlignment(QtCore.Qt.AlignCenter)
        self.y_label.setObjectName("y_label")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setHandleWidth(29)
        self.splitter_6.setObjectName("splitter_6")
        self.x_entry = QtWidgets.QLineEdit(self.splitter_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.x_entry.setFont(font)
        self.x_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x_entry.setObjectName("x_entry")
        self.y_entry = QtWidgets.QLineEdit(self.splitter_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.y_entry.setFont(font)
        self.y_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.y_entry.setObjectName("y_entry")
        self.add_btn = QtWidgets.QPushButton(self.splitter_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy)
        self.add_btn.setMaximumSize(QtCore.QSize(16777215, 51))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.add_btn.setFont(font)
        self.add_btn.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.add_btn.setObjectName("add_btn")
        self.label_3 = QtWidgets.QLabel(self.splitter_8)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.result_box = QtWidgets.QComboBox(self.splitter_8)
        self.result_box.setMaximumSize(QtCore.QSize(361, 51))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.result_box.setFont(font)
        self.result_box.setStyleSheet("selection-color: rgb(0, 0, 0);")
        self.result_box.setObjectName("result_box")
        self.result_box.addItem("")
        self.result_box.addItem("")
        self.result_box.addItem("")
        self.result_box.addItem("")
        self.result_box.addItem("")
        self.result_box.addItem("")
        self.result_box.addItem("")
        self.result_box.addItem("")
        self.cut_btn = QtWidgets.QPushButton(self.splitter_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cut_btn.sizePolicy().hasHeightForWidth())
        self.cut_btn.setSizePolicy(sizePolicy)
        self.cut_btn.setMaximumSize(QtCore.QSize(16777215, 51))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cut_btn.setFont(font)
        self.cut_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        self.cut_btn.setObjectName("cut_btn")
        self.label_4 = QtWidgets.QLabel(self.splitter_8)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setHandleWidth(29)
        self.splitter_7.setObjectName("splitter_7")
        self.clear_btn = QtWidgets.QPushButton(self.splitter_7)
        self.clear_btn.setMinimumSize(QtCore.QSize(166, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.clear_btn.setFont(font)
        self.clear_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(78, 154, 6);")
        self.clear_btn.setObjectName("clear_btn")
        self.exit_btn = QtWidgets.QPushButton(self.splitter_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy)
        self.exit_btn.setMinimumSize(QtCore.QSize(166, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(164, 0, 0);")
        self.exit_btn.setObjectName("exit_btn")
        self.gridLayout.addWidget(self.splitter_8, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Отсечение отрезков методом Сазерленда-Коэна"))
        self.radio_cutter.setText(_translate("MainWindow", "Ввод отсекателя"))
        self.radio_line.setText(_translate("MainWindow", "Ввод отрезков"))
        self.cutter_box.setItemText(0, _translate("MainWindow", "Цвет отсекателя..."))
        self.cutter_box.setItemText(1, _translate("MainWindow", "Красный"))
        self.cutter_box.setItemText(2, _translate("MainWindow", "Синий"))
        self.cutter_box.setItemText(3, _translate("MainWindow", "Черный"))
        self.cutter_box.setItemText(4, _translate("MainWindow", "Зеленый"))
        self.cutter_box.setItemText(5, _translate("MainWindow", "Горчичный"))
        self.cutter_box.setItemText(6, _translate("MainWindow", "Фиолетовый"))
        self.cutter_box.setItemText(7, _translate("MainWindow", "Белый"))
        self.border_label.setText(_translate("MainWindow", "Границы отсекателя:"))
        self.left_label.setText(_translate("MainWindow", "X левый:"))
        self.top_label.setText(_translate("MainWindow", "Y верхний:"))
        self.right_label.setText(_translate("MainWindow", "X правый:"))
        self.bottom_label.setText(_translate("MainWindow", "Y нижний:"))
        self.cutter_btn.setText(_translate("MainWindow", "Применить"))
        self.line_box.setItemText(0, _translate("MainWindow", "Цвет отрезков..."))
        self.line_box.setItemText(1, _translate("MainWindow", "Красный"))
        self.line_box.setItemText(2, _translate("MainWindow", "Синий"))
        self.line_box.setItemText(3, _translate("MainWindow", "Черный"))
        self.line_box.setItemText(4, _translate("MainWindow", "Зеленый"))
        self.line_box.setItemText(5, _translate("MainWindow", "Горчичный"))
        self.line_box.setItemText(6, _translate("MainWindow", "Фиолетовый"))
        self.line_box.setItemText(7, _translate("MainWindow", "Белый"))
        self.x_label.setText(_translate("MainWindow", "X:"))
        self.y_label.setText(_translate("MainWindow", "Y:"))
        self.add_btn.setText(_translate("MainWindow", "Добавить точку"))
        self.result_box.setItemText(0, _translate("MainWindow", "Цвет результата..."))
        self.result_box.setItemText(1, _translate("MainWindow", "Красный"))
        self.result_box.setItemText(2, _translate("MainWindow", "Синий"))
        self.result_box.setItemText(3, _translate("MainWindow", "Черный"))
        self.result_box.setItemText(4, _translate("MainWindow", "Зеленый"))
        self.result_box.setItemText(5, _translate("MainWindow", "Горчичный"))
        self.result_box.setItemText(6, _translate("MainWindow", "Фиолетовый"))
        self.result_box.setItemText(7, _translate("MainWindow", "Белый"))
        self.cut_btn.setText(_translate("MainWindow", "Применить отсечение"))
        self.clear_btn.setText(_translate("MainWindow", "Очистить"))
        self.exit_btn.setText(_translate("MainWindow", "Выход"))