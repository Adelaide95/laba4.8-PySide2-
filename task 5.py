#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtCore import QPoint, QPropertyAnimation


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task 5")
        self.setGeometry(200, 200,500,500)
        self.circle = QWidget(self)
        self.circle.setStyleSheet("background-color: green; border-radius: 50%;")
        self.circle.resize(100, 100)
        self.anim = QPropertyAnimation(self.circle, b"pos")
        self.anim.setDuration(1500)

    def mousePressEvent(self, event):
        self.anim.setEndValue(QPoint(event.x() - 25, event.y() - 25))
        self.anim.start()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setObjectName("MainWindow")
    window.setStyleSheet("#MainWindow{background-color:purple}")
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

