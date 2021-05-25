from app_interface import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QColor, QPen

import sys
from math import sqrt

class Point():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class Vector():
    def __init__(self, a = Point(0, 0), b = Point(0, 0)):
        self.x = b.x - a.x
        self.y = b.y - a.y
    
    def set_coords(self, x, y):
        self.x = x
        self.y = y
    
    # скалярное произведение
    def product(self, vector):
        return self.x * vector.x + self.y * vector.y
    
    # векторное произведение
    def cross_product(self, vector):
        return self.x * vector.y - self.y * vector.x
    
class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cutter = []
        self.cutter_is_closed = True

        self.figure = []
        self.figure_is_closed = True

        self.exit_btn.clicked.connect(self.exit)
        self.cut_btn.clicked.connect(self.cut_figure)
        self.close_btn.clicked.connect(self.close_polygon)
        self.clear_btn.clicked.connect(self.clear)
        self.add_btn.clicked.connect(self.add_point)

    # получение цвета по выбору пользователя
    def get_color(self, color_box):
        if color_box.currentIndex() == 1:
            return Qt.red
        if color_box.currentIndex() == 2:
            return Qt.blue
        if color_box.currentIndex() == 3:
            return Qt.black
        if color_box.currentIndex() == 4:
            return Qt.darkGreen
        if color_box.currentIndex() == 5:
            return Qt.darkYellow
        if color_box.currentIndex() == 6:
            return Qt.darkMagenta
        if color_box.currentIndex() == 7:
            return Qt.white

    # формирование окна с сообщением с заданным текстом
    def show_message(self, title, text, font, icon = QtWidgets.QMessageBox.Warning):
        msg = QtWidgets.QMessageBox()
        msg.setGeometry(800, 400, 250, 200)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setFont(QtGui.QFont(font))
        msg.setIcon(icon)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    # проверка события клика мышкой по сцене
    def check_event(self, ev):
        if ev.button() != Qt.LeftButton:
            return 0
        if self.scene.sceneRect().contains(ev.x(), ev.y()):
            return 1
        return 0

    # обработка клика на сцену при задании фигуры
    def line_process(self, x, y, ev = None):            
        ctrl = False    # возможность ввода горизонтального/вертикального ребра
        shift = False    # возможность привязки к ребру отсекателя
        alt = False    # возможность привязки к вершине отсекателя
        if ev != None:
            if ev.modifiers() == Qt.ControlModifier:
                ctrl = True
            if ev.modifiers() == Qt.ShiftModifier:
                shift = True
            if ev.modifiers() == Qt.AltModifier:
                alt = True
        
        if ctrl: 
            if self.radio_cutter.isChecked() and not self.cutter_is_closed:
                prev_x = self.cutter[-1].x    # построение горизонтального/вертикального отрезка отсекателя
                prev_y = self.cutter[-1].y
            elif self.radio_figure.isChecked() and not self.figure_is_closed:
                prev_x = self.figure[-1].x    # построение горизонтального/вертикального отрезка многоугольника
                prev_y = self.figure[-1].y
            else:
                prev_y = y
                prev_x = x
            
            if abs(x - prev_x) >= abs(y - prev_y):
                y = prev_y
            else:
                x = prev_x

        # находим вершину, ближайшую к месту клика, и ставим в нее новую точку
        if alt and self.radio_figure.isChecked() and self.cutter != []:
            min_dist_2 = 10000 * 10000
            vertex = 0
            for i in range(len(self.cutter)):
                dist_2 = (x - self.cutter[i].x) ** 2 + (y - self.cutter[i].y) ** 2
                if dist_2 < min_dist_2:
                    min_dist_2 = dist_2
                    vertex = i
            x = self.cutter[vertex].x
            y = self.cutter[vertex].y
        
        if shift and self.radio_figure.isChecked() and len(self.cutter) >= 2:
            # находим ребро отсекателя, ближе всего к которому поставлена точка
            # и строим точку на нем (в основании перпендикуляра к ребру)
            min_dist = 10000    # минимальное расстояние до ребра
            k_min = None
            vertex = 0
            for i in range(len(self.cutter)):
                # угловой коэффициент ребра (ах + ву + с = 0)
                # проверка вертикальности ребра
                if abs(self.cutter[(i + 1) % len(self.cutter)].x - self.cutter[i].x) > 1e-7:
                    a = (self.cutter[(i + 1) % len(self.cutter)].y - self.cutter[i].y)\
                        / (self.cutter[(i + 1) % len(self.cutter)].x - self.cutter[i].x)
                    b = -1
                    c = self.cutter[i].y - a * self.cutter[i].x
                    # расстояние до i-го ребра отсекателя от первой точки отрезка
                    dist = abs(a * x + b * y + c) / sqrt(a * a + b * b)
                else:
                    dist = abs(x - self.cutter[i].x)
                    a = None
                if dist < min_dist:
                    min_dist = dist
                    k_min = a
                    vertex = i
            if k_min != None:
                dy = min_dist / sqrt(k_min * k_min + 1)
                dx = -k_min * dy
                if abs(k_min * (x + dx) - (y + dy) + self.cutter[vertex].y - k_min * self.cutter[vertex].x) > 1e-5:
                    dx, dy = -dx, -dy
            else:
                dy = 0
                dx = self.cutter[vertex].x - x
            
            x += dx
            y += dy
        self.add_to_screen(x, y)

    # обработка события - клик мышкой -> добавление точки
    def mousePressEvent(self, ev):
        if self.check_event(ev) == 1:
            ev.accept()
            x = ev.x()
            y = ev.y()

            # проверка, выбран ли цвет
            try:
                if self.radio_cutter.isChecked() and self.cutter_box.currentIndex() == 0:
                    raise Warning
                if self.radio_figure.isChecked() and self.figure_box.currentIndex() == 0:
                    raise TypeError
            except Warning:
                self.show_message("Ошибка", "Выберите цвет отсекателя", "Ubuntu 15")
            except:
                self.show_message("Ошибка", "Выберите цвет отсекаемого многоугольника", "Ubuntu 15")
            else:
                self.line_process(x, y, ev)

    # добавление точки и соединяющей прямой на экран
    def add_to_screen(self, x, y):
        if self.radio_cutter.isChecked():
            color = self.get_color(self.cutter_box)
            self.cutter.append(Point(x, y))
            if self.cutter_is_closed:
                self.cutter_is_closed = False
                if len(self.cutter) != 1:
                    self.erase_cutter()
                    self.cutter.append(Point(x, y))
                self.draw_point(color, x, y)
            else:
                self.scene.addLine(self.cutter[-2].x, self.cutter[-2].y, 
                                    self.cutter[-1].x, self.cutter[-1].y, QPen(color))
        else:
            color = self.get_color(self.figure_box)
            self.figure.append(Point(x, y))
            if self.figure_is_closed:
                self.figure_is_closed = False
                if len(self.figure) != 1:
                    self.erase_figure()
                    self.figure.append(Point(x, y))
                self.draw_point(color, x, y)
            else:
                self.scene.addLine(self.figure[-2].x, self.figure[-2].y, 
                                    self.figure[-1].x, self.figure[-1].y, QPen(color))

    # добавление точки с точными координатами
    def add_point(self):
        try:
            x = int(self.x_entry.text())
            y = int(self.y_entry.text())
        except:
            self.show_message("Неверные координаты", "Координаты должны "
                "являться целыми числами", "Ubuntu 15")
        else:
            self.line_process(x, y)

    # стереть отсекатель
    def erase_cutter(self):
        for i in range(len(self.cutter) - 1):
            self.scene.addLine(self.cutter[i].x, self.cutter[i].y, 
                                    self.cutter[i + 1].x, self.cutter[i + 1].y, QPen(Qt.white))
        self.scene.addLine(self.cutter[-1].x, self.cutter[-1].y, self.cutter[0].x, self.cutter[0].y, QPen(Qt.white))
        self.cutter.clear()
    
    # стереть многоугольник
    def erase_figure(self):
        for i in range(len(self.figure) - 1):
            self.scene.addLine(self.figure[i].x, self.figure[i].y, 
                                    self.figure[i + 1].x, self.figure[i + 1].y, QPen(Qt.white))
        self.scene.addLine(self.figure[-1].x, self.figure[-1].y, self.figure[0].x, self.figure[0].y, QPen(Qt.white))
        self.figure.clear()
    
    # рисуем точку
    def draw_point(self, color, x, y):
        self.scene.addLine(x - 1, y - 1, x + 1, y - 1, QPen(color))
        self.scene.addLine(x - 1, y, x + 1, y, QPen(color))
        self.scene.addLine(x - 1, y + 1, x + 1, y + 1, QPen(color))

    def sign(self, a):
        if a < 0:
            return -1
        if a > 0:
            return 1
        return 0

    # определение видимости точки относительно ребра отсекателя
    def point_is_visible(self, point, start, end):
        cross_product = (point.x - start.x) * (end.y - start.y)
        cross_product -= (point.y - start.y) * (end.x - start.x)
        return self.sign(cross_product)

    # проверка пересечения ребра многоугольника с ребром отсекателя
    def has_intersection(self, fig_start, fig_end, cut_start, cut_end):
        fig_start_is_visible = self.point_is_visible(fig_start, cut_start, cut_end)
        fig_end_is_visible = self.point_is_visible(fig_end, cut_start, cut_end)
        if fig_start_is_visible * fig_end_is_visible < 0:
            return True
        return False

    # инверсия матрицы
    def inv(self, matrix):
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        inv_matr = [[matrix[1][1] / det, -matrix[0][1] / det],
                    [-matrix[1][0] / det, matrix[0][0] / det]]
        return inv_matr

    # получение точки пересечения ребра многоугольника с ребром отсекателя
    def get_intersection(self, fig_start, fig_end, cut_start, cut_end):
        # используются параметрические уравнения для прямых
        coeffs = [[fig_end.x - fig_start.x, cut_start.x - cut_end.x], 
                    [fig_end.y - fig_start.y, cut_start.y - cut_end.y]]
        right_parts = [[cut_start.x - fig_start.x], [cut_start.y - fig_start.y]]
        # решаем систему из двух уравнений в матричном виде
        coeffs = self.inv(coeffs)
        param = [[coeffs[0][0] * right_parts[0][0] + coeffs[0][1] * right_parts[1][0]],
                [coeffs[1][0] * right_parts[0][0] + coeffs[1][1] * right_parts[1][0]]]
        x = fig_start.x + (fig_end.x - fig_start.x) * param[0][0]
        y = fig_start.y + (fig_end.y - fig_start.y) * param[0][0]
        return Point(x, y)

    # проверка выпуклости многоугольника
    def is_convex(self):
        # меньше трех вершин - какой ты многоугольник после этого?
        if len(self.cutter) < 3:
            return False
        
        # проверяем, что все векторные произведения смежных сторон отсекателя 
        # одного знака, за эталон берем первые два ребра
        vect1 = Vector(self.cutter[0], self.cutter[1])
        vect2 = Vector(self.cutter[1], self.cutter[2])

        if vect1.cross_product(vect2) > 0:
            sign = 1
        else:
            sign = -1

        # проверка остальных сторон
        for i in range(3, len(self.cutter) + 2):
            vect1 = vect2
            if i < len(self.cutter):
                vect2 = Vector(self.cutter[i - 1], self.cutter[i])
            elif i == len(self.cutter):
                vect2 = Vector(self.cutter[-1], self.cutter[0])
            else:
                vect2 = Vector(self.cutter[0], self.cutter[1])
            
            if sign * vect1.cross_product(vect2) < 0:
                return False

        return True

    # отсечение всех текущих отрезков текущим отсекателем
    def cut_figure(self):
        try:
            if self.result_box.currentIndex() == 0:
                raise Warning

            if self.cutter == [] or not self.cutter_is_closed or not self.is_convex():
                raise TypeError

            if self.figure == [] or not self.figure_is_closed:
                raise IOError

        except Warning:
            self.show_message("Ошибка", "Выберите цвет результата", "Ubuntu 15")
        except TypeError:
            self.show_message("Ошибка", "Задайте замкнутый выпуклый отсекатель", "Ubuntu 15")
        except IOError:
            self.show_message("Ошибка", "Задайте замкнутый многоугольник для отсечения", "Ubuntu 15")

        else:
            # создаем копию отсекаемого многоугольника
            copy_figure = []
            for i in range(len(self.figure)):
                copy_figure.append(self.figure[i])
            
            self.cutter.append(self.cutter[0])   # последняя вершина совпадает с первой
            for i in range(len(self.cutter) - 1):    # цикл по сторонам отсекателя
                result = []        # массив вершин результирующего многоугольника
                for j in range(len(copy_figure)):    # цикл по сторонам многоугольника
                    if j == 0:
                        f = copy_figure[j]         # сохраняем первую вершину
                    else:
                        if self.has_intersection(s, copy_figure[j], self.cutter[i], self.cutter[i + 1]):
                            intersec = self.get_intersection(s, copy_figure[j], self.cutter[i], self.cutter[i + 1])
                            result.append(intersec)    # есть пересечение ребра с отсекателем - добавляем в массив
                    s = copy_figure[j]
                    if self.point_is_visible(s, self.cutter[i], self.cutter[i + 1]) >= 0:
                        # конечная вершина внутри отсекателя - добавляем ее - она будет начальной при следующем шаге
                        result.append(s)
                if len(result) == 0:
                    break    # ребра полностью невидимы относительно одного ребра отсекателя - многоугольник невидим
                # проверяем ребро, которому принадлежат первая и последняя вершины
                if self.has_intersection(s, f, self.cutter[i], self.cutter[i + 1]):
                    intersec = self.get_intersection(s, f, self.cutter[i], self.cutter[i + 1])
                    result.append(intersec)
                # теперь результат - новый многоугольник, который мы будем отсекать следующим ребром
                copy_figure = result.copy()
            
            # визуализация
            color = self.get_color(self.result_box)
            pen = QPen(color)
            pen.setWidth(2)

            for i in range(len(copy_figure) - 1):
                self.scene.addLine(copy_figure[i].x, copy_figure[i].y, 
                                        copy_figure[i + 1].x, copy_figure[i + 1].y, pen)
            self.scene.addLine(copy_figure[-1].x, copy_figure[-1].y, copy_figure[0].x, copy_figure[0].y, pen)

    # замыкание многоугольника
    def close_polygon(self):
        if self.radio_cutter.isChecked():
            try:
                if self.cutter_box.currentIndex() == 0:
                    raise Warning
                if len(self.cutter) < 3:
                    raise TypeError
            except Warning:
                self.show_message("Ошибка", "Выберите цвет отсекателя", "Ubuntu 15")
            except:
                self.show_message("Ошибка", "Для замкнутого многоугольника необходимо "
                    "хотя бы три точки", "Ubuntu 15")
            else:
                color = self.get_color(self.cutter_box)
                self.scene.addLine(self.cutter[-1].x, self.cutter[-1].y, 
                                            self.cutter[0].x, self.cutter[0].y, QPen(color))
                self.cutter_is_closed = True
        else:
            try:
                if self.figure_box.currentIndex() == 0:
                    raise Warning
                if len(self.figure) < 3:
                    raise TypeError
            except Warning:
                self.show_message("Ошибка", "Выберите цвет отсекатемого многоугольника", "Ubuntu 15")
            except:
                self.show_message("Ошибка", "Для замкнутого многоугольника необходимо "
                    "хотя бы три точки", "Ubuntu 15")
            else:
                color = self.get_color(self.figure_box)
                self.scene.addLine(self.figure[-1].x, self.figure[-1].y, 
                                            self.figure[0].x, self.figure[0].y, QPen(color))
                self.figure_is_closed = True

    # очистка экрана
    def clear(self):
        self.scene.clear()
        self.cutter.clear()
        self.cutter_is_closed = True
        self.figure.clear()
        self.figure_is_closed = True

    def exit(self):
        sys.exit(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
