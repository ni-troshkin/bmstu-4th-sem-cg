from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsScene

def lib_line(scene: QGraphicsScene, start_x, start_y, end_x, end_y, pen):
    scene.addLine(start_x, start_y, end_x, end_y, pen)

def dda(scene: QGraphicsScene, start_x, start_y, end_x, end_y, pen):
    x = start_x
    y = start_y
    l = abs(end_x - start_x) if abs(end_x - start_x) >= abs(end_y - start_y) else abs(end_y - start_y)

    dx = (end_x - start_x) / l
    dy = (end_y - start_y) / l

    for i in range(int(l)):
        scene.addLine(x, y, x, y, pen)
        x += dx
        y += dy

def bresenham(scene: QGraphicsScene, start_x, start_y, end_x, end_y, pen):
    pass

def int_bresenham(scene: QGraphicsScene, start_x, start_y, end_x, end_y, pen):
    pass

def opt_bresenham(scene: QGraphicsScene, start_x, start_y, end_x, end_y, pen):
    pass

def wu(scene: QGraphicsScene, start_x, start_y, end_x, end_y, pen):
    pass
