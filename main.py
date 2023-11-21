from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter
from random import randint
from UI import Ui_MainWindow

import sys


class Circle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.draw)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def draw(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        self.xy = randint(50, 400)
        qp.drawEllipse(300, 100, self.xy, self.xy)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
