# ЛАБОРАТОРНАЯ РАБОТА N4
# РЕАЛИЗАЦИЯ И ИССЛЕДОВАНИЕ АЛГОРИТМОВ ГЕНЕРАЦИИ ОКРУЖНОСТИ И ЭЛЛИПСА

# Цель работы: реализация алгоритмов построения окружности, исследование и 
# сравнение визуальных и временных характеристик алгоритмов.
# При выполнении этой лабораторной работы студент должен выполнить следующий объем работ:
# 1.Реализовать алгоритмы построения окружности на основе 
#    - Канонического уравнения X^2+Y^2=R^2
#    - Параметрического уравнения X=Rcost, Y=Rsint
#    - Алгоритма Брезенхема 
#    - Алгоритма средней точки
#    - построение окружности с помощью библиотечной функции
# Пользователь выбирает из списка определенный алгоритм, задает координаты центра, 
# радиус, цвет рисования.
# Визуальные характеристики исследуются путем рисования той же окружности цветом фона, 
# но с помощью другого алгоритма.

# 2. Реализовать алгоритмы построения эллипса на основе 
#    - Канонического уравнения X^2/a^2+Y^2/b^2=1
#    - Параметрического уравнения X=acost, Y=bsint
#    - Алгоритма Брезенхема (модифицировать самостоятельно)
#    - Алгоритма средней точки
#    - построение эллипса с помощью библиотечной функции
# Пользователь выбирает из списка определенный алгоритм, задает координаты центра, 
# полуоси, цвет рисования.
# Визуальные характеристики исследуются путем рисования того же эллипса цветом фона, 
# но с помощью другого алгоритма.
# П 1 и 2 предусматривают рисование одиночных кривых.

# 3. Сравнение визуальных характеристик разных алгоритмов при рисовании спектра 
# концентрических окружностей.
# Пользователь выбирает из списка определенный алгоритм, задает координаты центра, 
# цвет рисования, три из следующих четырех параметров: начальный радиус, конечный радиус, 
# шаг изменения радиуса, количество окружностей.
# Визуальные характеристики исследуются путем рисования того же спектра окружностей 
# цветом фона, но с помощью другого алгоритма.

# 4. Сравнение визуальных характеристик разных алгоритмов при рисовании спектра концентрических эллипсов.
# Пользователь выбирает из списка определенный алгоритм, задает координаты центра, 
# цвет рисования, начальные значения полуосей, шаг изменения одной из полуосей, количество эллипсов.
# Визуальные характеристики исследуются путем рисования того же спектра эллипсов 
# цветом фона, но с помощью другого алгоритма.

# Дополнительное задание.
# Сравнить временные характеристики разных алгоритмов, построив в одном поле вывода 
# (в одной системе координат и одном масштабе) графики зависимости времени работы 
# алгоритма от радиуса (для окружности). 
# Для эллипсов построить аналогичную зависимость (зависимость времени работы 
# алгоритма от изменения полуоси.  Имеется в виду, что вторая полуось тоже 
# будет изменяться см. п.4).


from app_interface import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPen

import sys
import numpy
import matplotlib.pyplot as plt
from math import sin, cos, radians
from time import time

REPEATS = 1000

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.exit_btn.clicked.connect(self.exit)
        self.spectre_btn.clicked.connect(self.exit)
        self.curve_btn.clicked.connect(self.exit)
        self.ctime_btn.clicked.connect(self.exit)
        self.etime_btn.clicked.connect(self.exit)
        self.clear_btn.clicked.connect(self.clear_scene)

        self.figure_box.currentIndexChanged.connect(self.enable_ellipse)

        self.red_pen = QPen(QColor(140, 0, 0))
        self.blue_pen = QPen(QColor(0, 0, 140))
        self.pink_pen = QPen(QColor(155, 0, 155))
        self.black_pen = QPen(QColor(0, 0, 0))
        self.orange_pen = QPen(QColor(155, 100, 0))
        self.bg_pen = QPen(QColor(246, 255, 252))
    
    def show_warning(self, title, text, font):
        msg = QtWidgets.QMessageBox()
        msg.setGeometry(800, 400, 250, 200)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setFont(QtGui.QFont(font))
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def enable_ellipse(self):
        if self.figure_box.currentIndex() == 1:
            self.entry_b.setStyleSheet("background-color: rgb(211, 215, 207);")
            self.entry_startb.setStyleSheet("background-color: rgb(211, 215, 207);")
            self.entry_b.setDisabled(True)
            self.entry_startb.setDisabled(True)
        else:
            self.entry_b.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.entry_startb.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.entry_b.setEnabled(True)
            self.entry_startb.setEnabled(True) 

    def clear_scene(self):
        self.scene.clear()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
