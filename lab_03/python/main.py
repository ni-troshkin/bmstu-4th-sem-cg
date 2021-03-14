# Лабораторная работа №3
# РЕАЛИЗАЦИЯ И ИССЛЕДОВАНИЕ АЛГОРИТМОВ ПОСТРОЕНИЯ ОТРЕЗКОВ    
# 
# 1. Реализовать следующие алгоритмы построения отрезков 
# (предоставить пользователю возможность выбора алгоритма, 
# задания координат начала и конца отрезка, выбора цвета рисования)

# -Алгоритм, использующий библиотечную функцию;
# -Алгоритм цифрового дифференциального анализатора;
# -Алгоритм Брезенхема с действительными данными;
# -Алгоритм Брезенхема с целочисленными данными;
# -Алгоритм Брезенхема с устранением ступенчатости;
# -Алгоритм Ву.

#     2. Исследование визуальных характеристик при выводе отрезков 
# заданной длины в заданном спектре углов с помощью одного из алгоритмов 
# и наложения на полученный результат отрезков, построенных с помощью 
# другого алгоритма (цветом фона).

#     3. Исследование временных характеристик алгоритмов 
# (результат вывести в виде гистограммы).
#     4. Исследование ступенчатости отрезков. 
# Результат визуализировать в виде графика зависимости длины ступеньки 
# или количества ступенек в зависимости от угла наклона отрезка, 
# вывести для справки длину отрезка).

from line_algorithms import *
from app_interface import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPen

import sys
from math import sin, cos, radians

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
        self.pink_pen = QPen(QColor(255, 0, 255))
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

    def draw_line(self):
        try:
            alg = self.line_alg.currentIndex()
            if alg == 0:
                raise ValueError
            color = self.line_color.currentIndex()
            if color == 0:
                raise Warning

            start_x = float(self.entry_sx.text())
            start_y = float(self.entry_sy.text())
            end_x = float(self.entry_ex.text())
            end_y = float(self.entry_ey.text())
        
        except ValueError:
            self.show_warning("Ошибка", "Выберите алгоритм "
                "построения отрезка", "Ubuntu 15")

        except Warning:
            self.show_warning("Ошибка", "Выберите цвет построения", "Ubuntu 15")
        
        except:
            self.show_warning("Ошибка", "Координаты концов отрезка должны быть "
                "вещественными числами", "Ubuntu 15")
        
        else:
            if (alg == 1):
                lib_line(self.scene, start_x, start_y, end_x, end_y, self.get_pen(color))
            if (alg == 2):
                dda(self.scene, start_x, start_y, end_x, end_y, self.get_pen(color))
            if (alg == 3):
                bresenham(self.scene, start_x, start_y, end_x, end_y, self.get_pen(color))
            if (alg == 4):
                int_bresenham(self.scene, start_x, start_y, end_x, end_y, self.get_pen(color))
            if (alg == 5):
                opt_bresenham(self.scene, start_x, start_y, end_x, end_y, self.get_pen(color))
            if (alg == 6):
                wu(self.scene, start_x, start_y, end_x, end_y, self.get_pen(color))
    
    def draw_step(self, alg, color, center_x, center_y, step, length):
        fi = 0
        while (fi < 360):
            end_x = center_x + length * cos(radians(fi))
            end_y = center_y + length * sin(radians(fi))
            fi += step
            if (alg == 0):
                lib_line(self.scene, center_x, center_y, end_x, end_y, self.get_pen(color))
            if (alg == 1):
                dda(self.scene, center_x, center_y, end_x, end_y, self.get_pen(color))
            if (alg == 2):
                bresenham(self.scene, center_x, center_y, end_x, end_y, self.get_pen(color))
            if (alg == 3):
                int_bresenham(self.scene, center_x, center_y, end_x, end_y, self.get_pen(color))
            if (alg == 4):
                opt_bresenham(self.scene, center_x, center_y, end_x, end_y, self.get_pen(color))
            if (alg == 5):
                wu(self.scene, center_x, center_y, end_x, end_y, self.get_pen(color))

    def draw_spectre(self):
        try:
            alg = self.spectre_alg.currentIndex()
            if alg == 0:
                raise ValueError
            color = self.spectre_color.currentIndex()
            if color == 0:
                raise Warning

            center_x = float(self.entry_cx.text())
            center_y = float(self.entry_cy.text())
            angle = float(self.entry_angle.text())
            length = float(self.entry_len.text())
            if length <= 0:
                raise ArithmeticError
        
        except ValueError:
            self.show_warning("Ошибка", "Выберите алгоритм "
                "построения отрезка", "Ubuntu 15")

        except Warning:
            self.show_warning("Ошибка", "Выберите цвет построения", "Ubuntu 15")
        
        except ArithmeticError:
            self.show_warning("Ошибка", "Длина должна быть положительной", 
                "Ubuntu 15")

        except:
            self.show_warning("Ошибка", "Координаты, длина и угол должны быть "
                "вещественными числами", "Ubuntu 15")
        
        else:
            self.draw_step(alg, color, center_x, center_y, angle, length)

    def count_time(self):
        pass

    def count_steps(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()     
