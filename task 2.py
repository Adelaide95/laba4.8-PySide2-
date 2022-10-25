#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QListWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task 2")
        self.setGeometry(270, 290, 270, 290)
        self.lst1 = QListWidget()
        self.lst1.itemDoubleClicked.connect(self.replaceitem)
        self.inp1 = QLineEdit()
        self.inp1.returnPressed.connect(self.replacetxt)
        self.create()

    def create(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.inp1)
        vbox.addWidget(self.lst1)
        self.setLayout(vbox)

    def replacetxt(self):
        self.lst1.addItem(self.inp1.text())
        self.inp1.clear()

    def replaceitem(self):
        listItems = self.lst1.selectedItems()
        if not listItems:
            return None
        for item in listItems:
            self.inp1.setText(item.text())


def main():
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
