from model.matrix2d import Matrix2D


class Line:
    """ line class which will hold info about dots of line and one edge 
    """
    def __init__(self, verticies = None) -> None:
        self.verticies = verticies or Matrix2d()
        self.edges = [self.verticies.data[0], self.verticies.data[1]]

    def __str__(self) -> str:
        return f"{self.__class__.__name__}\n vertices: {self.verticies}\n edges: {self.edges}\n"

    def change_verticies(self, verticies) -> None:
        self.verticies = Matrix2D(verticies)
        self.edges = [self.verticies.data[0], self.verticies.data[1]]
