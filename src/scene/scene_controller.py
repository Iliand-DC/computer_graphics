class SceneController:
    """ manage all actions with actions
    """
    def __init__(self, scene):
        self.scene = scene

    def add_figure(self, figure):
        for line in figure.lines:
            if not line in self.scene.items():
                self.scene.addItem(line)

    def remove_figure(self, figure):
        for line in figure.lines:
            if line in self.scene.items():
                self.scene.removeItem(line)

