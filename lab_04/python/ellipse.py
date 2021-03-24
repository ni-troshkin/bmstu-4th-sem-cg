from PyQt5.QtWidgets import QGraphicsScene, QGraphicsEllipseItem
from PyQt5.QtGui import QPen, QBrush

from math import sqrt, sin, cos, pi

class Ellipse():
    def __init__(self, cx, cy, a, b):
        self.center_x = cx
        self.center_y = cy

        self.a = a
        self.b = b

        self.points = []
    
    def generate(self, alg, scene, pen, brush):
        if alg == 1:
            self.create_lib()
            self.draw_lib(scene, pen, brush)
        elif alg == 2:
            self.create_canon()
            self.draw_points(scene, pen)
        elif alg == 3:
            self.create_param()
            self.draw_points(scene, pen)
        elif alg == 4:
            self.create_bresenham()
            self.draw_points(scene, pen)
        elif alg == 5:
            self.create_middledot()
            self.draw_points(scene, pen)

    def draw_lib(self, scene: QGraphicsScene, pen, brush):
        scene.addEllipse(self.center_x - self.a, self.center_y - self.b, 
            2 * self.a, 2 * self.b, pen, brush)
    
    def draw_points(self, scene, pen):
        for point in self.points:
            scene.addLine(point[0], point[1], point[0], point[1], pen)
    
    def create_lib(self):
        return QGraphicsEllipseItem(self.center_x - self.a, 
            self.center_y - self.b, 2 * self.a, 2 * self.b)

    def create_canon(self):
        self.points.clear()
        x = -self.a
        for i in range(2 * int(self.a) + 1):
            y = sqrt(self.a * self.a - x * x) * self.b / self.a
            self.points.append([x + self.center_x, y + self.center_y])
            y *= -1
            self.points.append([x + self.center_x, y + self.center_y])
            x += 1
    
    def create_param(self):
        self.points.clear()
        step = 1 / max(self.a, self.b)
        t = 0
        while t <= 2 * pi:
            x = self.a * cos(t) + self.center_x
            y = self.b * sin(t) + self.center_y
            self.points.append([x, y])
            t += step
    
    def create_bresenham(self):
        pass

    def create_middledot(self):
        pass
