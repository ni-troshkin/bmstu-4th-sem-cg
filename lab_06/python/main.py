from app_interface import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QColor

from time import sleep, time
import sys
from math import sqrt

class Point():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image = QImage(int(self.scene.width()), int(self.scene.height()), QImage.Format_ARGB32_Premultiplied)

        self.seed = None    # затравочная точка

        self.first_point = None    # первая точка незамкнутой фигуры
        self.last_point = None     # текущая последняя точка ломаной

        self.exit_btn.clicked.connect(self.exit)
        self.ellipse_btn.clicked.connect(self.add_ellipse)
        self.clear_btn.clicked.connect(self.clear)
        self.add_btn.clicked.connect(self.add_point)
        self.close_fig_btn.clicked.connect(self.close_figure)
        self.fill_btn.clicked.connect(self.fill_figure)

    def redraw(self):    # обновление сцены
        self.scene.clear()
        pixmap = QtGui.QPixmap(self.image.size())
        pixmap.convertFromImage(self.image)
        self.scene.addPixmap(pixmap)

    # получение цвета по выбору пользователя
    def get_color(self, color_box):
        if color_box.currentIndex() == 1:
            return Qt.red
        if color_box.currentIndex() == 2:
            return Qt.blue
        if color_box.currentIndex() == 3:
            return Qt.black
        if color_box.currentIndex() == 4:
            return Qt.white 

    # проверка события клика мышкой по сцене
    def check_event(self, ev):
        if ev.button() != Qt.LeftButton:
            return 0
        if self.scene.sceneRect().contains(ev.x(), ev.y()):
            return 1
        return 0

    # обработка клика на сцену при задании затравки
    def seed_process(self, x, y):
        try:
            if self.flood_box.currentIndex() == 0:
                raise Warning
        except Warning:
            self.show_message("Ошибка", "Выберите цвет заливки", "Ubuntu 15")
        else:
            if self.seed != None:    # удаляем предыдущую затравку
                self.image.setPixelColor(self.seed.x, self.seed.y, Qt.white)
            self.seed = Point(x, y)
            
            # отмечаем затравку на холсте
            self.image.setPixelColor(x, y, self.get_color(self.flood_box))

    # обработка клика на сцену при задании фигуры
    def bound_process(self, x, y):
        try:
            if self.boundary_color_box.currentIndex() == 0:
                raise Warning
        except Warning:
            self.show_message("Ошибка", "Выберите цвет границ", "Ubuntu 15")
        else:
            if self.radio_hor.isChecked() and self.last_point != None:
                prev_x = self.last_point.x    # построение горизонтального/вертикального отрезка
                prev_y = self.last_point.y
                if abs(x - prev_x) >= abs(y - prev_y):
                    y = prev_y
                else:
                    x = prev_x
            self.add_to_screen(x, y)

    # обработка события - клик мышкой -> добавление точки
    def mousePressEvent(self, ev):
        if self.check_event(ev) == 1:
            ev.accept()
            x = ev.x()
            y = ev.y()

            if self.radio_seed.isChecked():
                self.seed_process(x, y)
            else:
                self.bound_process(x, y)
        self.redraw()

    # добавление точки и соединяющей прямой на экран
    def add_to_screen(self, x, y):
        if self.first_point == None:
            # начало новой незамкнутой фигуры
            self.first_point = Point(x, y)
            self.image.setPixelColor(x, y, self.get_color(self.boundary_color_box))
        else:
            self.add_line(self.last_point.x, self.last_point.y, x, y, 
                            self.get_color(self.boundary_color_box))
        
        self.last_point = Point(x, y)

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
        except:
            self.show_message("Неверные координаты", "Координаты должны "
                "являться вещественными числами", "Ubuntu 15")
        else:
            if self.radio_seed.isChecked():
                self.seed_process(x, y)
            else:
                self.bound_process(x, y)
            self.redraw()

    def get_pixel_color(self, x, y):    # получение цвета пиксела с координатой
        return self.image.pixelColor(x, y)

    # проверка строки на наличие еще не заполненных пикселей
    def check_line_for_seeds(self, y, seeds, x_left, x_right, bound_color, flood_color):
        if y < 0 or y >= self.image.height():
            return seeds
        x = x_left

        while x <= x_right:
            flag = 0
            # нашли незаполненный интервал, ищем его правую точку
            while x < x_right and x < self.image.width() - 1 and \
                self.get_pixel_color(x, y) != bound_color and \
                self.get_pixel_color(x, y) != flood_color:
                if flag == 0:
                    flag = 1
                x += 1
            
            # нашли правую точку, добавили в стек
            if flag == 1:
                if (x == x_right or x == self.image.width() - 1) and \
                    self.get_pixel_color(x, y) != bound_color and \
                    self.get_pixel_color(x, y) != flood_color:
                    seeds.append(Point(x, y))
                else:
                    seeds.append(Point(x - 1, y))
                flag = 0
            
            # проверка, если наткнулись на горизонтальную границу или заполненный интервал
            x_entry = x
            while (x < x_right or x < self.image.width() - 1) and \
                (self.get_pixel_color(x, y) == bound_color or \
                self.get_pixel_color(x, y) == flood_color):
                x += 1
            
            # убеждаемся, что увеличили абсциссу
            if x == x_entry:
                x += 1
        
        return seeds

    # заполнение многоугольника
    def fill_figure(self):
        # проверки на замкнутость, выбор цвета и наличие затравки
        if self.flood_box.currentIndex() == 0:
            self.show_message("Ошибка", "Выберите цвет заливки", "Ubuntu 15")
            return
        if self.first_point != None:
            self.show_message("Ошибка", "Есть незамкнутые многоугольники", "Ubuntu 15")
            return
        if self.seed == None:
            self.show_message("Ошибка", "Введите затравочную точку", "Ubuntu 15")
            return
        if not self.delay_check.isChecked():
            start = time()
            
        flood_color = self.get_color(self.flood_box)    # цвет заливки
        bound_color = self.get_color(self.boundary_color_box)    # цвет границ

        seeds = []    # стек затравок
        seeds.append(self.seed)

        while len(seeds):
            point = seeds.pop()
            x = point.x
            y = point.y

            self.image.setPixelColor(x, y, flood_color)
            x += 1
            # закрашиваем вправо от затравочного пиксела до границы
            while x < self.image.width() and self.get_pixel_color(x, y) != bound_color:
                self.image.setPixelColor(x, y, flood_color)
                x += 1
            x_right = x - 1

            x = point.x - 1
            # закрашиваем влево от затравочного пиксела до границы
            while x >= 0 and self.get_pixel_color(x, y) != bound_color:
                self.image.setPixelColor(x, y, flood_color)
                x -= 1
            x_left = x + 1

            # обновляем стек (ищем незаполненные интервалы над и под текущей строкой)
            seeds = self.check_line_for_seeds(y + 1, seeds, x_left, x_right, bound_color, flood_color)
            seeds = self.check_line_for_seeds(y - 1, seeds, x_left, x_right, bound_color, flood_color)
        
            if self.delay_check.isChecked():    # задержка
                sleep(0)
                self.redraw()
                QtWidgets.QApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        # если заполнение без задержки - вывести сообщение о времени заполнения
        if not self.delay_check.isChecked():
            end = time()
            self.redraw()
            QtWidgets.QApplication.processEvents(QtCore.QEventLoop.AllEvents)
            self.show_message("Закраска успешно завершена", "Время работы алгоритма: {:.1f} "
                                "секунд".format(end - start), "Ubuntu 15", QtWidgets.QMessageBox.Information)

    # добавление эллипса на холст для проверки заполнения области, ограниченной кривой
    def add_ellipse(self):
        try:
            color = self.boundary_color_box.currentIndex()
            if color == 0:
                raise Warning

            center_x = float(self.cx_entry.text())
            center_y = float(self.cy_entry.text())
            a = float(self.a_entry.text())
            b = float(self.b_entry.text())
            
        except Warning:
            self.show_message("Ошибка", "Выберите цвет границ", "Ubuntu 15")
        
        except:
            self.show_message("Ошибка", "Координаты центра эллипса и "
                "полуоси/радиус должны быть вещественными числами", "Ubuntu 15")
        
        else:
            self.add_ellipse_middot(a, b, center_x, center_y, self.get_color(self.boundary_color_box))

    # замыкание многоугольника, соединяем последнюю точку 
    # с первой, не входящей в другую замкнутую фигуру
    def close_figure(self):
        if self.first_point == None:
            self.show_message("Ошибка", "Многоугольник или не начат, или уже замкнут", "Ubuntu 15")
            return
        try:
            if self.boundary_color_box.currentIndex() == 0:
                raise Warning
        except Warning:
            self.show_message("Ошибка", "Выберите цвет границ", "Ubuntu 15")
        else:
            self.add_line(self.last_point.x, self.last_point.y, 
                self.first_point.x, self.first_point.y, self.get_color(self.boundary_color_box))
            self.first_point = None
            self.last_point = None
            self.redraw()

    # Брезенхем
    def add_line(self, start_x, start_y, end_x, end_y, color):
        if abs(end_x - start_x) < 0.5 and abs(end_y - start_y) < 0.5:
            self.image.setPixelColor(int(round(x)), int(round(y)), color)

        x = start_x
        y = start_y

        dx = abs(end_x - start_x)
        dy = abs(end_y - start_y)

        def sign(a):
            if (a < 0):
                return -1
            if (a > 0):
                return 1
            return 0

        signx = sign(end_x - start_x)
        signy = sign(end_y - start_y)

        if dy <= dx: # горизонтальный наклон
            change = 0
        else:
            change = 1    # вертикальный наклон
            dx, dy = dy, dx

        error = 2 * dy - dx

        for i in range(int(dx) + 1):
            self.image.setPixelColor(int(round(x)), int(round(y)), color)
            if error >= 0:
                if change == 1:
                    x += signx
                else:
                    y += signy
                error -= 2 * dx
        
            if error < 0:
                if change == 1:
                    y += signy
                else:
                    x += signx
                error += 2 * dy

    # добавление точек при построении эллипса
    def draw_points(self, cx, cy, x, y, color):
        x, y, cx, cy = int(round(x)), int(round(y)), int(round(cx)), int(round(cy))
        self.image.setPixelColor(x + cx, y + cy, color)
        self.image.setPixelColor(-x + cx, y + cy, color)
        self.image.setPixelColor(x + cx, -y + cy, color)
        self.image.setPixelColor(-x + cx, -y + cy, color)

    # построение эллипса методом средней линии
    def add_ellipse_middot(self, a, b, cx, cy, color):
        x = 0
        y = b

        sq_a = a * a
        sq_b = b * b

        f = sq_b - sq_a * b + sq_a / 4
        y_border = sq_b / sqrt(sq_a + sq_b)

        self.draw_points(cx, cy, x, y, color)
        while y > y_border:
            if f > 0:
                y -= 1
                f -= 2 * sq_a * y
            f += 2 * sq_b * x + sq_b
            x += 1    
            self.draw_points(cx, cy, x, y, color)

        f += 3 / 4 * (sq_a - sq_b) - (sq_b * x + sq_a * y)
        while y >= 0:
            if f < 0:
                x += 1
                f += 2 * sq_b * x
            f += sq_a - 2 * sq_a * y
            y -= 1
            self.draw_points(cx, cy, x, y, color)
        
        self.redraw()

    # очистка экрана
    def clear(self):
        self.scene.clear()
        self.image.fill(Qt.white)
        self.seed = None
        self.first_point = None
        self.last_point = None

    def exit(self):
        sys.exit(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
