# ЛАБОРАТОРНАЯ РАБОТА N4
# РЕАЛИЗАЦИЯ И ИССЛЕДОВАНИЕ АЛГОРИТМОВ ГЕНЕРАЦИИ ОКРУЖНОСТИ И ЭЛЛИПСА

from app_interface import Ui_MainWindow
from ellipse import Ellipse

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPen, QBrush

import sys
import numpy
import matplotlib.pyplot as plt
from math import sin, cos, radians
from time import time

REPEATS = 250

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.exit_btn.clicked.connect(self.exit)
        self.spectre_btn.clicked.connect(self.draw_spectre)
        self.curve_btn.clicked.connect(self.draw_curve)
        self.ctime_btn.clicked.connect(self.circle_time)
        self.etime_btn.clicked.connect(self.ellipse_time)
        self.clear_btn.clicked.connect(self.clear_scene)

        self.figure_box.currentIndexChanged.connect(self.enable_ellipse)

        self.red_pen = QPen(QColor(140, 0, 0))
        self.blue_pen = QPen(QColor(0, 0, 140))
        self.pink_pen = QPen(QColor(155, 0, 155))
        self.black_pen = QPen(QColor(0, 0, 0))
        self.orange_pen = QPen(QColor(155, 100, 0))
        self.bg_pen = QPen(QColor(246, 255, 252))

        self.bgb = QBrush(QColor(246, 255, 252, 0))
    
    def show_warning(self, title, text, font):
        msg = QtWidgets.QMessageBox()
        msg.setGeometry(800, 400, 250, 200)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setFont(QtGui.QFont(font))
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def get_pen(self, index: int):
        if (index == 1):
            return self.red_pen
        if (index == 2):
            return self.blue_pen
        if (index == 3):
            return self.black_pen
        if (index == 4):
            return self.pink_pen
        if (index == 5):
            return self.orange_pen
        if (index == 6):
            return self.bg_pen

    def enable_ellipse(self):
        if self.figure_box.currentIndex() == 1:
            self.entry_b.setStyleSheet("background-color: rgb(211, 215, 207);")
            self.entry_startb.setStyleSheet("background-color: rgb(211, 215, 207);")
            self.entry_b.setDisabled(True)
            self.entry_startb.setDisabled(True)
            self.label_a.setText("Радиус\nокружности")
            self.label_starta.setText("Начальный\nрадиус")
            self.label_step.setText("Шаг изменения\nрадиуса")
        else:
            self.entry_b.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.entry_startb.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.entry_b.setEnabled(True)
            self.entry_startb.setEnabled(True)
            self.label_a.setText("Полуось\nа эллипса")
            self.label_starta.setText("Начальная\nполуось а")
            self.label_step.setText("Шаг изменения\nполуоси а")

    def generate_spectre(self, alg, color, center_x, center_y, a, b, num, step):
        pen = self.get_pen(color)
        for i in range(num):
            ellipse = Ellipse(center_x, center_y, a, b)
            ellipse.generate(alg, self.scene, pen, self.bgb)
            a += step
            b *= (1 + step / a)
            if self.figure_box.currentIndex() == 1:
                b = a

    def draw_spectre(self):
        try:
            alg = self.alg_box.currentIndex()
            if alg == 0:
                raise TypeError
            color = self.color_box.currentIndex()
            if color == 0:
                raise Warning

            center_x = float(self.entry_cx.text())
            center_y = float(self.entry_cy.text())

            a_start = float(self.entry_starta.text())
            if self.figure_box.currentIndex() == 0:
                b_start = float(self.entry_startb.text())
            else:
                b_start = a_start
            num = float(self.entry_num.text())
            num = int(num)
            step = float(self.entry_step.text())
            if a_start <= 0 or num <= 0 or b_start <= 0:
                raise ArithmeticError
        
        except TypeError:
            self.show_warning("Ошибка", "Выберите алгоритм "
                "построения кривой", "Ubuntu 15")

        except Warning:
            self.show_warning("Ошибка", "Выберите цвет построения", "Ubuntu 15")
        
        except ArithmeticError:
            self.show_warning("Ошибка", "Количество кривых и размер полуосей "
                "должны быть положительными", "Ubuntu 15")

        except:
            self.show_warning("Ошибка", "Координаты, длины и шаг должны быть "
                "вещественными числами, количество - целым", "Ubuntu 15")
        
        else:
            self.generate_spectre(alg, color, center_x, center_y, a_start, b_start, num, step)


    def draw_curve(self):
        try:
            alg = self.alg_box.currentIndex()
            if alg == 0:
                raise TypeError
            color = self.color_box.currentIndex()
            if color == 0:
                raise Warning

            center_x = float(self.entry_cx.text())
            center_y = float(self.entry_cy.text())
            a = float(self.entry_a.text())
            if self.figure_box.currentIndex() == 0:
                b = float(self.entry_b.text())
            else:
                b = a
        
        except TypeError:
            self.show_warning("Ошибка", "Выберите алгоритм "
                "построения кривой", "Ubuntu 15")

        except Warning:
            self.show_warning("Ошибка", "Выберите цвет построения", "Ubuntu 15")
        
        except:
            self.show_warning("Ошибка", "Координаты центра эллипса и "
                "полуоси/радиус должны быть вещественными числами", "Ubuntu 15")
        
        else:
            ellipse = Ellipse(center_x, center_y, a, b)
            ellipse.generate(alg, self.scene, self.get_pen(color), self.bgb)

    def circle_time(self):
        cx = 500
        cy = 500
        r = 50
        canon = dict()
        param = dict()
        lib = dict()
        bres = dict()
        middot = dict()
        for i in range(6):
            ellipse = Ellipse(cx, cy, r, r)
            sum_time = 0
            for j in range(REPEATS):
                start = time()
                ellipse.create_lib()
                sum_time += time() - start
            lib[r] = sum_time / REPEATS * 1000000

            sum_time = 0
            for j in range(REPEATS):
                start = time()
                ellipse.create_canon()
                sum_time += time() - start
            canon[r] = sum_time / REPEATS * 1000000

            sum_time = 0
            for j in range(REPEATS):
                start = time()
                ellipse.create_param()
                sum_time += time() - start
            param[r] = sum_time / REPEATS * 1000000

            sum_time = 0
            for j in range(REPEATS):
                start = time()
                ellipse.create_bresenham()
                sum_time += time() - start
            bres[r] = sum_time / REPEATS * 1000000

            sum_time = 0
            for j in range(REPEATS):
                start = time()
                ellipse.create_middledot()
                sum_time += time() - start
            middot[r] = sum_time / REPEATS * 1000000

            r += 50
        
        self.circle_plot(lib, canon, param, bres, middot)

    def circle_plot(self, lib, canon, param, bres, middot, is_circle=True):
        xlib = list(lib.keys())
        ylib = list(lib.values())
        plt.plot(xlib, ylib, 'r', label="Библиотечный")
        ycanon = list(canon.values())
        plt.plot(xlib, ycanon, 'g', label="Каноническое ур-е")
        yparam = list(param.values())
        plt.plot(xlib, yparam, 'b', label="Параметрическое ур-е")
        ybres = list(bres.values())
        plt.plot(xlib, ybres, 'y', label="Брезенхем")
        ymiddot = list(middot.values())
        plt.plot(xlib, ymiddot, 'm', label="Средняя точка")

        plt.legend()

        plt.ylabel("Время построения, мкс")
        if is_circle:
            plt.xlabel("Радиус окружности")
            plt.title("Сравнение времени генерации окружностей разными алгоритмами")
        else:
            plt.xlabel("Полуось а эллипса")
            plt.title("Сравнение времени генерации эллипсов\n(a/b = 2) разными алгоритмами")
        plt.show()

    def ellipse_time(self):
        cx = 500
        cy = 500
        a = 50
        b = a / 2
        canon = dict()
        param = dict()
        lib = dict()
        bres = dict()
        middot = dict()
        for i in range(6):
            ellipse = Ellipse(cx, cy, a, b)
            sum_time = 0
            for j in range(REPEATS):
                start = time()
                ellipse.create_lib()
                sum_time += time() - start
            lib[a] = sum_time / REPEATS * 1000000

            sum_time = 0
            for j in range(REPEATS):
                start = time()
                ellipse.create_canon()
                sum_time += time() - start
            canon[a] = sum_time / REPEATS * 1000000

            sum_time = 0
            for j in range(REPEATS):
                start = time()
                ellipse.create_param()
                sum_time += time() - start
            param[a] = sum_time / REPEATS * 1000000

            sum_time = 0
            for j in range(REPEATS):
                start = time()
                ellipse.create_bresenham()
                sum_time += time() - start
            bres[a] = sum_time / REPEATS * 1000000

            sum_time = 0
            for j in range(REPEATS):
                start = time()
                ellipse.create_middledot()
                sum_time += time() - start
            middot[a] = sum_time / REPEATS * 1000000
            a += 50
            b = a / 2
        
        self.circle_plot(lib, canon, param, bres, middot, False)

    def clear_scene(self):
        self.scene.clear()

    def exit(self):
        sys.exit(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
