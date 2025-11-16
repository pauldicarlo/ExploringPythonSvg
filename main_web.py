

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt

from sailocus.server import server


# TODO: create a main for running the server version
server.runApp()