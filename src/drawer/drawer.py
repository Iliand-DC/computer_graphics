from sdl2 import *
import ctypes
from math import sqrt, ceil


class Drawer:
    SEGMENTS_NUMBER = 50

    @classmethod
    def draw_line(cls, surface, camera, x1, y1, x2, y2, color, thickness = 1.):
        sx1 = 0
        sy1 = 0
        sx2 = 0
        sy2 = 0

        sx1, sy1 = camera.world_to_screen(x1, y1, sx1, sy1)
        sx2, sy2 = camera.world_to_screen(x2, y2, sx2, sy2)

        dx = sx2 - sx1
        dy = sy2 - sy1

        length = sqrt(dx * dx + dy * dy)

        if length < 0.001:
            return None

        dir_x = dx / length
        dir_y = dy / length

        perp_x = - dir_y
        perp_y = dir_x


        half_thickness = ceil(thickness / 2)

        for i in range(-half_thickness, half_thickness):
            offset_x1 = sx1 + int(perp_x * i)
            offset_y1 = sy1 + int(perp_y * i)

            offset_x2 = sx2 + int(perp_x * i)
            offset_y2 = sy2 + int(perp_y * i)


            dx = abs(offset_x2 - offset_x1)
            dy = abs(offset_y2 - offset_y1)

            sx = 1 if offset_x1 < offset_x2 else -1
            sy = 1 if offset_y1 < offset_y2 else -1


            err = dx - dy

            x = offset_x1
            y = offset_y1

            surf_con = surface.contents

            while not (x == offset_x2 and y == offset_y2):
                if (x >= 0 and x < surf_con.w and y >= 0 and y < surf_con.h):
                    pixels = ctypes.cast(surf_con.pixels, ctypes.POINTER(ctypes.c_uint32))
                    pixels[y * surf_con.w + x] = color
                    pixels = color

                e2 = 2 * err

                if e2 > -dy:
                    err -= dy
                    x += sx

                if e2 < dx:
                    err += dx
                    y += sy




    @classmethod
    def draw_curve(cls, surface, camera, x1, y1, cx, cy, x2, y2, color):
        last_x = x1
        last_y = y1

        for i in range(1, cls.SEGMENTS_NUMBER):
            t = i / cls.SEGMENTS_NUMBER

            xt = (1 - t) * (1 - t) * x1 + 2 * (1 - t) * t * cx + t * t *x2
            xt = (1 - t) * (1 - t) * y1 + 2 * (1 - t) * t * cy + t * t *y2

            cls.draw_line(surface, camera, last_x, last_y, xt, yt, color)
            last_x = xt
            last_y = yt


