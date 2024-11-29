from shape.point import *
from drawer.drawer import *


class Axis:

    LEFT    = -1
    RIGHT   = 1
    TOP     = -1
    BOTTOM  = 1

    def draw(self, surface, camera, model_x, model_y):
        horizontal_line_start = Point(self.LEFT, 0)
        horizontal_line_end = Point(self.RIGHT, 0)

        vertical_line_start = Point(0, self.TOP)
        vertical_line_end = Point(0, self.BOTTOM)


        horizontal_line_start.x += model_x
        horizontal_line_start.y += model_y


        horizontal_line_end.x += model_x
        horizontal_line_end.y += model_y


        vertical_line_start.x += model_x
        vertical_line_start.y += model_y


        vertical_line_end.x += model_x
        vertical_line_end.y += model_y


        Drawer.draw_line(surface, camera, 
                         horizontal_line_start.x, 
                         horizontal_line_start.y, 
                         horizontal_line_end.x, 
                         horizontal_line_end.y, 
                         0x000000)

        Drawer.draw_line(surface, camera, 
                         vertical_line_start.x, 
                         vertical_line_start.y, 
                         vertical_line_end.x, 
                         vertical_line_end.y, 
                         0x000000)

