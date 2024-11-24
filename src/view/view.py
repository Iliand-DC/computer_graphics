from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class DraggableGraphicsView(QGraphicsView):
    """ view that can be dragged by left mouse button
    """
    def __init__(self):
        super().__init__()
        self.mouse_pressed = False

    def mousePressEvent(self, event):
        self.mouse_pressed = True
        self.mouse_prev_pos = event.pos()
        self.setCursor(Qt.ClosedHandCursor)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.mouse_pressed = False
        self.setCursor(Qt.ArrowCursor)
        super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.mouse_pressed:
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - (event.x() - self.mouse_prev_pos.x()))
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - (event.y() - self.mouse_prev_pos.y()))
            self.mouse_prev_pos = event.pos()

        super().mouseMoveEvent(event)


class ZoomableGraphicsView(DraggableGraphicsView):
    """ view that can be zoomed to mouse position
    """
    def __init__(self):
        super().__init__()
        self.zoom_factor = 1

    def wheelEvent(self, event):
        zoom_in_factor = 1.1
        zoom_out_factor = 1 / zoom_in_factor
        if event.modifiers() & Qt.ControlModifier:

            self.setTransformationAnchor(super().NoAnchor)
            self.setResizeAnchor(super().NoAnchor)

            old_pos = self.mapToScene(event.pos())

            if event.angleDelta().y() < 0:
                self.zoom_factor = zoom_out_factor
            else:
                self.zoom_factor = zoom_in_factor

            self.scale(self.zoom_factor, self.zoom_factor)

            new_pos = self.mapToScene(event.pos())

            delta = new_pos - old_pos
            self.translate(delta.x(), delta.y())

        else:
            super().wheelEvent(event)

