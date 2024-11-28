from shape.shape import *


class Graphics:
    def __init__(self, model, x_array, y_array, color = None):
        self.model = model
        self.x_array = x_array
        self.y_array = y_array
        self.color = color or 0x000000
        self.curves = []


    def create_graphic(self):
        for i in range(len(self.x_array) - 1):
            curve_start = Point(self.x_array[i], self.y_array[i])

            middle_x = (self.x_array[i] + self.x_array[i+1]) / 2
            middle_y = (self.y_array[i] + self.y_array[i+1]) / 2
            curve_control = Point(middle_x, middle_y)

            curve_end = Point(self.x_array[i+1], self.y_array[i+1])

            self.model.add_curve(curve_start.x,
                                 curve_start.y,
                                 curve_control.x,
                                 curve_control.y,
                                 curve_end.x,
                                 curve_end.y,
                                 self.color)

