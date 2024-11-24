class Axis:
    """ create axis on scene
    """
    def __init__(self, scene) -> None:
        self.scene = scene
        self.create_axis()

    def create_axis(self) -> None:
        center_x = self.scene.center_x()
        center_y = self.scene.center_y()

        self.scene.addLine(center_x, self.scene.top, 
                           center_x, self.scene.bottom)

        self.scene.addLine(self.scene.left, center_y, 
                           self.scene.right, center_y)
