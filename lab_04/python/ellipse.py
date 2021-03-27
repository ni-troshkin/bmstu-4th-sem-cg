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
        self.points.clear()
        sq_b = self.b * self.b
        sq_a = self.a * self.a
        exc = sq_b / sq_a
        x = 0
        y = self.b
        d = 2 * (1 - self.b)
        end_y = 0
        self.points.append([x, y])
        while (y >= end_y):
            if d < 0:
                d1 = 2 * d + 2 * y - 1
                if d1 <= 0:
                    d += (2 * x + 1) * exc + 2
                    x += 1
                else:
                    d += (2 * x + 1) * exc - 2 * y + 5
                    x += 1
                    y -= 1
            elif d == 0:
                d += (2 * x + 1) * exc - 2 * y + 5
                x += 1
                y -= 1
            else:
                d2 = 2 * d - 2 * x - 1
                if d2 <= 0:
                    d += (2 * x + 1) * exc - 2 * y + 5
                    x += 1
                    y -= 1
                else:
                    y -= 1
                    d += 1 - 2 * y
            self.points.append([x, y])
        self.hor_reflection()
        self.ver_reflection()
        self.move_to_center()

    def create_middledot(self):
        self.points.clear()
        x = 0
        y = self.b

        sq_a = self.a * self.a
        sq_b = self.b * self.b

        f = sq_b - sq_a * self.b + sq_a / 4
        x_border = sq_a / sqrt(sq_a + sq_b)
        y_border = sq_b / sqrt(sq_a + sq_b)

        self.points.append([x, y])
        while y > y_border:
            if f > 0:
                y -= 1
                f -= 2 * sq_a * y
            f += 2 * sq_b * x + sq_b
            x += 1    
            self.points.append([x, y])

        f += 3 / 4 * (sq_a - sq_b) - (sq_b * x + sq_a * y)
        while y >= 0:
            if f < 0:
                x += 1
                f += 2 * sq_b * x
            f += sq_a - 2 * sq_a * y
            y -= 1
            self.points.append([x, y])

        self.hor_reflection()
        self.ver_reflection()
        self.move_to_center()

    def hor_reflection(self):
        length = len(self.points)
        for i in range(length):
            self.points.append([-self.points[i][0], self.points[i][1]])
    
    def ver_reflection(self):
        length = len(self.points)
        for i in range(length):
            self.points.append([self.points[i][0], -self.points[i][1]])
    
    def move_to_center(self):
        for point in self.points:
            point[0] += self.center_x
            point[1] += self.center_y
    
