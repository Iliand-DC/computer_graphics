from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Grid:
    """ create grid on scene
    """
    GRID_MARGIN = 10
    def __init__(self, scene) -> None:
        self.scene = scene
        self.create_grid()

    def create_grid(self) -> None:
        i = self.scene.left
        while i <= self.scene.right:
            line = QGraphicsLineItem(i, self.scene.top, 
                                     i, self.scene.bottom)

            line.setPen(QPen(QColor("#111111")))
            self.scene.addItem(line)
            i += self.GRID_MARGIN

        i = self.scene.top
        while i <= self.scene.bottom:
            line = QGraphicsLineItem(self.scene.left, i, 
                                     self.scene.right, i)

            line.setPen(QPen(QColor("#111111")))
            self.scene.addItem(line)
            i += self.GRID_MARGIN
