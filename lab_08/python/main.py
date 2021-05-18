import sys
from app_interface import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QColor, QPen

from math import sqrt

# комментарии

class Point():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class Line():
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
class Vector():
    def __init__(self, a = Point(0, 0), b = Point(0, 0)):
        self.x = b.x - a.x
        self.y = b.y - a.y
    
    def set_coords(self, x, y):
        self.x = x
        self.y = y
    
    def product(self, vector):
        return self.x * vector.x + self.y * vector.y
    
    def cross_product(self, vector):
        return self.x * vector.y - self.y * vector.x

    
class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cutter = []    # отсекатель
        self.cutter_is_closed = True

        self.lines = []    # список отрезков
        self.begin_point = None    # флаг ожидания второй точки отрезка

        self.exit_btn.clicked.connect(self.exit)
        self.vertex_btn.clicked.connect(self.add_vertex)
        self.cut_btn.clicked.connect(self.cut)
        self.close_btn.clicked.connect(self.close_cutter)
        self.add_btn.clicked.connect(self.add_point)
        self.clear_btn.clicked.connect(self.clear)

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

    # обработка события - клик мышкой -> добавление точки
    def mousePressEvent(self, ev):
        if self.check_event(ev) == 1:
            ev.accept()
            x = ev.x()
            y = ev.y()

            try:
                if self.radio_cutter.isChecked() and self.cutter_box.currentIndex() == 0:
                    raise Warning
                if self.radio_line.isChecked() and self.line_box.currentIndex() == 0:
                    raise TypeError
            except Warning:
                self.show_message("Ошибка", "Выберите цвет отсекателя", "Ubuntu 15")
            except:
                self.show_message("Ошибка", "Выберите цвет отрезков", "Ubuntu 15")
            else:
                self.line_process(x, y, ev)

    # обработка клика на сцену при задании фигуры
    def line_process(self, x, y, ev = None):
        ctrl = False    # возможность ввода горизонтального/вертикального отрезка
        shift = False    # возможность привязки одной из координат к отсекателю
        if ev != None:
            if ev.modifiers() == Qt.ControlModifier:
                ctrl = True
            if ev.modifiers() == Qt.ShiftModifier:
                shift = True
        
        if ctrl:
            if self.radio_line.isChecked() and self.begin_point != None:
                prev_x = self.begin_point.x    # построение горизонтального/вертикального отрезка
                prev_y = self.begin_point.y
            elif not self.cutter_is_closed and self.radio_cutter.isChecked():
                prev_x = self.cutter[-1].x
                prev_y = self.cutter[-1].y
            else:
                self.add_to_screen(x, y)
                return
            if abs(x - prev_x) >= abs(y - prev_y):
                y = prev_y
            else:
                x = prev_x

        if shift and len(self.cutter) >= 2 and self.radio_line.isChecked() and self.begin_point != None:
            # находим ребро отсекателя, ближе всего к которому поставлена точка
            # и привязываем одну из координат к координате этого ребра
            min_dist = 1500
            k_min = None
            for i in range(len(self.cutter)):
                a = (self.cutter[(i + 1) % len(self.cutter)].y - self.cutter[i].y)\
                    / (self.cutter[(i + 1) % len(self.cutter)].x - self.cutter[i].x)
                b = -1
                c = self.cutter[i].y - a * self.cutter[i].x
                dist = abs(a * self.begin_point.x + b * self.begin_point.y + c) / sqrt(a * a + b * b)
                if dist < min_dist:
                    min_dist = dist
                    k_min = a
            
            length = sqrt((x - self.begin_point.x) ** 2 + (y - self.begin_point.y) ** 2)
            dx = sqrt(length * length / (1 + k_min * k_min))
            dy = dx * k_min
            if (x - self.begin_point.x) * dx < 0:
                dx, dy = -dx, -dy
            
            x = self.begin_point.x + dx
            y = self.begin_point.y + dy

        self.add_to_screen(x, y)

    # добавление точки и соединяющей прямой на экран
    def add_to_screen(self, x, y, is_cutter = None):
        if self.radio_line.isChecked() and is_cutter == None or is_cutter == False:
            if self.begin_point == None:
                self.begin_point = Point(x, y)
            else:
                line = Line(self.begin_point, Point(x, y))
                self.scene.addLine(line.start.x, line.start.y, line.end.x, line.end.y, QPen(self.get_color(self.line_box)))
                self.lines.append(line)
            
                self.begin_point = None
            self.draw_point(self.get_color(self.line_box), x, y)
        
        if self.radio_cutter.isChecked() and is_cutter == None or is_cutter == True:
            color = self.get_color(self.cutter_box)
            self.cutter.append(Point(x, y))
            if self.cutter_is_closed:
                self.cutter_is_closed = False
                self.draw_point(color, x, y)
            else:
                self.scene.addLine(self.cutter[-2].x, self.cutter[-2].y, 
                                    self.cutter[-1].x, self.cutter[-1].y, QPen(color))

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

    # добавление точки с точными координатами
    def add_point(self):
        try:
            x = int(self.x_entry.text())
            y = int(self.y_entry.text())
            if self.line_box.currentIndex() == 0:
                raise Warning
        except Warning:
            self.show_message("Ошибка", "Выберите цвет отрезков", "Ubuntu 15")
        except:
            self.show_message("Неверные координаты", "Координаты должны "
                "являться целыми числами", "Ubuntu 15")
        else:
            self.add_to_screen(x, y, False)

    # добавление точки с точными координатами
    def add_vertex(self):
        try:
            x = int(self.ver_x_entry.text())
            y = int(self.ver_y_entry.text())
            if self.cutter_box.currentIndex() == 0:
                raise Warning
        except Warning:
            self.show_message("Ошибка", "Выберите цвет отсекателя", "Ubuntu 15")
        except:
            self.show_message("Неверные координаты", "Координаты должны "
                "являться целыми числами", "Ubuntu 15")
        else:
            self.add_to_screen(x, y, True)
    
    # рисуем точку
    def draw_point(self, color, x, y):
        self.scene.addLine(x - 1, y - 1, x + 1, y - 1, QPen(color))
        self.scene.addLine(x - 1, y, x + 1, y, QPen(color))
        self.scene.addLine(x - 1, y + 1, x + 1, y + 1, QPen(color))

    def is_convex(self):
        if len(self.cutter) < 3:
            return False
        
        vect1 = Vector(self.cutter[0], self.cutter[1])
        vect2 = Vector(self.cutter[1], self.cutter[2])

        if vect1.cross_product(vect2) > 0:
            sign = 1
        else:
            sign = -1

        for i in range(3, len(self.cutter)):
            vect1 = Vector(self.cutter[i - 2], self.cutter[i - 1])
            vect2 = Vector(self.cutter[i - 1], self.cutter[i])

            if sign * vect1.cross_product(vect2) < 0:
                return False

        return True
    
    def get_normal(self, line, check_point):
        vect = Vector(line.start, line.end)
        normal = Vector()

        if vect.x == 0:
            normal.set_coords(1, 0)
        else:
            normal.set_coords(-vect.y / vect.x, 1)
        
        if normal.product(Vector(line.end, check_point)) < 0:
            normal.x, normal.y = -normal.x, -normal.y
        
        return normal

    def cut_line(self, line):
        direction = Vector(line.start, line.end)
        t_min = 0
        t_max = 1
        for i in range(len(self.cutter)):
            c_line = Line(self.cutter[i], self.cutter[(i + 1) % len(self.cutter)])
            normal = self.get_normal(c_line, self.cutter[(i + 2) % len(self.cutter)])
            border_point = self.cutter[i]
            w_vect = Vector(border_point, line.start)
            w_prod = w_vect.product(normal)
            d_prod = direction.product(normal)
            if d_prod != 0:
                t = -w_prod / d_prod
                if d_prod > 0:
                    if t > 1:
                        return
                    t_min = max(t, t_min)
                else:
                    if t < 0:
                        return
                    t_max = min(t, t_max)
            elif w_prod < 0:
                return
        if t_min > t_max:
            return
        
        color = self.get_color(self.result_box)
        pen = QPen(color)
        pen.setWidth(2)

        start_x = line.start.x + (line.end.x - line.start.x) * t_min
        start_y = line.start.y + (line.end.y - line.start.y) * t_min
        
        end_x = line.start.x + (line.end.x - line.start.x) * t_max
        end_y = line.start.y + (line.end.y - line.start.y) * t_max

        self.scene.addLine(start_x, start_y, end_x, end_y, pen)

    def cut(self):
        try:
            if not self.is_convex():
                raise Warning
            if self.result_box.currentIndex() == 0:
                raise TypeError
        except Warning:
            self.show_message("Ошибка", "Отсекатель невыпуклый", "Ubuntu 15")
        except:
            self.show_message("Ошибка", "Выберите цвет результата", "Ubuntu 15")
        else:
            for line in self.lines:
                start = Point(line.start.x, line.start.y)
                end = Point(line.end.x, line.end.y)
                buf_line = Line(start, end)
                self.cut_line(buf_line)

    def close_cutter(self):
        color = self.get_color(self.cutter_box)
        self.scene.addLine(self.cutter[-1].x, self.cutter[-1].y, 
                                    self.cutter[0].x, self.cutter[0].y, QPen(color))
        self.cutter_is_closed = True

    # очистка экрана
    def clear(self):
        self.scene.clear()
        self.lines.clear()
        self.begin_point = None
        self.cutter.clear()
        self.cutter_is_closed = True

    def exit(self):
        sys.exit(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
