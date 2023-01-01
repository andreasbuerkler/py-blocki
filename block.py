from abc import ABC, abstractmethod

class Block(ABC):

    @abstractmethod
    def mouseIsHovering(self, x: int, y: int) -> bool:
        pass


    @abstractmethod
    def mouseIsPressed(self, bool) -> None:
        pass


    @abstractmethod
    def mouseIsMoved(self, xChange: int, yChange: int) -> None:
        pass


    @abstractmethod
    def resize(self, width: int, height: int) -> None:
        pass


    @abstractmethod
    def getSvgString(self) -> str:
        pass
