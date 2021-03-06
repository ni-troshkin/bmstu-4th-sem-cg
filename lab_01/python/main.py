import app_interface, edit_interface, sys
from math import sqrt

from PyQt5 import QtCore, QtGui, QtWidgets

EPS = 1e-7    # точность для сравнения вещественных чисел

class Triangle():
    def __init__(self, a: tuple, b: tuple, c: tuple):
        self.a = a
        self.b = b
        self.c = c
        self.dots = 0
    
    def exists(self):    # проверка существования треугольника
        xab = self.b[0] - self.a[0]    # вычисление координат векторов-сторон
        yab = self.b[1] - self.a[1]
        xbc = self.c[0] - self.b[0]
        ybc = self.c[1] - self.b[1]
        xac = self.c[0] - self.a[0]
        yac = self.c[1] - self.a[1]

        ab = sqrt(xab * xab + yab * yab)    # вычисление длин сторон
        bc = sqrt(xbc * xbc + ybc * ybc)
        ac = sqrt(xac * xac + yac * yac)
    
        if abs(ab + ac - bc) <= EPS or abs(ab + bc - ac) <= EPS \
            or abs(ac + bc - ab) <= EPS:
            return False

        return True

    def define_subtriangles(self):
        # вычисление оснований медиан
        self.ma = ((self.b[0] + self.c[0]) / 2, (self.b[1] + self.c[1]) / 2)
        self.mb = ((self.a[0] + self.c[0]) / 2, (self.a[1] + self.c[1]) / 2)
        self.mc = ((self.a[0] + self.b[0]) / 2, (self.a[1] + self.b[1]) / 2)

        # центр пересечения медиан
        self.m = (self.ma[0] + (self.a[0] - self.ma[0]) / 3, 
            self.ma[1] + (self.a[1] - self.ma[1]) / 3)

        # формирование списка "внутренних" треугольников 
        self.subtriangles = [Triangle(self.a, self.m, self.mc), 
            Triangle(self.mc, self.m, self.b), Triangle(self.b, self.m, self.ma), 
            Triangle(self.ma, self.m, self.c), Triangle(self.c, self.m, self.mb),
            Triangle(self.mb, self.m, self.a)]
    
    def find_in_triangle(self, point: tuple):
        for tr in self.subtriangles:    # нахождение точки во внутреннем треуг-е
            if tr.contains(point):
                tr.dots += 1
                break

    def contains(self, point: tuple):
        xab = self.b[0] - self.a[0]    # вычисление координат векторов-сторон
        yab = self.b[1] - self.a[1]
        xbc = self.c[0] - self.b[0]
        ybc = self.c[1] - self.b[1]
        xac = self.c[0] - self.a[0]
        yac = self.c[1] - self.a[1]

        # вычисление координат векторов из вершин к данной точке
        xam = point[0] - self.a[0]
        yam = point[1] - self.a[1]
        xbm = point[0] - self.b[0]
        ybm = point[1] - self.b[1]
        xcm = point[0] - self.c[0]
        ycm = point[1] - self.c[1]

        zamab = xam*yab - yam*xab    # вычисление векторого произведения
        zbmbc = xbm*ybc - ybm*xbc
        zcmca = xcm*(-yac) + ycm*xac

        if ((zamab > 0) and (zbmbc > 0) and (zcmca > 0)) or \
            ((zamab < 0) and (zbmbc < 0) and (zcmca < 0)):
            return True
        return False

    def factor(self):
        max_dots = max([tr.dots for tr in self.subtriangles])
        min_dots = min([tr.dots for tr in self.subtriangles])
        diff = max_dots - min_dots
        return max_dots, min_dots, diff


class EditWindow(QtWidgets.QMainWindow, edit_interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
            

class Window(QtWidgets.QMainWindow, app_interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Реакции на нажатие кнопок
        self.exit_btn.clicked.connect(self.exit_clicked)
        self.add_btn.clicked.connect(self.add_clicked)
        self.del_btn.clicked.connect(self.del_clicked)
        self.info_btn.clicked.connect(self.info_clicked)
        self.find_btn.clicked.connect(self.find_clicked)
        self.edit_btn.clicked.connect(self.edit_clicked)
        
        # Заводим краски
        self.greenbrush = QtGui.QBrush(QtCore.Qt.darkGreen)
        self.greenpen = QtGui.QPen(QtCore.Qt.darkGreen)

        self.canvas_h = self.scene.height()    # параметры "холста"
        self.canvas_w = self.scene.width()
        self.offset = 20

        self.points = []    # массив реальных точек
        self.pixels = []    # массив экранных точек
        self.objects = []    # массив точек как объектов на экране
        self.labels = []    # массив надписей как объектов на экране
        self.lines = []    # массив линий как объектов на экране

        self.tri_points = []

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

    # пересчет координат из декартовых в экранные с учетом масштаба
    def convert_point(self, i):
        if abs(self.max_x - self.min_x) < EPS:
            new_x = self.canvas_w / 2
        else:
            new_x = self.offset + (self.points[i][0] - self.min_x) / \
                (self.max_x - self.min_x) * (self.canvas_w - 2 * self.offset)
        
        if abs(self.max_y - self.min_y) < EPS:
            new_y = self.canvas_h / 2
        else:
            new_y = self.canvas_h - (self.offset + (self.points[i][1] - 
                self.min_y) / (self.max_y - self.min_y) * (self.canvas_h - 
                2 * self.offset))

        return new_x, new_y

    # добавление точки и подписи на экранный холст
    def add_point(self, x, y, i):
        self.objects[i] = self.scene.addEllipse(x - 3.5, y - 3.5, 7, 7, self.greenpen, 
            self.greenbrush)
        
        label_width = len(self.labels[i].text()) * 6.5 + 10
            
        if x < 100 and y > 30:
            self.labels[i].setPos(x + 15, y - 10)
        elif x > 100 and y < 30:
            self.labels[i].setPos(x - label_width, y + 10)
        elif x > 100 and y > 30:
            self.labels[i].setPos(x - label_width, y - 10)
        else:
            self.labels[i].setPos(x + 15, y + 10)

        self.pixels[i] = (x, y)

    # перерисовка точек в соответствии с текущим масштабом
    def rezoom_canvas(self):
        for i in range(len(self.pixels)):
            self.scene.removeItem(self.objects[i])

            new_x, new_y = self.convert_point(i)
            self.add_point(new_x, new_y, i)

    # обновление максимальных и минимальных координат при изменении списка точек
    def refresh_limits(self):
        if self.points == []:
            self.min_x = self.min_y = self.max_x = self.max_y = None
        else:
            x_s = [self.points[i][0] for i in range(len(self.points))]
            y_s = [self.points[i][1] for i in range(len(self.points))]
            self.min_x = min(x_s)
            self.max_x = max(x_s)
            self.min_y = min(y_s)
            self.max_y = max(y_s)

    # добавление точки
    def add_clicked(self):
        try:
            x = float(self.x_entry.text())
            y = float(self.y_entry.text())
        except:
            self.show_warning("Неверные координаты", "Координаты должны "
                "являться вещественными числами", "Ubuntu 15")

        else:
            # флаг поднимается, если меняются предельные координаты точек
            needs_zooming = False
            if len(self.points) == 0:
                self.max_x = self.min_x = x
                self.max_y = self.min_y = y
            if x > self.max_x:
                self.max_x = x
                needs_zooming = True
            if x < self.min_x:
                self.min_x = x
                needs_zooming = True
            if y > self.max_y:
                self.max_y = y
                needs_zooming = True
            if y < self.min_y:
                self.min_y = y
                needs_zooming = True

            self.points.append((x, y))
            self.dots_table.insertRow(len(self.points) - 1)    # заносим в таблицу
            self.dots_table.setItem(len(self.points) - 1, 0, 
                QtWidgets.QTableWidgetItem(str(len(self.points))))
            self.dots_table.setItem(len(self.points) - 1, 1, 
                QtWidgets.QTableWidgetItem(str(x)))
            self.dots_table.setItem(len(self.points) - 1, 2, 
                QtWidgets.QTableWidgetItem(str(y)))
        
            if needs_zooming:
                self.rezoom_canvas()
                if self.tri_points != []:
                    self.draw_triangle(self.tri_points[0], self.tri_points[1], self.tri_points[2])

            x, y = self.convert_point(-1)
            self.objects.append(None)    # резервируется место в списке точек
            self.pixels.append(None)
            self.labels.append(self.scene.addSimpleText(str(len(self.points)) 
                + '(' + str(self.points[-1][0]) + ', ' + 
                str(self.points[-1][1]) + ')'))
            self.add_point(x, y, -1)

    def exit_clicked(self):
        sys.exit(0)
    
    def info_clicked(self):
        info = QtWidgets.QMessageBox()
        info.setGeometry(800, 400, 250, 200)
        info.setWindowTitle("Информация о программе")

        info.setText("Программа позволяет решить геометрическую задачу на "
            "множестве точек, заданном пользователем\nДля просмотра описания "
            "задачи нажмите на кнопку \"Show Details\".")
        info.setDetailedText("Задача: найти такой треугольник с вершинами в "
            "точках из заданного множества, у которого разность максимального "
            "и минимального количества точек, попавших в каждый из шести "
            "треугольников, образованных пересечением медиан, максимальна.\n\n"
            "(c) Трошкин Николай, ИУ7-46Б")
    
        info.setFont(QtGui.QFont("Ubuntu 14"))
        info.setIcon(QtWidgets.QMessageBox.Information)
        info.setStandardButtons(QtWidgets.QMessageBox.Ok)
        info.exec_()

    # удаление точки с экрана
    def del_clicked(self):
        try:
            num = int(self.del_entry.text())
            if (num < 1 or num >= self.dots_table.rowCount()):
                raise TypeError
        except TypeError:
            self.show_warning("Неверный номер точки", "Точка с таким номером "
                "не найдена", "Ubuntu 15")
        except:
            self.show_warning("Неверный номер точки", "Номер точки должен быть"
                " положительным целым числом", "Ubuntu 15")
        
        else:
            needs_zooming = False
            if abs(self.points[num - 1][0] - self.max_x) < EPS or \
                abs(self.points[num - 1][1] - self.max_y) < EPS:
                needs_zooming = True
            if abs(self.points[num - 1][0] - self.min_x) < EPS or \
                abs(self.points[num - 1][1] - self.min_y) < EPS:
                needs_zooming = True
            
            # удаление точки из таблицы, с экрана, из массивов
            self.scene.removeItem(self.objects[num - 1])
            self.scene.removeItem(self.labels[num - 1])
            for i in range(num, len(self.pixels)):
                self.dots_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i)))
                self.labels[i].setText(str(i) + '(' + str(self.points[i][0]) +
                    ', ' + str(self.points[i][1]) + ')')
            self.dots_table.removeRow(num - 1)
            self.points.pop(num - 1)
            self.pixels.pop(num - 1)
            self.objects.pop(num - 1)
            self.labels.pop(num - 1)
            if num - 1 in self.tri_points:
                self.tri_points.clear()
                self.clear_triangle()
            
            for i in range(len(self.tri_points)):
                if self.tri_points[i] > num - 1:
                    self.tri_points[i] -= 1

            if needs_zooming:
                self.refresh_limits()
                self.rezoom_canvas()
                if self.tri_points != []:
                    self.draw_triangle(*self.tri_points)
                else:
                    self.clear_triangle()

    # текстовый вывод результата 
    def show_result(self, info):
        result = QtWidgets.QMessageBox()
        result.setGeometry(800, 400, 250, 200)
        result.setWindowTitle("Результат")
        result.setFont(QtGui.QFont("Ubuntu 15"))

        result.setText("Искомый треугольник построен на точках {:d}, {:d} и "
            "{:d}\nДля подробностей нажмите на кнопку "
            "\"Show Details\".".format(info[3] + 1, info[4] + 1, info[5] + 1))
        result.setDetailedText("У данного треугольника:\n"
        "Вершины: {:d}({:.2f}, {:.2f}), {:d}({:.2f}, {:.2f}), {:d}({:.2f}, {:.2f})\n"
        "Минимальное число точек во внутреннем треугольнике = {:d}\n"
        "Максимальное число точек во внутреннем треугольнике = {:d}\n"
        "Разница = {:d}".format(info[3] + 1, self.points[info[3]][0], 
        self.points[info[3]][1], info[4] + 1, self.points[info[4]][0], 
        self.points[info[4]][1], info[5] + 1, self.points[info[5]][0], 
        self.points[info[5]][1], info[0], info[1], info[2]))
        
        result.setIcon(QtWidgets.QMessageBox.Information)
        result.setStandardButtons(QtWidgets.QMessageBox.Ok)
        result.exec_()

    # нахождение искомого треугольника
    def find_clicked(self):
        info = tuple()
        triangle = None

        # проверка достаточного количества точек
        if len(self.points) < 3:
            self.show_warning("Недостаточно точек", "Введено недостаточно "
            "точек, чтобы строить на них треугольники", "Ubuntu 15")
            return
        
        # рассматривается каждая тройка вершин
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                for k in range(j + 1, len(self.points)):
                    current = Triangle(self.points[i], self.points[j], 
                        self.points[k])
                    if not current.exists():
                        continue
                    current.define_subtriangles()
                    for point in self.points:
                        current.find_in_triangle(point)
                    max_d, min_d, diff = current.factor()
                    if triangle == None:
                        triangle = current
                        info = (min_d, max_d, diff, i, j, k)
                    elif diff > info[2]:
                        triangle = current
                        info = (min_d, max_d, diff, i, j, k)
        
        if triangle == None:
            self.show_warning("Треугольники не найдены", "На введенном "
            "множестве точек невозможно построить треугольники (точки лежат "
            "на одной прямой)", "Ubuntu 15")
        else:
            self.tri_points = [info[3], info[4], info[5]]
            self.draw_triangle(*self.tri_points)
            self.show_result(info)

    def clear_triangle(self):
        # очистка старого треугольника, если он был на экране
        for line in self.lines:
            self.scene.removeItem(line)
        self.lines.clear()

    def draw_triangle(self, i, j, k):
        self.clear_triangle()

        self.blackpen = QtGui.QPen(QtCore.Qt.black)
        self.blackpen.setWidth(4)
        self.redpen = QtGui.QPen(QtCore.Qt.red)
        self.redpen.setWidth(2)

        # определение треугольника в экранных координатах
        pixel_triangle = Triangle(self.pixels[i], self.pixels[j], self.pixels[k])
        pixel_triangle.define_subtriangles()

        # отрисовка сторон и медиан треугольника
        self.lines.append(self.scene.addLine(pixel_triangle.a[0], pixel_triangle.a[1],
            pixel_triangle.b[0], pixel_triangle.b[1], self.blackpen))
        self.lines.append(self.scene.addLine(pixel_triangle.b[0], pixel_triangle.b[1],
            pixel_triangle.c[0], pixel_triangle.c[1], self.blackpen))
        self.lines.append(self.scene.addLine(pixel_triangle.c[0], pixel_triangle.c[1],
            pixel_triangle.a[0], pixel_triangle.a[1], self.blackpen))
        self.lines.append(self.scene.addLine(pixel_triangle.a[0], pixel_triangle.a[1], 
            pixel_triangle.ma[0], pixel_triangle.ma[1], self.redpen))
        self.lines.append(self.scene.addLine(pixel_triangle.b[0], pixel_triangle.b[1], 
            pixel_triangle.mb[0], pixel_triangle.mb[1], self.redpen))
        self.lines.append(self.scene.addLine(pixel_triangle.c[0], pixel_triangle.c[1], 
            pixel_triangle.mc[0], pixel_triangle.mc[1], self.redpen))

    def edit_clicked(self):
        try:
            self.edit_num = int(self.del_entry.text())
            if (self.edit_num < 1 or self.edit_num >= self.dots_table.rowCount()):
                raise TypeError
        except TypeError:
            self.show_warning("Неверный номер точки", "Точка с таким номером "
                "не найдена", "Ubuntu 15")
        except:
            self.show_warning("Неверный номер точки", "Номер точки должен "
                "быть положительным целым числом", "Ubuntu 15")
        
        else:
            self.form = EditWindow()    # открытие окна для ввода новых коорд.
            self.form.change_btn.clicked.connect(self.change_point)
            self.form.show()

    def change_point(self):
        try:
            new_x = float(self.form.new_x_entry.text())
            new_y = float(self.form.new_y_entry.text())
        except:
            self.show_warning("Неверные координаты", "Координаты должны "
                "являться вещественными числами", "Ubuntu 15")
        
        else:
            i = self.edit_num - 1    # переменные введены для удобства
            x = self.points[i][0]
            y = self.points[i][1]
            needs_zooming = False
            if abs(x - self.max_x) < EPS or abs(x - self.min_x) < EPS or \
                abs(y - self.max_y) < EPS or abs(y - self.min_y) < EPS:
                needs_zooming = True
            
            if new_x > self.max_x or new_x < self.min_x or \
                new_y > self.max_y or new_y < self.min_y:
                needs_zooming = True
            
            # переписываем строки таблицы
            self.dots_table.setItem(self.edit_num - 1, 1, 
                QtWidgets.QTableWidgetItem(str(new_x)))
            self.dots_table.setItem(self.edit_num - 1, 2, 
                QtWidgets.QTableWidgetItem(str(new_y)))

            self.points[i] = (new_x, new_y)
            self.labels[i].setText(str(i + 1) + '(' + str(self.points[i][0]) 
                + ', ' + str(self.points[i][1]) + ')')
            
            if i in self.tri_points:
                self.tri_points.clear()
                self.clear_triangle()

            if needs_zooming:
                self.refresh_limits()
                self.rezoom_canvas()
                if self.tri_points != []:
                    self.draw_triangle(*self.tri_points)
                else:
                    self.clear_triangle()

            else:    # перерисовывается только измененная точка
                self.scene.removeItem(self.objects[i])
                new_x, new_y = self.convert_point(i)
                self.add_point(new_x, new_y, i)

            self.form.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
