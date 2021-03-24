from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QPen

from math import trunc

EPS = 1e-7

def sign(a):
    if (a < 0):
        return -1
    if (a > 0):
        return 1
    return 0

def get_color_with_intesity(color, intensity):    # интенсивность = 0 - альфа-канал 0 - прозрачно
    color.setAlpha(255 * intensity)
    return color

def lib_line(start_x, start_y, end_x, end_y):    # библиотечная функция создания отрезка
    return QtWidgets.QGraphicsLineItem(start_x, start_y, end_x, end_y)

# цифровой дифференциальный анализатор
def dda(start_x, start_y, end_x, end_y):
    points = []

    if abs(end_x - start_x) < 0.5 and abs(end_y - start_y) < 0.5:
        points.append([round(start_x), round(start_y), 1])
        return points, 0
    
    x = start_x
    y = start_y
    l = abs(end_x - start_x) if abs(end_x - start_x) >= abs(end_y - start_y) else abs(end_y - start_y)

    dx = (end_x - start_x) / l
    dy = (end_y - start_y) / l

    i = 0
    steps = 0

    x_step = False
    if abs(dx) == 1:
        x_step = True

    while i <= l:
        points.append([round(x), round(y), 1])
        if x_step and i + 1 <= l:
            if round(y + dy) != round(y):
                steps += 1
        elif i + 1 <= l:
            if round(x + dx) != round(x):
                steps += 1
        x += dx
        y += dy
        i += 1
    
    return points, steps

def bresenham(start_x: int, start_y: int, end_x: int, end_y: int):
    points = []

    if abs(end_x - start_x) < 0.5 and abs(end_y - start_y) < 0.5:
        points.append([start_x, start_y, 1])
        return points, 0
        
    x = start_x
    y = start_y

    dx = abs(end_x - start_x)
    dy = abs(end_y - start_y)

    signx = sign(end_x - start_x)
    signy = sign(end_y - start_y)

    if dy <= dx: # горизонтальный наклон
        change = 0
    else:
        change = 1    # вертикальный наклон
        dx, dy = dy, dx

    m = dy / dx
    error = m - 0.5

    steps = 0
    for i in range(int(dx) + 1):
        points.append([x, y, 1])
        if error >= 0:
            if change == 1:
                x += signx
            else:
                y += signy
            error -= 1
            steps += 1
    
        if error < 0:
            if change == 1:
                y += signy
            else:
                x += signx
            error += m

    return points, steps

def int_bresenham(start_x: int, start_y: int, end_x: int, end_y: int):
    points = []

    if abs(end_x - start_x) < 0.5 and abs(end_y - start_y) < 0.5:
        points.append([start_x, start_y, 1])
        return points, 0
    x = start_x
    y = start_y

    dx = abs(end_x - start_x)
    dy = abs(end_y - start_y)

    signx = sign(end_x - start_x)
    signy = sign(end_y - start_y)

    if dy <= dx: # горизонтальный наклон
        change = 0
    else:
        change = 1    # вертикальный наклон
        dx, dy = dy, dx

    error = 2 * dy - dx

    steps = 0
    for i in range(int(dx) + 1):
        points.append([x, y, 1])
        if error >= 0:
            if change == 1:
                x += signx
            else:
                y += signy
            error -= 2 * dx
            steps += 1
    
        if error < 0:
            if change == 1:
                y += signy
            else:
                x += signx
            error += 2 * dy

    return points, steps

def antialiased_bresenham(start_x: int, start_y: int, end_x: int, end_y: int):
    points = []

    if abs(end_x - start_x) < 0.5 and abs(end_y - start_y) < 0.5:
        points.append([start_x, start_y, 1])
        return points, 0
    
    x = start_x
    y = start_y

    dx = abs(end_x - start_x)
    dy = abs(end_y - start_y)

    signx = sign(end_x - start_x)
    signy = sign(end_y - start_y)

    if dy <= dx: # горизонтальный наклон
        change = 0
    else:
        change = 1    # вертикальный наклон
        dx, dy = dy, dx

    m = dy/dx
    error = 0.5
    w = 1 - m

    steps = 0
    for i in range(int(dx)):
        points.append([x, y, 1 - error])
        if error >= w:
            if change == 1:
                x += signx
            else:
                y += signy
            error -= 1
            steps += 1

        if error < w:
            if change == 1:
                y += signy
            else:
                x += signx
            error += m
            
    points.append([x, y, 1 - error])

    return points, steps

def wu(start_x, start_y, end_x, end_y):
    points = []

    if abs(end_x - start_x) < 0.5 and abs(end_y - start_y) < 0.5:
        points.append([start_x, start_y, 1])
        return points, 0

    x = int(start_x)
    y = int(start_y)

    dx = abs(end_x - start_x)
    dy = abs(end_y - start_y)

    signx = sign(end_x - start_x)
    signy = sign(end_y - start_y)

    if dy <= dx: # горизонтальный наклон
        change = 0
    else:
        change = 1    # вертикальный наклон
        dx, dy = dy, dx

    steps = 0
    if change == 0:
        frac_y = y - trunc(y)
        for i in range(int(dx)):
            points.append([x, trunc(y), 1 - frac_y])
            points.append([x, trunc(y) + 1, frac_y])
            
            x += signx
            new_y = y + signy * dy / dx / signx

            if trunc(y) != trunc(new_y):
                steps += 1
            y = new_y
            frac_y = y - trunc(y)

        points.append([x, trunc(y), 1 - frac_y])
        points.append([x, trunc(y) + 1, frac_y])

    else:
        frac_x = x - trunc(x)
        for i in range(int(dx)):
            points.append([trunc(x), y, 1 - frac_x])
            points.append([trunc(x) + 1, y, frac_x])

            y += signy
            new_x = x + signx * dy / dx / signy

            if trunc(x) != trunc(new_x):
                steps += 1
            x = new_x
            frac_x = x - trunc(x)
        
        points.append([trunc(x), y, 1 - frac_x])
        points.append([trunc(x) + 1, y, frac_x])

    return points, steps
