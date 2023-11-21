from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QColor, QPainter
from random import randint

import sys


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
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
        qp.setBrush(QColor(255, 255, 0))
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
