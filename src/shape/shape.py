from shape.point import *


class Shape2D:
    PI = 3.14
    def draw(self, surface, camera, model_x, model_y, rotation, scale_x, scale_y):
        raise NotImplementedError(
            f"implement draw method in {self.__class__.__name__}")

    def rotate_position(self, pos, degrees):
        radians = degrees * self.PI / 180.

        cos_a = cos(radians)
        sin_a = sin(radians)

        new_x = pos.x * cos_a - pos.y * sin_a
        new_y = pos.x * sin_a + pos.y * cos_a

        pos.x = new_x
        pos.y = new_y


class Line2D(Shape2D):
    def __init__(self, start = None, end = None, color = None, thickness = 1.0):
        self.start = start
        self.end = end
        self.color = color
        self.thickness = thickness

    def draw(self, surface, camera, model_x, model_y, rotation, scale_x, scale_y):
        transformed_start = Point(self.start.x * scale_x, self.start.y * scale_y)
        transformed_end = Point(self.end.x * scale_x, self.end.y * scale_y)

        self.rotate_position(transformed_start, rotation)
        self.rotate_position(transformed_end, rotation)

        transformed_start.x += model_x
        transformed_start.y += model_y

        transformed_end.x += model_x
        transformed_end.y += model_y


