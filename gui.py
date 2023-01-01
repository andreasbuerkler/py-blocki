from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import Qt, QMouseEvent, QResizeEvent
from PySide6.QtSvgWidgets import QSvgWidget
from typing import Callable


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mouseMoveFunctions: dict[str, Callable[[int, int], None]] = {}
        self.mousePressFunctions: dict[str, Callable[[bool], None]] = {}
        self.mouseHoverFunctions: dict[str, Callable[[int, int], bool]] = {}
        self.updateFunctions: dict[str, Callable[[], None]] = {}
        self.resizeFunctions: dict[str, Callable[[int, int], None]] = {}

        self.setMouseTracking(True)
        self.svg_widget = QSvgWidget()
        self.setCentralWidget(self.svg_widget)
        self.centralWidget().setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.xOld = 0
        self.yOld = 0


    def _update(self) -> None:
        for updateFunc in self.updateFunctions.values():
            updateFunc()


    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        xPos = event.pos().x()
        yPos = event.pos().y()
        xDiff = xPos - self.xOld
        yDiff = yPos - self.yOld

        for name, mouseIsHovering in self.mouseHoverFunctions.items():
            if mouseIsHovering(xPos, yPos):
                moveFunc = self.mouseMoveFunctions[name]
                moveFunc(xDiff, yDiff)

        self.xOld = xPos
        self.yOld = yPos

        self._update()


    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            for pressFunc in self.mousePressFunctions.values():
                pressFunc(True)


    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            for pressFunc in self.mousePressFunctions.values():
                pressFunc(False)


    def resizeEvent(self, event: QResizeEvent) -> None:
        for resizeFunc in self.resizeFunctions.values():
            resizeFunc(event.size().width(), event.size().height())
        self._update()


    def registerMouseHoverFunc(self, name: str, func: Callable[[int, int], bool]) -> None:
        self.mouseHoverFunctions[name] = func


    def registerMouseMoveFunc(self, name: str, func: Callable[[int, int], None]) -> None:
        self.mouseMoveFunctions[name] = func


    def registerMousePressFunc(self, name: str, func: Callable[[bool], None]) -> None:
        self.mousePressFunctions[name] = func


    def registerUpdateFunc(self, name: str, func: Callable[[], None]) -> None:
        self.updateFunctions[name] = func


    def registerResizeFunc(self, name: str, func: Callable[[int, int], None]) -> None:
        self.resizeFunctions[name] = func
