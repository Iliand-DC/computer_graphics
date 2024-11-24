from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from model.matrix2d import Matrix2D


class Figure:
    """ create figure from vertex matrix
    """
    def __init__(self, verticies = None) -> None:
        self.verticies = verticies or Matrix2D()
        self.edges = []
        self.lines = []
        for i in range(len(self.verticies.data) - 1):
            self.edges.append([self.verticies.data[i], self.verticies.data[i + 1]])

        self.create_lines()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}\n vertices: {self.verticies}\n edges: {self.edges}\n"

    def change_verticies(self, verticies) -> None:
        self.verticies = Matrix2D(verticies)
        self.edges = []
        for edge in self.edges:
            for i in range(len(self.verticies.data) - 1):
                self.edges.append([self.verticies.data[i], self.verticies.data[i + 1]])

        self.lines = []
        self.create_lines()

    def create_lines(self) -> None:
        """ virtual method
        """
        for edge in self.edges:
            line = QGraphicsLineItem()
            line.setLine(edge[0][0], edge[0][1], edge[1][0], edge[1][1])
            self.lines.append(line)

