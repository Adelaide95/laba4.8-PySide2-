#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QAbstractItemView,
)


class MainWindow(QWidget):
    def __init__(self, trp):
        super().__init__()
        self.setWindowTitle("Task 1")
        self.setGeometry(370, 390, 370, 390)
        self.lst1 = QListWidget()
        self.lst1.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lst2 = QListWidget()
        self.lst2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lst1.addItems(trp)
        self.inp1 = QPushButton("Add")
        self.inp2 = QPushButton("Remove")
        self.setting()

    def setting(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        hbox.addWidget(self.lst1)
        hbox.addLayout(vbox)
        vbox.addWidget(self.inp1)
        vbox.addWidget(self.inp2)
        hbox.addWidget(self.lst2)
        self.setLayout(hbox)
        self.inp1.clicked.connect(self.toright)
        self.inp2.clicked.connect(self.toleft)
        self.inp1.setStyleSheet("background: purple")
        self.inp2.setStyleSheet("background: blue")

    def toright(self):
        listItems = self.lst1.selectedItems()
        for item in listItems:
            self.lst1.takeItem(self.lst1.row(item))
            self.lst2.addItem(item)

    def toleft(self):
        listItems = self.lst2.selectedItems()
        for item in listItems:
            self.lst2.takeItem(self.lst2.row(item))
            self.lst1.addItem(item)


def main():
    app = QApplication(sys.argv)
    trp = (
        "Apple",
        "Bananas",
        "Carrot",
        "Butter",
        "Meat",
        "Potato",
        "Pineapple"
    )
    application = MainWindow(trp)
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()