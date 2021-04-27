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
        self.code = [0, 0, 0, 0]

class Cutter():
    def __init__(self, color, left=0, right=0, top=0, bottom=0):
        self.left = int(left)
        self.right = int(right)
        self.top = int(top)
        self.bottom = int(bottom)

        self.color = color

        self.top_line = Line(Point(self.left, self.top), Point(self.right, self.top))
        self.bottom_line = Line(Point(self.left, self.bottom), Point(self.right, self.bottom))
        self.left_line = Line(Point(self.left, self.top), Point(self.left, self.bottom))
        self.right_line = Line(Point(self.right, self.top), Point(self.right, self.bottom))

class Line():
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image = QImage(int(self.scene.width()), int(self.scene.height()), QImage.Format_ARGB32_Premultiplied)

        self.cutter = None
        self.buf_cutter = None
        self.waiting_for_second_point = False
        self.lines = []

        self.begin_point = None

        self.exit_btn.clicked.connect(self.exit)
        self.cut_btn.clicked.connect(self.cut_lines)
        self.cutter_btn.clicked.connect(self.edit_cutter)
        self.clear_btn.clicked.connect(self.clear)
        self.add_btn.clicked.connect(self.add_point)

    def update(self):    # обновление сцены
        self.scene.clear()
        print("HELLO")
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
            return Qt.darkGreen
        if color_box.currentIndex() == 5:
            return Qt.darkYellow
        if color_box.currentIndex() == 6:
            return Qt.darkMagenta
        if color_box.currentIndex() == 7:
            return Qt.white

    # проверка события клика мышкой по сцене
    def check_event(self, ev):
        if ev.button() != Qt.LeftButton:
            return 0
        if self.scene.sceneRect().contains(ev.x(), ev.y()):
            return 1
        return 0

    def copy_cutter(self, color):
        if self.cutter == None:
            self.cutter = Cutter(color, self.buf_cutter.left, self.buf_cutter.right, 
                self.buf_cutter.top, self.buf_cutter.bottom)
        else:
            self.erase_cutter()
            print(self.buf_cutter.top, self.buf_cutter.bottom)
            self.cutter = Cutter(color, self.buf_cutter.left, self.buf_cutter.right, 
                self.buf_cutter.top, self.buf_cutter.bottom)
        self.draw_cutter(color)
        self.update()

    # обработка клика на сцену при задании отсекателя
    def cutter_process(self, x, y):
        try:
            if self.cutter_box.currentIndex() == 0:
                raise Warning
        except Warning:
            self.show_message("Ошибка", "Выберите цвет отсекателя", "Ubuntu 15")
        else:
            color = self.get_color(self.cutter_box)
            if not self.waiting_for_second_point:
                self.buf_cutter = Cutter(color)
                self.buf_cutter.left = x
                self.buf_cutter.top = y
                self.waiting_for_second_point = True
                self.draw_point(color, x, y)
                # self.label = QtWidgets.QLabel("({:3d, :3d})".format(x, y))
                self.update()
            else:
                if x < self.buf_cutter.left:
                    self.buf_cutter.right, self.buf_cutter.left = self.buf_cutter.left, x
                else:
                    self.buf_cutter.right = x
                
                if y > self.buf_cutter.top:
                    self.buf_cutter.bottom, self.buf_cutter.top = self.buf_cutter.top, y
                else:
                    self.buf_cutter.bottom = y

                self.waiting_for_second_point = False
                # self.label2 = QtWidgets.QLabel("({:3d, :3d})".format(x, y))
                # self.label2.setPos(x + 15, y + 15)
                self.copy_cutter(color)

    # обработка клика на сцену при задании фигуры
    def line_process(self, x, y, ev = None):
        try:
            if self.line_box.currentIndex() == 0:
                raise Warning
        except Warning:
            self.show_message("Ошибка", "Выберите цвет отрезков", "Ubuntu 15")
        else:
            ctrl = False
            shift = False
            if ev != None:
                if ev.modifiers() == Qt.ControlModifier:
                    ctrl = True
                if ev.modifiers() == Qt.ShiftModifier:
                    shift = True
            if ctrl and self.begin_point != None:
                prev_x = self.begin_point.x    # построение горизонтального/вертикального отрезка
                prev_y = self.begin_point.y
                if abs(x - prev_x) >= abs(y - prev_y):
                    y = prev_y
                else:
                    x = prev_x
            if shift and self.cutter != None:
                to_top = abs(y - self.cutter.top)
                to_bottom = abs(y - self.cutter.bottom)
                to_left = abs(x - self.cutter.left)
                to_right = abs(x - self.cutter.right)
                l_min = min(to_top, to_bottom, to_left, to_right)
                if l_min == to_top:
                    y = self.cutter.top
                elif l_min == to_bottom:
                    y = self.cutter.bottom
                elif l_min == to_left:
                    x = self.cutter.left
                else:
                    x = self.cutter.right
                
            self.add_to_screen(x, y)

    # обработка события - клик мышкой -> добавление точки
    def mousePressEvent(self, ev):
        if self.check_event(ev) == 1:
            ev.accept()
            x = ev.x()
            y = ev.y()

            if self.radio_cutter.isChecked():
                self.cutter_process(x, y)
            else:
                self.line_process(x, y, ev)
        

    # добавление точки и соединяющей прямой на экран
    def add_to_screen(self, x, y):
        if self.begin_point == None:
            # начало новой незамкнутой фигуры
            self.begin_point = Point(x, y)
            self.image.setPixelColor(x, y, self.get_color(self.line_box))
        else:
            line = Line(self.begin_point, Point(x, y))
            self.draw_line(self.get_color(self.line_box), line)
            self.lines.append(line)
        
            self.begin_point = None
        self.draw_point(self.get_color(self.line_box), x, y)
        self.update()

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
                "являться целыми числами", "Ubuntu 15")
        else:
            self.line_process(x, y)
            self.update()

    def get_pixel_color(self, x, y):    # получение цвета пиксела с координатой
        return self.image.pixelColor(x, y)
    
    def edit_cutter(self):
        try:
            top = int(self.top_entry.text())
            bottom = int(self.bottom_entry.text())
            left = int(self.left_entry.text())
            right = int(self.right_entry.text())
            if self.cutter_box.currentIndex() == 0:
                raise Warning
        except Warning:
            self.show_message("Ошибка", "Выберите цвет отсекателя", "Ubuntu 15")
        except:
            self.show_message("Неверные координаты", "Координаты должны "
                "являться целыми числами", "Ubuntu 15")
        else:
            color = self.get_color(self.cutter_box)
            if top < bottom:
                top, bottom = bottom, top
            self.buf_cutter = Cutter(color, left, right, top, bottom)
            self.copy_cutter(color)

    # Брезенхем
    def draw_line(self, color, line):
        print(line.start.x, line.start.y, "->", line.end.x, line.end.y)
        if color == Qt.white:
            print("White")
        else:
            print("Not White")
        if abs(line.end.x - line.start.x) < 0.5 and abs(line.end.y - line.start.y) < 0.5:
            self.image.setPixelColor(int(round(line.end.x)), int(round(line.end.y)), color)
            return

        x = line.start.x
        y = line.start.y

        dx = abs(line.end.x - line.start.x)
        dy = abs(line.end.y - line.start.y)

        def sign(a):
            if (a < 0):
                return -1
            if (a > 0):
                return 1
            return 0

        signx = sign(line.end.x - line.start.x)
        signy = sign(line.end.y - line.start.y)

        if dy <= dx: # горизонтальный наклон
            change = 0
        else:
            change = 1    # вертикальный наклон
            dx, dy = dy, dx

        error = 2000 * dy - 1000 * dx + int(100 * (line.start.x - int(line.start.x)))
        if error >= 0:
            if change == 1:
                x += signx
            else:
                y += signy
            error -= 2000 * dx

        for i in range(int(dx) + 1):
            self.image.setPixelColor(int(round(x)), int(round(y)), color)
            
            if color == self.get_color(self.result_box):
                self.image.setPixelColor(int(round(x)), int(round(y - signy)), color)
            
            if error >= 0:
                if change == 1:
                    x += signx
                else:
                    y += signy
                error -= 2000 * dx
        
            if error < 0:
                if change == 1:
                    y += signy
                else:
                    x += signx
                error += 2000 * dy

    def erase_cutter(self):
        self.draw_cutter(Qt.white)

    def draw_cutter(self, color):
        self.draw_line(color, self.cutter.top_line)
        self.draw_line(color, self.cutter.bottom_line)
        self.draw_line(color, self.cutter.left_line)
        self.draw_line(color, self.cutter.right_line)
    
    def draw_point(self, color, x, y):
        self.image.setPixelColor(x, y, color)
        self.image.setPixelColor(x - 1, y, color)
        self.image.setPixelColor(x + 1, y, color)
        self.image.setPixelColor(x, y - 1, color)
        self.image.setPixelColor(x - 1, y - 1, color)
        self.image.setPixelColor(x + 1, y - 1, color)
        self.image.setPixelColor(x, y + 1, color)
        self.image.setPixelColor(x - 1, y + 1, color)
        self.image.setPixelColor(x + 1, y + 1, color)

    def is_visible(self, line, params):
        sum1 = self.get_code(line.start, params)
        sum2 = self.get_code(line.end, params)
        result = 0
        if sum1 == 0 and sum2 == 0:
            result = 1
        else:
            if self.is_invisible(line):
                result = -1
        return result
    
    def get_code(self, point, params):
        point.code[3] = 1 if point.x < self.cutter.left else 0
        point.code[2] = 1 if point.x > self.cutter.right else 0
        point.code[1] = 1 if point.y < self.cutter.bottom else 0
        point.code[0] = 1 if point.y > self.cutter.top else 0

        return sum(point.code)
    
    def is_invisible(self, line):
        prod = 0
        for i in range(4):
            prod += int((line.start.code[i] + line.end.code[i]) / 2)
        return prod

    def cut_line(self, line):
        color = self.get_color(self.result_box)
        flag = 1
        if line.end.x - line.start.x == 0:
            flag = -1
        else:
            k = (line.end.y - line.start.y) / (line.end.x - line.start.x)
            if k == 0:
                flag = 0
        cutter_params = [self.cutter.left, self.cutter.right, self.cutter.bottom, self.cutter.top]
        for i in range(4):
            print(cutter_params)
            print(line.start.x, line.start.y, "->", line.end.x, line.end.y)
            print(i, cutter_params[i])
            visible = self.is_visible(line, cutter_params)
            print(line.start.code, line.end.code)
            if visible == 1:
                print("visible")
                self.draw_line(color, line)
                return
            if visible == -1:

                return
            if line.start.code[3 - i] == line.end.code[3 - i]:
                continue
            if line.start.code[3 - i] == 0:
                print("changed")
                line.start, line.end = line.end, line.start
            if flag != -1 and i <= 1:
                print("!")
                line.start.y = k * (cutter_params[i] - line.start.x) + line.start.y
                line.start.x = cutter_params[i]
            else:
                if flag != 0:
                    if flag != -1:
                        line.start.x = (1 / k) * (cutter_params[i] - line.start.y) + line.start.x
                    line.start.y = cutter_params[i]
        self.draw_line(color, line)

    def cut_lines(self):
        try:
            if self.result_box.currentIndex() == 0:
                raise Warning

            if self.cutter == None:
                raise TypeError
        except Warning:
            self.show_message("Ошибка", "Выберите цвет результата", "Ubuntu 15")
        except:
            self.show_message("Ошибка", "Задайте отсекатель", "Ubuntu 15")
        
        for line in self.lines:
            self.cut_line(line)
        
        self.update()

    # очистка экрана
    def clear(self):
        self.scene.clear()
        self.image.fill(Qt.white)
        self.lines.clear()

    def exit(self):
        sys.exit(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
