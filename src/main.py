import sys
from math import sin, tan

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from model.line import Line
from model.matrix2d import Matrix2D
from model.figure import Figure
from model.closed_figure import ClosedFigure

from camera.camera2d import Camera2D

from view.view import ZoomableGraphicsView
from scene.scene import Scene

import numpy as np


class Function:
    def __call__(self, func, x):
        return [func(item) for item in x]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.view = ZoomableGraphicsView()
        self.scene = Scene()

        x = np.linspace(0, 100, 1000)

        y = np.sin(x)

        matrix = Matrix2D()
        for i in range(len(x)):
            matrix_data = [x[i], y[i]]
            matrix.data.append(matrix_data)

        figure = Figure(matrix)

        figure.create_lines()

        self.scene.scene_controller.add_figure(figure)

        self.view.setScene(self.scene)

        self.camera = Camera2D(self)

        self.view.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    app.exec_()

