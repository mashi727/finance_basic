'''
Imports are always put at the top of the file, just after any module
comments and docstrings, and before module globals and constants.

Imports should be grouped in the following order:

1. Standard library imports.
2. Related third party imports.
3. Local application/library specific imports.

You should put a blank line between each group of imports.
'''
import sys
import numpy as np
from datetime import datetime

from PySide6.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QWidget
from PySide6.QtGui import Qt
from PySide6 import QtWidgets

import pyqtgraph as pg
from pyqtgraph.dockarea import Dock
from pyqtgraph import QtCore, QtGui

# 自作のライブラリ
from financeUi import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.init_ui()
        self.plot()


    def init_ui(self):
        self.setGeometry(100, 100, 2200, 1400)

    def plot(self):
        # Dockの準備
        self.d1 = Dock('chart', size=(20, 15))
        self.d2 = Dock('region', size=(1, 2))

        self.graphicsView.addDock(self.d1)
        self.graphicsView.addDock(self.d2)
        glw = pg.GraphicsLayoutWidget()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    from pyqtgraph.dockarea.Dock import DockLabel
    def updateStyle(self):
        self.setStyleSheet("DockLabel { color: #FFF; background-color: #444; font-size:20pt}")
    setattr(DockLabel, 'updateStyle', updateStyle)

    style = """
        QWidget { color: #AAA; background-color: #333; border: 0px; padding:0px; }
        QWidget:item:selected { background-color: #666; }
        QMenuBar::item { background: transparent; }
        QMenuBar::item:selected { background: transparent; border: 1px solid#666; }
    """
    main()