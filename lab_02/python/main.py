import app_interface, sys
from epicycloid import Epicycloid
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPen, QBrush 

EPS = 1e-7

class Window(QtWidgets.QMainWindow, app_interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.exit_btn.clicked.connect(self.exit)
        self.move_btn.clicked.connect(self.move_wrapper)
        self.scale_btn.clicked.connect(self.scale_wrapper)
        self.rotate_btn.clicked.connect(self.rotate_wrapper)
        self.back_btn.clicked.connect(self.back)
        self.origin_btn.clicked.connect(self.origin)
        self.info_btn.clicked.connect(self.show_info)

        self.pen = QPen(Qt.darkGreen)
        self.pen.setWidth(3)

        self.figure = Epicycloid()
        self.figure.draw_init(self.scene, self.pen)
        self.update_center()

        self.last = {"trans": "", "x": 0, "y": 0, "cx": 0, "cy": 0, "angle": 0}

    def show_info(self):
        info = QtWidgets.QMessageBox()
        info.setGeometry(800, 400, 250, 200)
        info.setWindowTitle("Информация о программе")

        info.setText("Программа позволяет осуществлять преобразования над "
            "плоской геометрической фигурой (эпициклоидой) - перенос, масштабирование, поворот.")
    
        info.setFont(QtGui.QFont("Ubuntu 15"))
        info.setIcon(QtWidgets.QMessageBox.Information)
        info.setStandardButtons(QtWidgets.QMessageBox.Ok)
        info.exec_()

    def show_warning(self, title, text, font):
        msg = QtWidgets.QMessageBox()
        msg.setGeometry(800, 400, 250, 200)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setFont(QtGui.QFont(font))
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def update_center(self):
        self.label_center.setText("Центр фигуры С({:.2f}, "
                "{:.2f})".format(self.figure.center_x, self.figure.center_y))

    def scale_wrapper(self):
        try:
            cx = float(self.entry_cx.text())
            cy = float(self.entry_cy.text())
            kx = float(self.entry_kx.text())
            ky = float(self.entry_ky.text())
        
        except:
            self.show_warning("Неверные параметры", "Координаты и коэффициенты масштабирования должны "
                "являться вещественными числами", "Ubuntu 15")
        else:
            self.last['trans'] = 'scale'
            self.last['cx'] = cx
            self.last['cy'] = cy
            if abs(kx) < EPS or abs(ky) < EPS:
                self.last['x'] = self.last['y'] = None
            else:
                self.last['x'] = kx
                self.last['y'] = ky
            self.figure.scale(self.scene, self.pen, cx, cy, kx, ky)
            self.update_center()

    def rotate_wrapper(self):
        try:
            cx = float(self.entry_cx.text())
            cy = float(self.entry_cy.text())
            deg = float(self.entry_angle.text())
        
        except:
            self.show_warning("Неверные параметры", "Координаты и угол должны "
                "являться вещественными числами", "Ubuntu 15")
        else:
            self.last['trans'] = 'rotate'
            self.last['cx'] = cx
            self.last['cy'] = cy
            self.last['angle'] = deg
            self.figure.rotate(self.scene, self.pen, cx, cy, deg)
            self.update_center()

    def move_wrapper(self):
        try:
            dx = float(self.entry_dx.text())
            dy = float(self.entry_dy.text())
        except:
            self.show_warning("Неверное смещение", "Координаты должны "
                "являться вещественными числами", "Ubuntu 15")
        else:
            self.last['trans'] = 'move'
            self.last['x'] = dx
            self.last['y'] = dy
            self.figure.move(self.scene, self.pen, dx, dy)
            self.update_center()

    def back(self):
        if self.last["trans"] == "":
            self.show_warning("Невозможно вернуться", "Не сделано ни одного "
            "преобразования или возврат был в предыдущем действии", "Ubuntu 15")
        
        if self.last["trans"] == 'move':
            self.figure.move(self.scene, self.pen, -(self.last["x"]), -(self.last["y"]))
            self.update_center()
        elif self.last["trans"] == 'scale':
            if self.last['x'] == None:
                self.figure.draw_points(self.scene, self.pen)
            else:
                self.figure.scale(self.scene, self.pen, self.last["cx"], self.last["cy"], 
                    1 / self.last["x"], 1 / self.last["y"])
                self.update_center()
        elif self.last["trans"] == 'rotate':
            self.figure.rotate(self.scene, self.pen, self.last["cx"], self.last["cy"], -(self.last["angle"]))
            self.update_center()
            
        self.last["trans"] = ""

    def origin(self):
        del self.figure
        self.figure = Epicycloid()
        self.scene.clear()
        self.figure.draw_init(self.scene, self.pen)
        self.update_center()

    def exit(self):
        sys.exit(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
