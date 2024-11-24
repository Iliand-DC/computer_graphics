from model.figure import *


class ClosedFigure(Figure):
    """ create closed figure
    """
    def create_lines(self) -> None:
        super().create_lines()
        line = QGraphicsLineItem()
        last_edge = self.edges[-1][1]
        first_edge = self.edges[0][0]
        line.setLine(first_edge[0], first_edge[1], last_edge[0], last_edge[1])
        self.lines.append(line)
