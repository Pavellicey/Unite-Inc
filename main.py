import sys
import random
from PyQt5 import uic

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.run)
        self.paint = False

    def run(self):
        self.paint = True
        self.update()

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        tmp = random.randint(100, 500)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(100, 100, tmp, tmp)
        tmp2 = random.randint(100, 500)
        qp.drawEllipse(500, 100, tmp2, tmp2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())