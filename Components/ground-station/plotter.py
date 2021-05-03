import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt, QTimer, QThread, QRect

WIDTH = 640
HEIGHT = 480

class Locator():
    def __init__(self):
        self.x = 41.325917
        self.y = -74.489999
    
    def update(self, x, y):
        # print('updating location:{0}. {1}'.format(x, y))
        self.x = x
        self.y = y

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Coordinate Plotter'
        self.resize(WIDTH, HEIGHT)

        self.locator = Locator()
        self.coords = QLabel(self)
        self.initStuff()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(0.0001)

    def initStuff(self):
        self.coords.setGeometry(0, 463, 175, 15)
        self.coords.setStyleSheet('background-color: white')

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap('map.png')
        painter.drawPixmap(self.rect(), pixmap)
        painter.end()

        self.updateLocation()
        self.drawLocator(self.locator)
        self.show()
    
    def drawLocator(self, locator):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.cyan, 3, Qt.SolidLine))
        scaled_x, scaled_y = self.translateLoc(locator.x, locator.y)
        painter.drawEllipse(scaled_x, scaled_y, 3, 3)

    def translateLoc(self, x, y):
        # (0,0) for map is (41.315917, -74.490298)
        # (WIDHT,HEIGHT) for map is (41.334287, -74.490298)

        scaled_x = int(WIDTH * (41.334287 - x) // 0.01837)
        scaled_y = int(HEIGHT * (74.490298 - abs(y)) // 0.001322)
        return scaled_x, scaled_y

    def updateLocation(self):
        self.locator.update(self.locator.x + 0.000001, self.locator.y + 0.000001)
        self.coords.setText('{0:2.10}, {1:2.10}'.format(self.locator.x, self.locator.y))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
