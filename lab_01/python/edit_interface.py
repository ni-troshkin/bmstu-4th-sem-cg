from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # основное окно
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 275)
        MainWindow.setStyleSheet("background-color: rgb(255, 231, 175);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 275))

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(7, 7, 10, 10)
        self.gridLayout.setObjectName("gridLayout")

        # поле ввода х
        self.new_x_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.new_x_entry.setGeometry(QtCore.QRect(50, 110, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.new_x_entry.setFont(font)
        self.new_x_entry.setStyleSheet("background-color: rgb(235, 255, 253);")
        self.new_x_entry.setObjectName("new_x_entry")
        self.new_x_entry.setMaximumHeight(60)
        self.gridLayout.addWidget(self.new_x_entry, 1, 0, 1, 1)

        # поле ввода у
        self.new_y_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.new_y_entry.setGeometry(QtCore.QRect(210, 110, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.new_y_entry.setFont(font)
        self.new_y_entry.setStyleSheet("background-color: rgb(235, 255, 253);")
        self.new_y_entry.setObjectName("new_y_entry")
        self.new_y_entry.setMaximumHeight(60)
        self.gridLayout.addWidget(self.new_y_entry, 1, 1, 1, 1)

        # надпись над полем х
        self.new_x_label = QtWidgets.QLabel(self.centralwidget)
        self.new_x_label.setGeometry(QtCore.QRect(40, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_x_label.setFont(font)
        self.new_x_label.setAlignment(QtCore.Qt.AlignCenter)
        self.new_x_label.setObjectName("new_x_label")
        self.gridLayout.addWidget(self.new_x_label, 0, 0, 1, 1)

        # надпись над полем у
        self.new_y_label = QtWidgets.QLabel(self.centralwidget)
        self.new_y_label.setGeometry(QtCore.QRect(205, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_y_label.setFont(font)
        self.new_y_label.setAlignment(QtCore.Qt.AlignCenter)
        self.new_y_label.setObjectName("new_y_label")
        self.gridLayout.addWidget(self.new_y_label, 0, 1, 1, 1)

        # кнопка для редактирования
        self.change_btn = QtWidgets.QPushButton(self.centralwidget)
        self.change_btn.setGeometry(QtCore.QRect(50, 190, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.change_btn.setFont(font)
        self.change_btn.setStyleSheet("background-color: rgb(235, 255, 253);")
        self.change_btn.setObjectName("change_btn")
        self.gridLayout.addWidget(self.change_btn, 2, 0, 1, 2)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, 
            QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.new_x_label.setSizePolicy(sizePolicy)
        self.new_y_label.setSizePolicy(sizePolicy)
        self.new_x_entry.setSizePolicy(sizePolicy)
        self.new_y_entry.setSizePolicy(sizePolicy)
        self.change_btn.setSizePolicy(sizePolicy)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Редактирование точки"))
        self.new_x_label.setText(_translate("MainWindow", "Новая \n"
            "координата Х"))
        self.new_y_label.setText(_translate("MainWindow", "Новая \n"
            "координата Y"))
        self.change_btn.setText(_translate("MainWindow", "Изменить положение точки"))
