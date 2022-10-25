#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QPainter, QBrush, QPen, QPolygon, QPainterPath
from PySide2.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task 4")
        self.setGeometry(150, 50, 600, 550)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.darkMagenta))
        painter.drawRect(0, 0, 600, 500)
        painter.setPen(QPen(Qt.darkMagenta))
        painter.setBrush(QBrush(Qt.darkMagenta))
        painter.drawRect(0, 420, 600, 130)
        painter.setPen(Qt.darkMagenta)
        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(Qt.gray)
        points_Cat1 = QPolygon([
        QPoint(62, 400),
        QPoint(59, 408),
        QPoint(61, 419),
        QPoint(64, 428),
        QPoint(70, 439),
        QPoint(82, 449),
        QPoint(95, 460),
        QPoint(104, 464),
        QPoint(120, 469),
        QPoint(136, 471),
        QPoint(151, 471),
        QPoint(167, 470),
        QPoint(162, 459),
        QPoint(156, 445),
        QPoint(158, 451),
        QPoint(146, 445),
        QPoint(138, 443),
        QPoint(129, 441),
        QPoint(119, 437),
        QPoint(113, 433),
        QPoint(107, 430),
        QPoint(95, 421),
        QPoint(88, 413),
        QPoint(83, 408),
        QPoint(76, 401),
        QPoint(69, 399),
        QPoint(63, 399)
        ])

        points_Cat2 = QPolygon([
            QPoint(227, 509),
            QPoint(226, 522),
            QPoint(229, 535),
            QPoint(236, 542),
            QPoint(246, 543),
            QPoint(253, 532),
            QPoint(253, 515),
            QPoint(242, 513),
            QPoint(228, 510)
        ])

        points_Cat3 = QPolygon([
            QPoint(404, 514),
            QPoint(403, 525),
            QPoint(407, 535),
            QPoint(417, 539),
            QPoint(425, 536),
            QPoint(430, 529),
            QPoint(430, 514),
            QPoint(426, 507),
            QPoint(417, 510),
            QPoint(403, 513)
        ])

        points_Cat = QPolygon([
            QPoint(154, 437),
            QPoint(151, 414),
            QPoint(150, 400),
            QPoint(151, 379),
            QPoint(151, 394),
            QPoint(151, 381),
            QPoint(151, 372),
            QPoint(152, 352),
            QPoint(155, 343),
            QPoint(155, 337),
            QPoint(159, 320),
            QPoint(160, 315),
            QPoint(162, 305),
            QPoint(164, 300),
            QPoint(167, 288),
            QPoint(172, 271),
            QPoint(177, 255),
            QPoint(181, 240),
            QPoint(188, 221),
            QPoint(193, 200),
            QPoint(197, 188),
            QPoint(200, 170),
            QPoint(209, 145),
            QPoint(215, 124),
            QPoint(222, 106),
            QPoint(230, 91),
            QPoint(233, 84),
            QPoint(239, 75),
            QPoint(246, 65),
            QPoint(249, 62),
            QPoint(253, 60),
            QPoint(260, 64),
            QPoint(265, 69),
            QPoint(271, 76),
            QPoint(275, 80),
            QPoint(279, 88),
            QPoint(288, 100),
            QPoint(292, 106),
            QPoint(302, 107),
            QPoint(338, 104),
            QPoint(343, 104),
            QPoint(350, 96),
            QPoint(359, 82),
            QPoint(366, 72),
            QPoint(379, 59),
            QPoint(387, 63),
            QPoint(396, 73),
            QPoint(408, 93),
            QPoint(416, 108),
            QPoint(425, 127),
            QPoint(436, 146),
            QPoint(441, 156),
            QPoint(445, 165),
            QPoint(452, 179),
            QPoint(457, 192),
            QPoint(463, 208),
            QPoint(466, 217),
            QPoint(469, 229),
            QPoint(478, 248),
            QPoint(485, 279),
            QPoint(488, 297),
            QPoint(494, 327),
            QPoint(495, 339),
            QPoint(497, 346),
            QPoint(499, 368),
            QPoint(499, 383),
            QPoint(500, 391),
            QPoint(498, 423),
            QPoint(496, 439),
            QPoint(492, 453),
            QPoint(486, 466),
            QPoint(478, 478),
            QPoint(467, 489),
            QPoint(451, 498),
            QPoint(437, 504),
            QPoint(418, 510),
            QPoint(398, 514),
            QPoint(380, 517),
            QPoint(360, 520),
            QPoint(336, 521),
            QPoint(309, 521),
            QPoint(282, 519),
            QPoint(259, 517),
            QPoint(239, 512),
            QPoint(216, 505),
            QPoint(194, 494),
            QPoint(176, 480),
            QPoint(168, 471)
        ])
        painter.drawPolygon(points_Cat)
        painter.drawPolygon(points_Cat1)
        painter.drawPolygon(points_Cat2)
        painter.drawPolygon(points_Cat3)
        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        painter.drawEllipse(274, 166, 21, 21)
        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        painter.drawEllipse(382, 164, 20, 20)
        painter.setPen(Qt.black)
        painter.setBrush(Qt.red)
        points_Cat4 = QPolygon([
            QPoint(317, 177),
            QPoint(318, 186),
            QPoint(320, 189),
            QPoint(323, 194),
            QPoint(323, 194),
            QPoint(330, 194),
            QPoint(337, 194),
            QPoint(342, 188),
            QPoint(342, 174),
            QPoint(339, 173),
            QPoint(334, 170),
            QPoint(329, 165),
            QPoint(326, 169),
            QPoint(323, 171),
            QPoint(320, 174),
            QPoint(317, 175)
        ])

        painter.drawPolygon(points_Cat4)

        painter.setBrush(QBrush(Qt.darkGray, Qt.SolidPattern))
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        points_Cat5 = QPolygon([
            QPoint(65, 430),
            QPoint(67, 418),
            QPoint(82, 408),
            QPoint(88, 413),
            QPoint(93, 419),
            QPoint(82, 427),
            QPoint(77, 443),
            QPoint(68, 436)
        ])
        painter.drawPolygon(points_Cat5)

        painter.setBrush(QBrush(Qt.darkGray, Qt.SolidPattern))
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        points_Cat6 = QPolygon([
            QPoint(91, 455),
            QPoint(92, 440),
            QPoint(105, 430),
            QPoint(111, 432),
            QPoint(118, 437),
            QPoint(109, 449),
            QPoint(109, 464),
            QPoint(98, 461)
        ])
        painter.drawPolygon(points_Cat6)

        painter.setBrush(QBrush(Qt.darkGray, Qt.SolidPattern))
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        points_Cat7 = QPolygon([
            QPoint(127, 470),
            QPoint(122, 457),
            QPoint(128, 441),
            QPoint(138, 443),
            QPoint(146, 444),
            QPoint(143, 457),
            QPoint(152, 471),
            QPoint(137, 471)
        ])
        painter.drawPolygon(points_Cat7)


        painter.setPen(Qt.black)
        painter.setBrush(Qt.black)
        path = QPainterPath()
        path.moveTo(231, 136)
        path.cubicTo(216, 123, 197, 113, 148, 108)
        path2 = QPainterPath()
        path2.moveTo(228, 172)
        path2.cubicTo(210, 162, 195, 159, 140, 160)
        path3 = QPainterPath()
        path3.moveTo(409, 158)
        path3.cubicTo(431, 138, 455, 123, 501, 107)
        path4 = QPainterPath()
        path4.moveTo(423, 179)
        path4.cubicTo(448, 171, 471, 167, 511, 166)
        painter.drawPath(path)
        painter.drawPath(path2)
        painter.drawPath(path3)
        painter.drawPath(path4)
        painter.setBrush(Qt.gray)
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        path5 = QPainterPath()
        path5.moveTo(260, 271)
        path5.cubicTo(305, 278, 283, 292, 265, 293)
        path6 = QPainterPath()
        path6.moveTo(412, 269)
        path6.cubicTo(448, 273, 439, 284, 414, 286)
        painter.drawPath(path5)
        painter.drawPath(path6)
        painter.setPen(Qt.black)
        painter.setBrush(Qt.red)
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        path7 = QPainterPath()
        path7.moveTo(308, 175)
        path7.cubicTo(323, 174, 325, 172, 329, 158)
        path8 = QPainterPath()
        path8.moveTo(327, 164)
        path8.cubicTo(335, 171, 342, 174, 350, 174)
        path9 = QPainterPath()
        path9.moveTo(306, 107,)
        path9.cubicTo(308, 115, 308, 118, 309, 122)

        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        path10 = QPainterPath()
        path10.moveTo(321, 106)
        path10.cubicTo(322, 114, 322, 118,324, 125)
        path11 = QPainterPath()
        path11.moveTo(339, 103)
        path11.cubicTo(340, 112, 340, 118, 341, 120)
        painter.drawPath(path9)
        painter.drawPath(path10)
        painter.drawPath(path11)

        painter.setBrush(QBrush(Qt.darkGray, Qt.SolidPattern))
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        path12 = QPainterPath()
        path12.moveTo(176, 256)
        path12.cubicTo(192, 265, 194, 277, 168, 285)
        path13 = QPainterPath()
        path13.moveTo(157, 336)
        path13.cubicTo(174, 341, 179, 357, 152, 367)
        painter.drawPath(path12)
        painter.drawPath(path13)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
