from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from scene.scene_controller import SceneController
from scene.axis import Axis
from scene.grid import Grid


class Scene(QGraphicsScene):
    """ create scene which will draw in view
    """
    def __init__(self, top = 0, bottom = 1080, left = 0, right = 1920) -> None:
        super().__init__()
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

        self.scene_controller = SceneController(self)
        # self.grid = Grid(self)
        self.axis = Axis(self)

        self.setSceneRect(self.left, self.top, 
                          self.right, self.bottom)

    def center_x(self) -> int:
        return (self.right - self.left) / 2

    def center_y(self) -> int:
        return (self.bottom - self.top) / 2

