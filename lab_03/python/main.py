from line_algorithms import *
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
        self.spectre_btn.clicked.connect(self.draw_spectre)
        self.line_btn.clicked.connect(self.draw_line)
        self.time_btn.clicked.connect(self.count_time)
        self.step_btn.clicked.connect(self.count_steps)
        self.clear_btn.clicked.connect(self.clear_scene)

        self.red_pen = QPen(QColor(140, 0, 0))
        self.blue_pen = QPen(QColor(0, 0, 140))
        self.pink_pen = QPen(QColor(155, 0, 155))
        self.black_pen = QPen(QColor(0, 0, 0))
        self.orange_pen = QPen(QColor(155, 100, 0))
        self.bg_pen = QPen(QColor(212, 255, 191))

    def clear_scene(self):
        self.scene.clear()

    def exit(self):
        sys.exit(0)

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

    def draw_points(self, points, pen):
        for point in points:
            if (abs(point[2] - 1.0) < EPS):
                self.scene.addLine(point[0], point[1], point[0], point[1], pen)
            else:
                al_pen = QPen(get_color_with_intesity(pen.color(), point[2]))
                self.scene.addLine(point[0], point[1], point[0], point[1], al_pen)

    def draw(self, alg, color, start_x, start_y, end_x, end_y):
        if (alg == 1):
            line = lib_line(start_x, start_y, end_x, end_y)
            self.scene.addLine(line.line(), self.get_pen(color))
        if (alg == 2):
            points = dda(start_x, start_y, end_x, end_y)[0]
            self.draw_points(points, self.get_pen(color))
        if (alg == 3):
            points = bresenham(start_x, start_y, end_x, end_y)[0]
            self.draw_points(points, self.get_pen(color))
        if (alg == 4):
            points = int_bresenham(start_x, start_y, end_x, end_y)[0]
            self.draw_points(points, self.get_pen(color))
        if (alg == 5):
            points = antialiased_bresenham(start_x, start_y, end_x, end_y)[0]
            self.draw_points(points, self.get_pen(color))
        if (alg == 6):
            points = wu(start_x, start_y, end_x, end_y)[0]
            self.draw_points(points, self.get_pen(color))
    
    def draw_step(self, alg, color, center_x, center_y, step, length):
        fi = 0
        while (fi < 360):
            end_x = center_x + length * cos(radians(fi))
            end_y = center_y - length * sin(radians(fi))
            fi += step
            self.draw(alg, color, center_x, center_y, end_x, end_y)

    def draw_line(self):
        try:
            alg = self.line_alg.currentIndex()
            if alg == 0:
                raise TypeError
            color = self.line_color.currentIndex()
            if color == 0:
                raise Warning

            start_x = float(self.entry_sx.text())
            start_y = float(self.entry_sy.text())
            end_x = float(self.entry_ex.text())
            end_y = float(self.entry_ey.text())
        
        except TypeError:
            self.show_warning("Ошибка", "Выберите алгоритм "
                "построения отрезка", "Ubuntu 15")

        except Warning:
            self.show_warning("Ошибка", "Выберите цвет построения", "Ubuntu 15")
        
        except:
            self.show_warning("Ошибка", "Координаты концов отрезка должны быть "
                "вещественными числами", "Ubuntu 15")
        
        else:
            self.draw(alg, color, start_x, start_y, end_x, end_y)
    
    def draw_spectre(self):
        try:
            alg = self.spectre_alg.currentIndex()
            if alg == 0:
                raise TypeError
            color = self.spectre_color.currentIndex()
            if color == 0:
                raise Warning

            center_x = float(self.entry_cx.text())
            center_y = float(self.entry_cy.text())
            angle = float(self.entry_angle.text())
            length = float(self.entry_len.text())
            if length <= 0 or angle <= 0:
                raise ArithmeticError
        
        except TypeError:
            self.show_warning("Ошибка", "Выберите алгоритм "
                "построения отрезка", "Ubuntu 15")

        except Warning:
            self.show_warning("Ошибка", "Выберите цвет построения", "Ubuntu 15")
        
        except ArithmeticError:
            self.show_warning("Ошибка", "Длина и шаг угла должны быть "
                "положительными", "Ubuntu 15")

        except:
            self.show_warning("Ошибка", "Координаты, длина и угол должны быть "
                "вещественными числами", "Ubuntu 15")
        
        else:
            self.draw_step(alg, color, center_x, center_y, angle, length)

    def count_time(self):
        times = {"Library": None, "DDA": None, "Bresenham": None, 
            "Int\nBresenham": None, "Antialiased\nBresenham": None, "Wu": None}
        sum_time = 0
        for i in range(REPEATS):
            start_time = time()
            lib_line(0, 0, 300, 200)
            sum_time += time() - start_time

        times['Library'] = sum_time / REPEATS * 1000000

        sum_time = 0
        for i in range(REPEATS):
            start_time = time()
            dda(0, 0, 300, 200)
            sum_time += time() - start_time

        times["DDA"] = sum_time / REPEATS * 1000000

        sum_time = 0
        for i in range(REPEATS):
            start_time = time()
            bresenham(0, 0, 300, 200)
            sum_time += time() - start_time

        times["Bresenham"] = sum_time / REPEATS * 1000000

        sum_time = 0
        for i in range(REPEATS):
            start_time = time()
            int_bresenham(0, 0, 300, 200)
            sum_time += time() - start_time

        times["Int\nBresenham"] = sum_time / REPEATS * 1000000

        sum_time = 0
        for i in range(REPEATS):
            start_time = time()
            antialiased_bresenham(0, 0, 300, 200)
            sum_time += time() - start_time

        times["Antialiased\nBresenham"] = sum_time / REPEATS * 1000000

        sum_time = 0
        for i in range(REPEATS):
            start_time = time()
            wu(0, 0, 300, 200)
            sum_time += time() - start_time

        times["Wu"] = sum_time / REPEATS * 1000000

        self.plot_time(times)

    def plot_time(self, times):
        x = list(times.keys())
        y = list(times.values())

        y_pos = numpy.arange(len(x))

        plt.bar(y_pos, y, align="center", alpha=0.5)
        plt.xticks(y_pos, x)
        plt.ylabel("Затраченное среднее время, мкс")
        plt.title("Сравнение времени построения отрезков")
        
        plt.show()

    def count_steps(self):
        start_x = start_y = 500
        length = 50
        steps_dda = dict()
        steps_bres = dict()
        steps_ibres = dict()
        steps_abres = dict()
        steps_wu = dict()
        fi = 0
        while (fi <= 90):
            end_x = start_x + length * cos(radians(fi))
            end_y = start_y + length * sin(radians(fi))

            steps_dda[fi] = dda(start_x, start_y, end_x, end_y)[1]
            steps_bres[fi] = bresenham(start_x, start_y, end_x, end_y)[1]
            steps_ibres[fi] = int_bresenham(start_x, start_y, end_x, end_y)[1]
            steps_abres[fi] = antialiased_bresenham(start_x, start_y, end_x, end_y)[1]
            steps_wu[fi] = wu(start_x, start_y, end_x, end_y)[1]

            fi += 1
        self.plot_steps(steps_dda, steps_bres, steps_ibres, steps_abres, steps_wu)

    def plot_steps(self, steps_dda, steps_bres, steps_ibres, steps_abres, steps_wu):
        xd = list(steps_dda.keys())
        yd = list(steps_dda.values())
        plt.plot(xd, yd, '-r', label="DDA")
        yi = list(steps_ibres.values())
        plt.plot(xd, yi, '-g', label="INT BRESENHAM")
        yb = list(steps_bres.values())
        plt.plot(xd, yb, ':k', label="BRESENHAM")
        yo = list(steps_abres.values())
        plt.plot(xd, yo, ':b', label="ANTIALIASED BRESENHAM")
        yw = list(steps_wu.values())
        plt.plot(xd, yw, '-y', label="WU")

        plt.legend()

        plt.xlabel("Угол наклона к горизонтальной оси")
        plt.ylabel("Количество ступенек")
        plt.title("Количество ступенек при построении отрезка длины 50")
        plt.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()     
