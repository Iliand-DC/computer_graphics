class Matrix2D:
    """ matrix class which will contain verticies of elements
    """
    def __init__(self, data: list[list[int]] = None) -> None:
        self.data = data or []

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.data}\nsize: {len(self.data)}"

