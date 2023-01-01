from PySide6.QtWidgets import QApplication
import sys
import traceback
from svgGen import SvgGen
from gui import Gui


def main():
    try:
        width = 500
        height = 500

        app = QApplication(sys.argv)
        window = Gui()
        SvgGen(width, height, window)

        window.resize(width, height)
        window.setWindowTitle("Hellou")
        window.show()

        sys.exit(app.exec())

    except Exception as err:
        print('%s', err)
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
