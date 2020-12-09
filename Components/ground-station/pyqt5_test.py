from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
import sys

app = QApplication(sys.argv)
win = QMainWindow()
#win.setGeometry(500, 500, 500, 500)
win.setWindowTitle("Test Window")

#label = QtWidgets.QLabel(win)
#label.setText("GPS COORDINATES TO AREA 51")
#label.adjustSize()
#label.move(0,0)

#~~~~~~~~~~~~~~~~~~~~~~ Counter ~~~~~~~~~~~~~~~~~~~~~~
#count = 0
#def increment_counter():
#    global count
#    label.setText(str(count))
#    count = count + 1

#timer = QTimer()
#timer.timeout.connect(increment_counter)
#timer.start(1000)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~ Images ~~~~~~~~~~~~~~~~~~~~~~~
image_label = QtWidgets.QLabel(win)
image_label
pixmap = QPixmap("test_image.jpg")
image_label.setPixmap(pixmap)
win.resize(pixmap.width(), pixmap.height())
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

win.show()

sys.exit(app.exec_())
