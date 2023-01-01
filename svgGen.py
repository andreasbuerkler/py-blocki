from rectangle import Rectangle
from grid import Grid
from gui import Gui
from PySide6.QtCore import QByteArray

class SvgGen():
    def __init__(self, width: int, height: int, svg: Gui):
        self.width = width
        self.height = height
        self.grid = Grid(width, height)
        self.rectangle = Rectangle(0, 0, 50, 50)
        self.svg = svg
        self.update()

        svg.registerMouseMoveFunc("gen", self.rectangle.mouseIsMoved)
        svg.registerMouseHoverFunc("gen", self.rectangle.mouseIsHovering)
        svg.registerMousePressFunc("gen", self.rectangle.mouseIsPressed)
        svg.registerUpdateFunc("gen", self.update)
        svg.registerResizeFunc("gen", self.resize)


    def resize(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.grid.resize(width, height)


    def update(self) -> None:
        image = QByteArray(self.GetImage().encode())
        self.svg.svg_widget.load(image)


    def GetImage(self) -> str:
        image = ""
        image += "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\""
        image += str(self.width)
        image += "\" height=\""
        image += str(self.height)
        image += "\" viewBox=\""
        image += str(0)
        image += " "
        image += str(0)
        image += " "
        image += str(self.width)
        image += " "
        image += str(self.height)
        image += "\">"

        image += self.grid.getSvgString()
        image += self.rectangle.getSvgString()

        image += "</svg>"

        return image
