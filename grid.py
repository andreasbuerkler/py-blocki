from block import Block

class Grid(Block):

    def __init__(self, width, height):
        super().__init__()

        self.width = width
        self.height = height
        self.createString()


    def getLine(self, x1: int, y1: int, x2: int, y2: int) -> str:
        lineString = "<line x1=\""
        lineString += str(x1)
        lineString += "\" y1=\""
        lineString += str(y1)
        lineString += "\" x2=\""
        lineString += str(x2)
        lineString += "\" y2=\""
        lineString += str(y2)
        lineString += "\" />"
        return lineString


    def createString(self) -> None:
        self.svgString = "<g stroke=\"black\" fill=\"white\" stroke-width=\"0.5\" >\n"

        for xPos in range(0, self.width, 50):
            self.svgString += self.getLine(xPos, 0, xPos, self.height)

        for yPos in range(0, self.height, 50):
            self.svgString += self.getLine(0, yPos, self.width, yPos)

        self.svgString += "</g>"


    def mouseIsHovering(self, x: int, y: int) -> bool:
        _ = x
        _ = y
        return False


    def mouseIsPressed(self, active: bool) -> None:
        _ = active


    def mouseIsMoved(self, xChange: int, yChange: int) -> None:
        _ = xChange
        _ = yChange


    def resize(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.createString()


    def getSvgString(self) -> str:
        return self.svgString
