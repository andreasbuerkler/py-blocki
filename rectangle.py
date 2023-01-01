from block import Block

class Rectangle(Block):

    def __init__(self, x, y, width, height):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.active = False
        self.hover = False
        self.createString()


    def createString(self) -> None:
        if self.hover:
            self.svgString = "<g stroke=\"blue\" fill=\"white\" stroke-width=\"3\" >\n"
        else:
            self.svgString = "<g stroke=\"black\" fill=\"white\" stroke-width=\"3\" >\n"

        self.svgString += "<rect x=\""
        self.svgString += str(self.x)
        self.svgString += "\" y=\""
        self.svgString += str(self.y)
        self.svgString += "\" width=\""
        self.svgString += str(self.width)
        self.svgString += "\" height=\""
        self.svgString += str(self.height)
        self.svgString += "\" />"

        self.svgString += "</g>"


    def mouseIsHovering(self, x: int, y: int) -> bool:
        xInRange = False
        yInRange = False
        if ((x > self.x) and (x < self.x + self.width)):
            xInRange = True
        if ((y > self.y) and (y < self.y + self.height)):
            yInRange = True
        self.hover = xInRange and yInRange

        self.createString()
        return self.hover


    def mouseIsPressed(self, active: bool) -> None:
        if (not self.active) and active and self.hover:
            self.active = True
        if (not active):
            self.active = False


    def mouseIsMoved(self, xChange: int, yChange: int) -> None:
        if self.active:
            self.x += xChange
            self.y += yChange
            self.createString()


    def resize(self, width: int, height: int) -> None:
        _ = width
        _ = height


    def getSvgString(self) -> str:
        return self.svgString
