from shape.shape import *
from sdl2.ext.surface import *


class Model2D:
    def __init__(self, pos_x = 0., pos_y = 0., rotation = 0., scale_x = 1., scale_y = 1.):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rotation = rotation
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.shapes = []


    def move(self, dx, dy):
        self.pos_x += dx
        self.pos_y += dy


    def rotate(self, degrees):
        self.rotation += degrees


    def add_line(self, x1, y1, x2, y2, color, thickness = 1.):
        self.shapes.append(Line2D(Point(x1, y1), 
                                  Point(x2, y2), 
                                  color, thickness))


    def add_curve(self, x1, y1, cx, cy, x2, y2, color):
        self.shapes.appendI(Line2D(Point(x1, y1),
                                   Point(x2, y2),
                                   color))


    def draw(self, surface, camera):
        for shape in self.shapes:
            shape.draw(surface, camera, 
                       self.pos_x, self.pos_y, 
                       self.rotation, self.scale_x, 
                       self.scale_y)
