from model.matrix2d import Matrix2D


class Point:
    """ point class which will hold info about one point
    """
    def __init__(self, vertices = None):
        self.vertices = vertices or Matrix2D()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}\n vertices: {self.vertices}"
