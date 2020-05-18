import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication,QMainWindow)
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # hbox = QHBoxLayout(self)
        # pixmap = QPixmap("486.png")
        #
        # lbl = QLabel(self)
        # lbl.setPixmap(pixmap)
        #
        # hbox.addWidget(lbl)
        # self.setLayout(hbox)

        # self.move(300, 200)
        #
        # self.setWindowTitle('Red Rock')
        Example=QMainWindow()
        Example.setObjectName("MainWindow")
        Example.setStyleSheet("#MainWindow{border-image:url(486.jpg);}")

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())