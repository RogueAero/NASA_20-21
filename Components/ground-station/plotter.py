import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt, QTimer, QThread, QRect

class Locator():
    def __init__(self):
        self.x = 41.315917
        self.y = -74.488976
    
    def update(self, x, y):
        # print('updating location:{0}. {1}'.format(x, y))
        self.x = x
        self.y = y

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Coordinate Plotter'
        self.resize(640, 480)

        self.locator = Locator()
        self.coords = QLabel(self)
        self.initStuff()

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateLocation)
        self.timer.start(1000)

    def initStuff(self):
        self.coords.setGeometry(0, 463, 175, 15)
        self.coords.setStyleSheet('background-color: white')

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap('map.png')
        painter.drawPixmap(self.rect(), pixmap)
        painter.end()

        self.drawLocator(self.locator)
        self.show()
    
    def drawLocator(self, locator):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
        painter.drawEllipse(locator.x, locator.y, 3, 3)

    def updateLocation(self):
        self.locator.update(self.locator.x + 0.000001, self.locator.y + 0.000001)
        self.coords.setText('{0:2.10}, {1:2.10}'.format(self.locator.x, self.locator.y))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
