from shape.point import *


class Camera2D:
    def __init__(self, width = 0, height = 0):
        self.position = Point(0, 0)
        self.zoom = 1.
        self.width = width
        self.height = height
        self.update_aspect_ratio()

    def update_aspect_ratio(self):
        self.aspect_ratio = self.width / self.height


    def normalize_coordinate(self, value, is_x):
        if is_x:
            return value * min(1., 1. / self.aspect_ratio)
        else:
            return value * min(1., self.aspect_ratio)


    def denormalize_coordinate(self, value, is_x):
        if is_x:
            return value / min(1., 1. / self.aspect_ratio)
        else:
            return value / min(1., self.aspect_ratio)


    def move(self, dx, dy):
        normalized_dx = dx * 2. / self.width / self.zoom
        normalized_dy = dy * 2. /self.height / self.zoom

        self.position.x += self.normalize_coordinate(normalized_dx, True)
        self.position.y += self.normalize_coordinate(normalized_dy, False)


    def set_position(self, x, y):
        self.position.x = self.normalize_coordinate(x, True)
        self.position.y = self.normalize_coordinate(y, False)


    def update_screen_size(self, width, height):
        old_aspect = self.aspect_ratio

        self.width = width
        self.height = height

        self.update_aspect_ratio()

        if(old_aspect != self.aspect_ratio):
            self.position.x = self.normalize_coordinate(
                self.denormalize_coordinate(self.position.x, True), True
            )

            self.position.y = self.normalize_coordinate(
                self.denormalize_coordinate(self.position.y, False), False
            )


    def world_to_screen(self, world_x, world_y, screen_x, screen_y):
        normalized_x = self.normalize_coordinate(world_x - self.position.x, True) * self.zoom
        normalized_y = self.normalize_coordinate(world_y - self.position.y, False) * self.zoom

        screen_x = int((normalized_x + 1.) * self.width * 0.5)
        screen_y = int((normalized_y + 1.) * self.height * 0.5)

        return [screen_x, screen_y]


    def screen_to_world(self, screen_x, screen_y, world_x, world_y):
        normalized_x = (screen_x * 2. / self.width - 1.)
        normalized_y = (screen_y * 2. / self.height - 1.)

        normalized_x = self.denormalize_coordinate(normalized_x / self.zoom, True)
        normalized_y = self.denormalize_coordinate(normalized_y / self.zoom, False)

        world_x = normalized_x + self.position.x
        world_y = normalized_y + self.position.y

        return [world_x, world_y]
