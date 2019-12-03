import sys

from PyQt5.QtWidgets import QApplication

from core.BooxWindow import BookShelf


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_w = BookShelf()
    main_w.show()
    sys.exit(app.exec())
