import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt, QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Coordinate Plotter'
        self.resize(640, 480)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap('map.png')

        painter.drawPixmap(self.rect(), pixmap)
        painter.setPen(QPen(Qt.red, 1))
        painter.drawEllipse(self.width // 2, self.height // 2, 5, 5)

class Shape():
    def __init__(self, length, position, color, parent=None):
        self.color = color
        self.position = position
        self.color = color

    def paint(self, painter):
        pass

class Circle(Shape):
    def paint(self, painter):
        if not painter.isActive():
            return
        painter.save()
        painter.setPen(QPen(self.color, 4, Qt.SolidLine))
        x, y = self.position.x(), self.position.y()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
