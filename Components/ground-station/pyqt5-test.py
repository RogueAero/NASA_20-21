import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow (QMainWindow):
    counter = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(800,600)
        self.setWindowTitle("Ground Station")
        self.l1 = QLabel(self)
        
        self.label2 = QLabel(self)
        pixmap = QPixmap('test_image.jpg')
        smaller_pm = pixmap.scaled(400, 300, Qt.KeepAspectRatio)
        self.label2.setPixmap(smaller_pm)
        self.setCentralWidget(self.label2)

        self.timer = QTimer()
        self.timer.timeout.connect(self.incCounter)
        self.timer.start(1000)

    def incCounter(self):
        self.l1.setText(str(self.counter))
        self.counter += 1

def main ():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()