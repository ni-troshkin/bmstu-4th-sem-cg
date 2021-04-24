from app_interface import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPen, QBrush

from time import sleep, time
import sys

class Point():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class Line():
    def __init__(self, begin: Point, end: Point):
        self.begin = begin    # точка начала ребра, меньшая ордината
        self.end = end    # точка конца ребра, большая ордината
        if self.begin.y > self.end.y:
            self.begin, self.end = self.end, self.begin
        self.next = None    # ссылка на следующее ребро в списке
        self.dy = abs(self.end.y - self.begin.y)    # количество пересекающих строк
        # расчет приращения абсциссы
        if not self.is_horisontal():
            if self.end.y == self.end.y:
                self.dx = (self.begin.x - self.end.x) / self.dy
            else:
                self.dx = (self.end.x - self.begin.x) / self.dy
        # пересечение с максимальной сканирующей строкой
        self.x = None
    
    # проверка, является ли горизонтальным ребром
    def is_horisontal(self):
        if self.begin.y == self.end.y:
            return True
        return False
    
    # нахождение пересечения с максимальной сканирующей строкой
    def x_intersection_max_str(self):
        delta_x = -0.5 * self.dx
        return self.end.x + delta_x

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.points = []    # массив точек
        self.lines = []    # массив отрезков
        self.start_figure = 0    # начальная точка незамкнутой фигуры
        self.is_closed = True    # замкнута ли фигура

        self.max_y = 0    # максимальная ордината, пересекающая фигуру
        self.min_y = self.scene.sceneRect().height()    # минимальная

        self.exit_btn.clicked.connect(self.exit)
        self.clear_btn.clicked.connect(self.clear)
        self.add_btn.clicked.connect(self.add_point)
        self.close_fig_btn.clicked.connect(self.close_figure)
        self.fill_btn.clicked.connect(self.fill_figure)
        
        self.brush = QBrush(Qt.black)
        self.pen = QPen(Qt.black)

        self.blackpen = QPen(Qt.black)
        self.redpen = QPen(Qt.red)
        self.bluepen = QPen(Qt.blue)
        self.whitepen = QPen(Qt.white)

    # получение пера по выбранному цвету
    def get_pen(self):
        if self.color_box.currentIndex() == 1:
            return self.redpen
        if self.color_box.currentIndex() == 2:
            return self.bluepen
        if self.color_box.currentIndex() == 3:
            return self.blackpen
        if self.color_box.currentIndex() == 4:
            return self.whitepen 

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
            self.add_to_table(x, y)

    def add_to_table(self, x, y):
        self.points.append(Point(x, y))
        # пересчет максимальной и минимальной ординаты
        if y < self.min_y:
            self.min_y = y
        if y > self.max_y:
            self.max_y = y
        
        if self.is_closed:
            # начало новой незамкнутой фигуры
            self.start_figure = len(self.points) - 1
            self.is_closed = False
        else:
            self.scene.addLine(self.points[-2].x, self.points[-2].y, 
                                self.points[-1].x, self.points[-1].y, self.pen)
            self.lines.append(Line(self.points[-2], self.points[-1]))
        
        self.scene.addEllipse(x-2, y-2, 4, 4, self.pen, self.brush)


    # формирование окна с предупреждением с заданным текстом
    def show_warning(self, title, text, font):
        msg = QtWidgets.QMessageBox()
        msg.setGeometry(800, 400, 250, 200)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setFont(QtGui.QFont(font))
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    # формирование окна с информацией с заданным текстом
    def show_info(self, title, text, font):
        msg = QtWidgets.QMessageBox()
        msg.setGeometry(800, 400, 250, 200)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setFont(QtGui.QFont(font))
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    # добавление точки с точными координатами
    def add_point(self):
        try:
            x = int(self.x_entry.text())
            y = int(self.y_entry.text())
        except:
            self.show_warning("Неверные координаты", "Координаты должны "
                "являться вещественными числами", "Ubuntu 15")
        else:
            self.add_to_table(x, y)
    
    def get_not_max_s(self, lines, y):
        ignore_list = []
        i = 0
        lines_end_here = []
        for line in lines:
            if line.end.y == y:
                lines_end_here.append((line, i))
            i += 1
        lines_start_here = []
        i = 0
        for line in lines:
            if line.begin.y == y:
                lines_start_here.append((line, i))
            i += 1
        
        for start_line in lines_start_here:
            for end_line in lines_end_here:
                if start_line[0].begin.x == end_line[0].end.x:
                    ignore_list.append(end_line[1])

        return ignore_list

    # заполнение многоугольника
    def fill_figure(self):
        # проверки на замкнутость и выбор цвета
        if self.color_box.currentIndex() == 0:
            self.show_warning("Ошибка", "Выберите цвет заполнения", "Ubuntu 15")
            return
        if self.is_closed == False:
            self.show_warning("Ошибка", "Есть незамкнутые многоугольники", "Ubuntu 15")
            return
        
        if not self.delay_check.isChecked():
            start = time()
            
        pen = self.get_pen()
        active = []    # САР
        lines = []    # массив, в котором подготовленные данные о ребрах
        # копируем в него основной массив ребер
        for line in self.lines:
            lines.append(Line(line.begin, line.end))

        # массив у-групп
        y_groups = [None for i in range(int(self.max_y - self.min_y + 1))]
        for line in lines:
            if line.is_horisontal():
                continue    # не рассматриваем горизонтальные ребра
            
            line.x = line.x_intersection_max_str()
            if line.x < min(line.begin.x, line.end.x):
                line.x = min(line.begin.x, line.end.x)
            if line.x > max(line.begin.x, line.end.x):
                line.x = max(line.begin.x, line.end.x)

            if y_groups[int(line.end.y - self.min_y)] == None:
                y_groups[int(line.end.y - self.min_y)] = lines.index(line)
            else:
                l = lines[y_groups[int(line.end.y - self.min_y)]]
                while l.next != None:
                    l = lines[l.next]
                l.next = lines.index(line)
        
        # для каждой сканирующей строки
        for i in range(len(y_groups) - 1, -1, -1):
            num_y = self.min_y + i    # фактическое значение у
            ignore = []
            # если соответствующая скан-строка является максимальной
            # для некоторого ребра, добавляем его в САР
            if y_groups[i] != None:
                line = lines[y_groups[i]]
                active.append(line)
                while line.next != None:
                    line = lines[line.next]
                    active.append(line)
                ignore = self.get_not_max_s(active, num_y)
            
            # сортируем абсциссы точек пересечения скан-строки с ребрами
            x_s = []
            i = -1
            for line in active:
                i += 1
                if i in ignore:
                    continue
                x_s.append(line.x)
 
            x_s.sort()
            # берем из отсортированного массива пару абсцисс и заполняем
            # пиксели между ними
            while len(x_s) > 0:
                for i in range(int(round(x_s[0]) - 0.5), int(round(x_s[1]) + 0.5)):
                    self.scene.addLine(i, num_y, i, num_y, pen)
                
                x_s.pop(0)
                x_s.pop(0)
            # для каждого элемента САР делаем необходимые преобразования, чтобы
            # перейти к следующей скан-строке
            for i in range(len(active) - 1, -1, -1):
                active[i].dy -= 1
                if active[i].dy < 0:
                    active.pop(i)
                else:
                    active[i].x += active[i].dx
                    if active[i].x < min(active[i].begin.x, active[i].end.x):
                        active[i].x = min(active[i].begin.x, active[i].end.x)
                    if active[i].x > max(active[i].begin.x, active[i].end.x):
                        active[i].x = max(active[i].begin.x, active[i].end.x)
            # если заполнение с задержкой - обновить сцену
            if self.delay_check.isChecked():
                QtWidgets.QApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        # если заполнение без задержки - вывести сообщение о времени заполнения
        if not self.delay_check.isChecked():
            end = time()
            QtWidgets.QApplication.processEvents(QtCore.QEventLoop.AllEvents)
            self.show_info("Закраска успешно завершена", "Время работы алгоритма: {:.1f} "
                                "секунд".format(end - start), "Ubuntu 15")

    # замыкание многоугольника, соединяем последнюю точку 
    # с первой не входящей в замкнутую фигуру
    def close_figure(self):
        if self.is_closed:
            self.show_warning("Ошибка", "Многоугольник уже замкнут", "Ubuntu 15")
            return
        self.scene.addLine(self.points[-1].x, self.points[-1].y, 
            self.points[self.start_figure].x, self.points[self.start_figure].y)
        self.lines.append(Line(self.points[-1], self.points[self.start_figure]))
        self.is_closed = True

    # очистка экрана
    def clear(self):
        self.scene.clear()
        self.points.clear()
        self.lines.clear()
        self.start_figure = 0
        self.is_closed = True

    def exit(self):
        sys.exit(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
