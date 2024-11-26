class Drawer:
    @staticmethod
    def draw_line(surface, camera, x1, y1, x2, y2, color, thickness = 1.):
        sx1, sy1, sx2, sy2 = 0

        camera.worldToScreen(x1, y1, sx1, sy1)
        camera.worldToScreen(x2, y2, sx2, sy2)

        dx = sx2 - sx1
        dy = sy2 - sy1

        try:
            length = sqrt(dx * dx + dy * dy)

        except Exception as err:
            print(err)
            return None

        dir_x = dx / length
        dir_y = dy / length

        perp_x = - dir_y
        perp_y = dir_x


        half_thickness = int(thickness / 2)

        for i in range(-half_thickness, half_thickness):
            offset_x1 = sx1 + 

