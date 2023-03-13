from PySide6 import QtWidgets
from mpl_canvas import MPLCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PySide6.QtWidgets import QSizePolicy

class MPLWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        # Inherit from QWidget
        QtWidgets.QWidget.__init__(self, parent)
        # Create canvas object
        self.canvas = MPLCanvas()
        # Create toolbar object
        self.mpl_toolbar = NavigationToolbar(self.canvas)
        # Set box for plotting
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.vbl.addWidget(self.mpl_toolbar)
        self.setLayout(self.vbl)
        