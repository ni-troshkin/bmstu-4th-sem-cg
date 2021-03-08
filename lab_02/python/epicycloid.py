# комментарии
# лэйаут
# линии -> эллипсы
# радиус кривизны и шаг угла
# баг с нулевым масштабированием и центром фигуры

from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPen
from math import cos, sin, sqrt, pi, radians
import numpy as np

EPS = 1e-7

class Epicycloid():
    def __init__(self):
        self.coeff = 3
        self.a = 10
        self.b = self.a * self.coeff

        self.dots = []

        self.center_x = 600
        self.center_y = 440
    
    def x(self, t):
        return (self.a + self.b) * cos(t) - self.a * cos((self.a + self.b) * t / self.a)

    def y(self, t):
        return (self.a + self.b) * sin(t) - self.a * sin((self.a + self.b) * t / self.a)

    def get_step(self, x, y):
        r = sqrt((x - self.center_x) ** 2 + (y - self.center_y) ** 2)
        return 1 / r

    def update_center(self, matrix):
        center = np.array([self.center_x, self.center_y, 1], np.double)
        res = np.matmul(center, matrix)
        self.center_x = res[0]
        self.center_y = res[1]

    def update_dots(self, matrix, scene, pen):
        for i in range(len(self.dots)):
            vector = np.array([self.dots[i][0], self.dots[i][1], 1], np.double)
            res = np.matmul(vector, matrix)
            self.dots[i] = (res[0], res[1])
        self.draw_points(scene, pen)
        self.update_center(matrix)

    def scale(self, scene, pen, cx, cy, kx, ky):
        if abs(kx) < EPS or abs(ky) < EPS:
            copy_dots = self.dots[:]
            cenx = self.center_x
            ceny = self.center_y
        matrix = np.array([[kx, 0, 0], [0, ky, 0], [cx * (1 - kx), cy * (1 - ky), 1]], np.double)
        self.update_dots(matrix, scene, pen)
        if abs(kx) < EPS or abs(ky) < EPS:
            self.dots = copy_dots[:]
            self.center_x = cenx
            self.center_y = ceny
        
    def rotate(self, scene, pen, cx, cy, fi):
        fi = radians(fi)
        matrix = np.array([
            [cos(fi), -sin(fi), 0], 
            [sin(fi), cos(fi), 0], 
            [cx * (1 - cos(fi)) - cy * sin(fi), cy * (1 - cos(fi)) + cx * sin(fi), 1]], 
            np.double)
        self.update_dots(matrix, scene, pen)
    
    def move(self, scene, pen, dx, dy):
        matrix = np.array([[1, 0, 0], [0, 1, 0], [dx, dy, 1]], np.double)
        self.update_dots(matrix, scene, pen)

    def draw_points(self, scene, pen):
        scene.clear()
        for i in range(len(self.dots) - 1):
            scene.addLine(self.dots[i][0], self.dots[i][1], 
                self.dots[i+1][0], self.dots[i+1][1], pen)

    def draw_init(self, scene: QGraphicsScene, pen: QPen):
        t = 0.0
        self.dots.clear()
        x = self.x(t) + self.center_x
        y = self.y(t) + self.center_y
        self.dots.append((x, y))

        while t < 2 * pi:
            step = self.get_step(x, y)
            t += step
            new_x = self.x(t) + self.center_x
            new_y = self.y(t) + self.center_y
            
            scene.addLine(x, y, new_x, new_y, pen)
            x, y = new_x, new_y
            self.dots.append((x, y))
