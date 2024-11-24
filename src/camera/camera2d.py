class Camera2D:
    def __init__(self, window):
        self.window = window

        self.left = window.pos().x()
        self.right = window.pos().x() + window.width()
        self.top = window.pos().y()
        self.bottom = window.pos().y() + window.height()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}\nleft: {self.left}\nright: {self.right}\ntop: {self.top}\nbottom: {self.bottom}\n"
