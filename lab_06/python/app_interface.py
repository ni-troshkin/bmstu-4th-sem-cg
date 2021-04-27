# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab_06_design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setStyleSheet("background-color: rgb(245, 213, 251);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 1588, 897))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(7, 7, 10, 10)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_8 = QtWidgets.QSplitter(self.widget)
        self.splitter_8.setMaximumSize(QtCore.QSize(361, 16777215))
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setHandleWidth(15)
        self.splitter_8.setObjectName("splitter_8")
        self.radio_random = QtWidgets.QRadioButton(self.splitter_8)
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.radio_random.setFont(font)
        self.radio_random.setChecked(True)
        self.radio_random.setObjectName("radio_random")
        self.radio_hor = QtWidgets.QRadioButton(self.splitter_8)
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radio_hor.setFont(font)
        self.radio_hor.setObjectName("radio_hor")
        self.radio_seed = QtWidgets.QRadioButton(self.splitter_8)
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.radio_seed.setFont(font)
        self.radio_seed.setObjectName("radio_seed")
        self.boundary_color_box = QtWidgets.QComboBox(self.splitter_8)
        self.boundary_color_box.setMaximumSize(QtCore.QSize(351, 51))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.boundary_color_box.setFont(font)
        self.boundary_color_box.setStyleSheet("selection-color: rgb(0, 0, 0);")
        self.boundary_color_box.setObjectName("boundary_color_box")
        self.boundary_color_box.addItem("")
        self.boundary_color_box.addItem("")
        self.boundary_color_box.addItem("")
        self.boundary_color_box.addItem("")
        self.boundary_color_box.addItem("")
        self.flood_box = QtWidgets.QComboBox(self.splitter_8)
        self.flood_box.setMaximumSize(QtCore.QSize(351, 51))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.flood_box.setFont(font)
        self.flood_box.setStyleSheet("selection-color: rgb(0, 0, 0);")
        self.flood_box.setObjectName("flood_box")
        self.flood_box.addItem("")
        self.flood_box.addItem("")
        self.flood_box.addItem("")
        self.flood_box.addItem("")
        self.flood_box.addItem("")
        self.splitter = QtWidgets.QSplitter(self.splitter_8)
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(29)
        self.splitter.setObjectName("splitter")
        self.x_label = QtWidgets.QLabel(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_label.sizePolicy().hasHeightForWidth())
        self.x_label.setSizePolicy(sizePolicy)
        self.x_label.setMinimumSize(QtCore.QSize(171, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.x_label.setFont(font)
        self.x_label.setAlignment(QtCore.Qt.AlignCenter)
        self.x_label.setObjectName("x_label")
        self.y_label = QtWidgets.QLabel(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_label.sizePolicy().hasHeightForWidth())
        self.y_label.setSizePolicy(sizePolicy)
        self.y_label.setMinimumSize(QtCore.QSize(161, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.y_label.setFont(font)
        self.y_label.setAlignment(QtCore.Qt.AlignCenter)
        self.y_label.setObjectName("y_label")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(29)
        self.splitter_2.setObjectName("splitter_2")
        self.x_entry = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.x_entry.setFont(font)
        self.x_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x_entry.setObjectName("x_entry")
        self.y_entry = QtWidgets.QLineEdit(self.splitter_2)
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
        self.close_fig_btn = QtWidgets.QPushButton(self.splitter_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_fig_btn.sizePolicy().hasHeightForWidth())
        self.close_fig_btn.setSizePolicy(sizePolicy)
        self.close_fig_btn.setMaximumSize(QtCore.QSize(16777215, 51))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.close_fig_btn.setFont(font)
        self.close_fig_btn.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.close_fig_btn.setObjectName("close_fig_btn")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setHandleWidth(29)
        self.splitter_5.setObjectName("splitter_5")
        self.cx_label = QtWidgets.QLabel(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cx_label.sizePolicy().hasHeightForWidth())
        self.cx_label.setSizePolicy(sizePolicy)
        self.cx_label.setMinimumSize(QtCore.QSize(171, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.cx_label.setFont(font)
        self.cx_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cx_label.setObjectName("cx_label")
        self.cy_label_2 = QtWidgets.QLabel(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cy_label_2.sizePolicy().hasHeightForWidth())
        self.cy_label_2.setSizePolicy(sizePolicy)
        self.cy_label_2.setMinimumSize(QtCore.QSize(161, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.cy_label_2.setFont(font)
        self.cy_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.cy_label_2.setObjectName("cy_label_2")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setHandleWidth(29)
        self.splitter_3.setObjectName("splitter_3")
        self.cx_entry = QtWidgets.QLineEdit(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cx_entry.setFont(font)
        self.cx_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cx_entry.setObjectName("cx_entry")
        self.cy_entry = QtWidgets.QLineEdit(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cy_entry.setFont(font)
        self.cy_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cy_entry.setObjectName("cy_entry")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setHandleWidth(29)
        self.splitter_7.setObjectName("splitter_7")
        self.a_label = QtWidgets.QLabel(self.splitter_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a_label.sizePolicy().hasHeightForWidth())
        self.a_label.setSizePolicy(sizePolicy)
        self.a_label.setMinimumSize(QtCore.QSize(171, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.a_label.setFont(font)
        self.a_label.setAlignment(QtCore.Qt.AlignCenter)
        self.a_label.setObjectName("a_label")
        self.b_label = QtWidgets.QLabel(self.splitter_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_label.sizePolicy().hasHeightForWidth())
        self.b_label.setSizePolicy(sizePolicy)
        self.b_label.setMinimumSize(QtCore.QSize(161, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.b_label.setFont(font)
        self.b_label.setAlignment(QtCore.Qt.AlignCenter)
        self.b_label.setObjectName("b_label")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setHandleWidth(29)
        self.splitter_6.setObjectName("splitter_6")
        self.a_entry = QtWidgets.QLineEdit(self.splitter_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.a_entry.setFont(font)
        self.a_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.a_entry.setObjectName("a_entry")
        self.b_entry = QtWidgets.QLineEdit(self.splitter_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_entry.setFont(font)
        self.b_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.b_entry.setObjectName("b_entry")
        self.ellipse_btn = QtWidgets.QPushButton(self.splitter_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ellipse_btn.sizePolicy().hasHeightForWidth())
        self.ellipse_btn.setSizePolicy(sizePolicy)
        self.ellipse_btn.setMaximumSize(QtCore.QSize(16777215, 51))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ellipse_btn.setFont(font)
        self.ellipse_btn.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.ellipse_btn.setObjectName("ellipse_btn")
        self.delay_check = QtWidgets.QCheckBox(self.splitter_8)
        self.delay_check.setMaximumSize(QtCore.QSize(16777215, 51))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.delay_check.setFont(font)
        self.delay_check.setStyleSheet("selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);")
        self.delay_check.setObjectName("delay_check")
        self.fill_btn = QtWidgets.QPushButton(self.splitter_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fill_btn.sizePolicy().hasHeightForWidth())
        self.fill_btn.setSizePolicy(sizePolicy)
        self.fill_btn.setMaximumSize(QtCore.QSize(16777215, 51))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.fill_btn.setFont(font)
        self.fill_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        self.fill_btn.setObjectName("fill_btn")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setHandleWidth(9)
        self.splitter_4.setObjectName("splitter_4")
        self.clear_btn = QtWidgets.QPushButton(self.splitter_4)
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.clear_btn.setFont(font)
        self.clear_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(78, 154, 6);")
        self.clear_btn.setObjectName("clear_btn")
        self.exit_btn = QtWidgets.QPushButton(self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy)
        self.exit_btn.setMinimumSize(QtCore.QSize(171, 0))
        font = QtGui.QFont()
        font.setFamily("KacstTitle")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(164, 0, 0);")
        self.exit_btn.setObjectName("exit_btn")
        self.gridLayout.addWidget(self.splitter_8, 0, 2, 1, 1)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 1190, 870)
        self.canvas = QtWidgets.QGraphicsView(self.scene, self.widget)
        self.canvas.setMinimumSize(QtCore.QSize(1200, 880))
        self.canvas.setMaximumSize(QtCore.QSize(16777215, 880))
        self.canvas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Заполнение многоугольника затравочным алгоритмом"))
        self.radio_random.setText(_translate("MainWindow", "Ввод произвольной точки"))
        self.radio_hor.setText(_translate("MainWindow", "Ввод горизонтали/вертикали"))
        self.radio_seed.setText(_translate("MainWindow", "Ввод затравочного пикселя"))
        self.boundary_color_box.setItemText(0, _translate("MainWindow", "Цвет границ..."))
        self.boundary_color_box.setItemText(1, _translate("MainWindow", "Красный"))
        self.boundary_color_box.setItemText(2, _translate("MainWindow", "Синий"))
        self.boundary_color_box.setItemText(3, _translate("MainWindow", "Черный"))
        self.boundary_color_box.setItemText(4, _translate("MainWindow", "Белый"))
        self.flood_box.setItemText(0, _translate("MainWindow", "Цвет заливки..."))
        self.flood_box.setItemText(1, _translate("MainWindow", "Красный"))
        self.flood_box.setItemText(2, _translate("MainWindow", "Синий"))
        self.flood_box.setItemText(3, _translate("MainWindow", "Черный"))
        self.flood_box.setItemText(4, _translate("MainWindow", "Белый"))
        self.x_label.setText(_translate("MainWindow", "X:"))
        self.y_label.setText(_translate("MainWindow", "Y:"))
        self.add_btn.setText(_translate("MainWindow", "Добавить точку"))
        self.close_fig_btn.setText(_translate("MainWindow", "Замкнуть многоугольник"))
        self.cx_label.setText(_translate("MainWindow", "X центра:"))
        self.cy_label_2.setText(_translate("MainWindow", "Y центра:"))
        self.a_label.setText(_translate("MainWindow", "Полуось а:"))
        self.b_label.setText(_translate("MainWindow", "Полуось b:"))
        self.ellipse_btn.setText(_translate("MainWindow", "Добавить эллипс"))
        self.delay_check.setText(_translate("MainWindow", "Задержка"))
        self.fill_btn.setText(_translate("MainWindow", "Заполнить"))
        self.clear_btn.setText(_translate("MainWindow", "Очистить"))
        self.exit_btn.setText(_translate("MainWindow", "Выход"))