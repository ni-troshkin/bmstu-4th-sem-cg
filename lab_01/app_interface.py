from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setBaseSize(QtCore.QSize(910, 749))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(188, 255, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(197, 244, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 255, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 255, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(197, 244, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 255, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 255, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 255, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 255, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True)

        # основное окно
        self.window_cg1 = QtWidgets.QWidget(MainWindow)
        self.window_cg1.setObjectName("window_cg1")
        self.widget = QtWidgets.QWidget(self.window_cg1)
        self.widget.setGeometry(QtCore.QRect(15, 9, 1571, 881))
        self.widget.setObjectName("widget")
        # выравнивание по сетке
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # сцена, от которой можно унаследовать холст и на нем рисовать
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 1177, 879)

        # холст с заданным цветом фона
        self.canvas = QtWidgets.QGraphicsView(self.scene, self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 248, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 248, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 248, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)

        brush = QtGui.QBrush(QtGui.QColor(255, 248, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 248, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 248, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)

        brush = QtGui.QBrush(QtGui.QColor(255, 248, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 248, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 248, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)

        self.canvas.setPalette(palette)
        self.canvas.setStyleSheet("background-color: rgb(255, 248, 177);")
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 0, 0, 1, 1)

        # создание формы с вертикальным выравниванием
        self.splitter_5 = QtWidgets.QSplitter(self.widget)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")

        # добавление таблицы и оформление шапки
        self.dots_table = QtWidgets.QTableWidget(self.splitter_5)
        self.dots_table.setRowCount(1)
        self.dots_table.setObjectName("dots_table")
        self.dots_table.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.dots_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dots_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dots_table.setHorizontalHeaderItem(2, item)
        self.dots_table.horizontalHeader().setCascadingSectionResizes(True)
        self.dots_table.horizontalHeader().setDefaultSectionSize(125)
        self.dots_table.horizontalHeader().setHighlightSections(False)
        self.dots_table.horizontalHeader().setStretchLastSection(True)
        self.dots_table.verticalHeader().setVisible(False)

        # горизонтальная форма, в которой находятся подписи
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")

        # надпись над полем х
        self.x_label = QtWidgets.QLabel(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, 
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_label.sizePolicy().hasHeightForWidth())
        self.x_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.x_label.setFont(font)
        self.x_label.setAlignment(QtCore.Qt.AlignCenter)
        self.x_label.setObjectName("x_label")

        # надпись над полем у
        self.y_label = QtWidgets.QLabel(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, 
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_label.sizePolicy().hasHeightForWidth())
        self.y_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.y_label.setFont(font)
        self.y_label.setAlignment(QtCore.Qt.AlignCenter)
        self.y_label.setObjectName("y_label")

        # горизонтальная форма, в которой находятся поля ввода
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")

        # поле ввода х
        self.x_entry = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.x_entry.setFont(font)
        self.x_entry.setObjectName("x_entry")

        # поле ввода у
        self.y_entry = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.y_entry.setFont(font)
        self.y_entry.setObjectName("y_entry")

        # кнопка добавления точки
        self.add_btn = QtWidgets.QPushButton(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, 
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")

        # надпись над полем с номером редактируемой точки
        self.del_label = QtWidgets.QLabel(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, 
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_label.sizePolicy().hasHeightForWidth())
        self.del_label.setSizePolicy(sizePolicy)
        self.del_label.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.del_label.setFont(font)
        self.del_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.del_label.setIndent(5)
        self.del_label.setObjectName("del_label")

        # поле для ввода редактируемой точки
        self.del_entry = QtWidgets.QLineEdit(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, 
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_entry.sizePolicy().hasHeightForWidth())
        self.del_entry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.del_entry.setFont(font)
        self.del_entry.setObjectName("del_entry")

        # горизонтальная форма для размещения кнопок удаления и редактирования
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")

        # кнопка удаления точки
        self.del_btn = QtWidgets.QPushButton(self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, 
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_btn.sizePolicy().hasHeightForWidth())
        self.del_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.del_btn.setFont(font)
        self.del_btn.setObjectName("del_btn")

        # кнопка редактирования точки
        self.edit_btn = QtWidgets.QPushButton(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edit_btn.setFont(font)
        self.edit_btn.setObjectName("edit_btn")
        self.find_btn = QtWidgets.QPushButton(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, 
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.find_btn.sizePolicy().hasHeightForWidth())
        self.find_btn.setSizePolicy(sizePolicy)
        self.find_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.find_btn.setFont(font)
        self.find_btn.setObjectName("find_btn")

        # горизонтальная форма для размещения кнопок справки и выхода
        self.splitter = QtWidgets.QSplitter(self.splitter_5)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        # кнопка вызова справочного окна
        self.info_btn = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, 
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_btn.sizePolicy().hasHeightForWidth())
        self.info_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.info_btn.setFont(font)
        self.info_btn.setObjectName("info_btn")

        # кнопка выхода
        self.exit_btn = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, 
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")

        self.gridLayout.addWidget(self.splitter_5, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.window_cg1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Геометрическая задача"))
        item = self.dots_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер точки"))
        item = self.dots_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Координата Х"))
        item = self.dots_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Координата Y"))
        self.x_label.setText(_translate("MainWindow", "X:"))
        self.y_label.setText(_translate("MainWindow", "Y:"))
        self.add_btn.setText(_translate("MainWindow", "Добавить точку"))
        self.del_label.setText(_translate("MainWindow", "Номер точки:"))
        self.del_btn.setText(_translate("MainWindow", "Удалить точку"))
        self.edit_btn.setText(_translate("MainWindow", "Редактировать"))
        self.find_btn.setText(_translate("MainWindow", "Рассчитать"))
        self.info_btn.setText(_translate("MainWindow", "Справка"))
        self.exit_btn.setText(_translate("MainWindow", "Выход"))
