from app_interface import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QColor, QPen

import sys
from math import sqrt, sin, cos, pi
from functions import *

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.clear_btn.clicked.connect(self.clear)
        self.exit_btn.clicked.connect(self.exit)
        self.draw_btn.clicked.connect(self.draw_surface)
        self.scale_btn.clicked.connect(self.scale)
        self.x_rotate_btn.clicked.connect(self.rotation_x)
        self.y_rotate_btn.clicked.connect(self.rotation_y)
        self.z_rotate_btn.clicked.connect(self.rotation_z)

        self.width = int(self.scene.width())
        self.height = int(self.scene.height())
        
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0

        self.scale_coeff = 1

    def show_message(self, title, text, font, icon = QtWidgets.QMessageBox.Warning):
        msg = QtWidgets.QMessageBox()
        msg.setGeometry(800, 400, 250, 200)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setFont(QtGui.QFont(font))
        msg.setIcon(icon)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def rotateX(self, x, y, z, teta):
        teta = teta * pi / 180
        buf = y
        y = cos(teta) * y - sin(teta) * z
        z = cos(teta) * z + sin(teta) * buf
        return x, y, z


    def rotateY(self, x, y, z, teta):
        teta = teta * pi / 180
        buf = x
        x = cos(teta) * x - sin(teta) * z
        z = cos(teta) * z + sin(teta) * buf
        return x, y, z


    def rotateZ(self, x, y, z, teta):
        teta = teta * pi / 180
        buf = x
        x = cos(teta) * x - sin(teta) * y
        y = cos(teta) * y + sin(teta) * buf
        return x, y, z

    def transform(self, x, y, z):
        x, y, z = self.rotateX(x, y, z, self.angle_x)
        x, y, z = self.rotateY(x, y, z, self.angle_y)
        x, y, z = self.rotateZ(x, y, z, self.angle_z)
        
        x = x * self.scale_coeff + self.width // 2
        y = y * self.scale_coeff + self.height // 2
        return int(round(x)), int(round(y)), int(round(z))

    def horizon(self, start_x, start_y, end_x, end_y):
        if end_x == start_x:
            if end_x >= self.scene.width():
                return
            self.max_horizon[end_x] = max(self.max_horizon[end_x], end_y)#max(start_y, end_y))
            self.min_horizon[end_x] = min(self.min_horizon[end_x], end_y)#min(start_y, end_y))
        else:
            k = (end_y - start_y) / (end_x - start_x)
            for x in range(start_x, end_x + 1):
                if x >= self.scene.width():
                    break
                y = k * (x - start_x) + start_y
                self.max_horizon[x] = max(self.max_horizon[x], y)
                self.min_horizon[x] = min(self.min_horizon[x], y)
    
    def is_visible(self, x, y):
        x = int(round(x))
        if x < 0 or x >= self.scene.width():
            return 0
        if y < self.max_horizon[x] and y > self.min_horizon[x]:
            return 0
        # print("VISIBILITY")
        if y >= self.max_horizon[x]:
            return 1
        return -1

    def intersection(self, x_start, y_start, x_end, y_end, horizon):
        def sign(a):
            if a < 0:
                return -1
            if a > 0:
                return 1
            return 0
        # print(x_start, y_start, x_end, y_end)
        # print(x_start, horizon[x_start], x_end, horizon[x_end])
        if x_end == x_start:
            if 0 <= x_end < self.scene.width():
                return x_end, horizon[x_end]
            return self.scene.width() - 1, horizon[self.scene.width() - 1]
        
        k = (y_end - y_start) / (x_end - x_start)
        sy = sign(y_start + k - horizon[x_start + 1])
        sc = sy
        y = y_start + k
        x = x_start + 1
        while sc == sy and x < x_end and x < self.scene.width():
            sc = sign(y - horizon[x])
            y += k
            x += 1
        # print("INTER")
        # print(int(round(x)), int(round(y)))
        return int(round(x)), int(round(y))

    def draw(self, x_from, x_to, x_step, z_from, z_to, z_step, f, color):
        z = z_to
        iz = 0
        visible = True
        x_left = -1
        y_left = -1
        x_right = -1
        y_right = -1

        self.min_horizon = [self.height for _ in range(self.width)]
        self.max_horizon = [0 for _ in range(self.width)]

        # self.scale_coeff = self.width / (x_to - x_from)

        while z >= z_from:
            x_last = x_from
            y_last = f(x_from, z)
            z_buf = z
            x_last, y_last, z_buf = self.transform(x_last, y_last, z)
            
            if x_left != -1:
                if self.is_visible(x_left, y_left) and self.is_visible(x_last, y_last):
                    self.scene.addLine(x_last, y_last, x_left, y_left, QPen(color))
                self.horizon(x_last, y_last, x_left, y_left)

            x_left = x_last
            y_left = y_last

            prev_visibility = self.is_visible(x_last, y_last)
            x = x_from
            while x <= x_to:
                y = f(x, z)
                x_curr, y_curr, z_buf = self.transform(x, y, z)
                # print(x_curr, y_curr)
                curr_visibility = self.is_visible(x_curr, y_curr)
                if prev_visibility == curr_visibility:
                    if curr_visibility:
                        # print("ADDLINE", x_last, y_last, x_curr, y_curr)
                        self.scene.addLine(x_last, y_last, x_curr, y_curr, QPen(color))
                        self.horizon(x_last, y_last, x_curr, y_curr)
                    # else:
                    #     print("FQ")
                else:
                    if not curr_visibility:
                        if prev_visibility == 1:
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.max_horizon)
                        else:
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.min_horizon)
                        
                        # print("ADDLINE")
                        self.scene.addLine(x_last, y_last, x_inter, y_inter, QPen(color))
                        self.horizon(x_last, y_last, x_inter, y_inter)
                    elif curr_visibility == 1:
                        if not prev_visibility:
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.max_horizon)
                            # print("ADDLINE") !
                            self.scene.addLine(x_inter, y_inter, x_curr, y_curr, QPen(color))
                            self.horizon(x_inter, y_inter, x_curr, y_curr)
                        else:
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.min_horizon)
                            # print("ADDLINE")
                            self.scene.addLine(x_last, y_last, x_inter, y_inter, QPen(color))
                            self.horizon(x_last, y_last, x_inter, y_inter)
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.max_horizon)
                            # print("ADDLINE")
                            self.scene.addLine(x_inter, y_inter, x_curr, y_curr, QPen(color))
                            self.horizon(x_inter, y_inter, x_curr, y_curr)
                    else:
                        if not prev_visibility:
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.min_horizon)
                            # print("ADDLINE") !
                            self.scene.addLine(x_inter, y_inter, x_curr, y_curr, QPen(color))
                            self.horizon(x_inter, y_inter, x_curr, y_curr)
                        else:
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.max_horizon)
                            # print("ADDLINE")
                            self.scene.addLine(x_last, y_last, x_inter, y_inter, QPen(color))
                            self.horizon(x_last, y_last, x_inter, y_inter)
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.min_horizon)
                            # print("ADDLINE")
                            self.scene.addLine(x_inter, y_inter, x_curr, y_curr, QPen(color))
                            self.horizon(x_inter, y_inter, x_curr, y_curr)
                prev_visibility = curr_visibility
                x_last = x_curr
                y_last = y_curr

                x += x_step

            if x_right != -1:
                self.scene.addLine(x_right, y_right, x_curr, y_curr, QPen(color))
                self.horizon(x_right, y_right, x_curr, y_curr)
            x_right = x_curr
            y_right = y_curr
            z -= z_step
    

    def draw_surface(self):
        try:
            x_from = self.x_from_entry.value()
            x_to = self.x_to_entry.value()
            z_from = self.z_from_entry.value()
            z_to = self.z_to_entry.value()

            x_step = self.x_step_entry.value()
            z_step = self.z_step_entry.value()

            f = self.function()
            color = self.get_color(self.color_box)

            if f == None:
                raise Warning
            if color == None:
                raise TypeError
            if x_from > x_to or z_from > z_to:
                raise IOError

        except Warning:
            self.show_message("Ошибка", "Выберите уравнение поверхности", "Ubuntu 15")
        except TypeError():
            self.show_message("Ошибка", "Выберите цвет построения", "Ubuntu 15")
        except IOError:
            self.show_message("Ошибка", "Нижний предел координат должен быть "
                "меньше/равен верхнего", "Ubuntu 15")
        else:
            self.scene.clear()
            self.draw(x_from, x_to, x_step, z_from, z_to, z_step, f, color)

    def rotation_x(self):
        try:
            angle = self.x_rotate_entry.value()
        except:
            self.show_message("Ошибка", "Выберите цвет построения", "Ubuntu 15")
        else:
            self.angle_x += angle
            self.draw_surface()

    def rotation_y(self):
        try:
            angle = self.y_rotate_entry.value()
        except:
            self.show_message("Ошибка", "Выберите цвет построения", "Ubuntu 15")
        else:
            self.angle_y += angle
            self.draw_surface()

    def rotation_z(self):
        try:
            angle = self.z_rotate_entry.value()
        except:
            self.show_message("Ошибка", "Выберите цвет построения", "Ubuntu 15")
        else:
            self.angle_z += angle
            self.draw_surface()
    
    def scale(self):
        self.scale_coeff = self.scale_entry.value()
        self.draw_surface()

    def clear(self):
        self.scene.clear()
        self.angle_x = self.angle_y = self.angle_z = 0
        self.scale_coeff = 1

    def exit(self):
        sys.exit(0)

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
        return None
    
    def function(self):
        if self.func_box.currentIndex() == 1:
            return f1
        if self.func_box.currentIndex() == 2:
            return f2
        if self.func_box.currentIndex() == 3:
            return f3
        if self.func_box.currentIndex() == 4:
            return f4
        if self.func_box.currentIndex() == 5:
            return f5
        if self.func_box.currentIndex() == 6:
            return f6
        return None

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
