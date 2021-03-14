from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPen, QBrush
from math import cos, sin, sqrt, pi, radians
import numpy as np

EPS = 1e-7

class Rectangle():
    def __init__(self):
        self.h_width = 250
        self.h_height = 200

        self.dots = []    # массив точек, через которые проходит кривая

        self.center_x = 600    # задание начального центра фигуры на экране
        self.center_y = 440
    
    def draw_init(self, scene: QGraphicsScene, pen: QPen):
        # первоначальная отрисовка фигуры на экране, заполнение массива точек
        self.dots.clear()
        
        self.dots.append(np.array([self.center_x - self.h_width, 
            self.center_y - self.h_height, 1], np.double))
        self.dots.append(np.array([self.center_x - self.h_width, 
            self.center_y + self.h_height, 1], np.double))
        self.dots.append(np.array([self.center_x + self.h_width, 
            self.center_y + self.h_height, 1], np.double))
        self.dots.append(np.array([self.center_x + self.h_width, 
            self.center_y - self.h_height, 1], np.double))

        self.draw_points(scene, pen)

    def draw_points(self, scene, pen):
        # рисование фигуры по точкам
        for i in range(len(self.dots) - 1):
            scene.addLine(self.dots[i][0], self.dots[i][1], 
                self.dots[i+1][0], self.dots[i+1][1], pen)
        scene.addLine(self.dots[-1][0], self.dots[-1][1],
            self.dots[0][0], self.dots[0][1], pen)

    def update_center(self, matrix):
        # пересчет координат центра по матрице преобразования
        center = np.array([self.center_x, self.center_y, 1], np.double)
        res = np.matmul(center, matrix)
        self.center_x = res[0]
        self.center_y = res[1]

    def update_dots(self, matrix, scene, pen):
        # пересчет и отрисовка точек преобразованной фигуры
        for i in range(len(self.dots)):
            self.dots[i] = np.matmul(self.dots[i], matrix)
        self.draw_points(scene, pen)
        self.update_center(matrix)

    def scale(self, scene, pen, cx, cy, kx, ky):
        # сохраняем точки для восстановления фигуры после нулевого масштабирования
        cenx, ceny = None, None
        if abs(kx) < EPS or abs(ky) < EPS:
            copy_dots = self.dots[:]
            cenx = self.center_x
            ceny = self.center_y
        matrix = np.array([
            [kx, 0, 0], 
            [0, ky, 0], 
            [cx * (1 - kx), cy * (1 - ky), 1]], np.double)
        self.update_dots(matrix, scene, pen)
        if abs(kx) < EPS or abs(ky) < EPS:
            self.dots = copy_dots[:]
            self.center_x, cenx = cenx, self.center_x
            self.center_y, ceny = ceny, self.center_y
        return cenx, ceny
        
    def rotate(self, scene, pen, cx, cy, fi):
        fi = radians(fi)
        matrix = np.array([
            [cos(fi), -sin(fi), 0], 
            [sin(fi), cos(fi), 0], 
            [cx * (1 - cos(fi)) - cy * sin(fi), 
                cy * (1 - cos(fi)) + cx * sin(fi), 1]], 
            np.double)
        self.update_dots(matrix, scene, pen)
    
    def move(self, scene, pen, dx, dy):
        matrix = np.array([[1, 0, 0], [0, 1, 0], [dx, dy, 1]], np.double)
        self.update_dots(matrix, scene, pen)
