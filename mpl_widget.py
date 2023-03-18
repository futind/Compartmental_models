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
        self.vertical_mpl_layout = QtWidgets.QVBoxLayout()
        self.vertical_mpl_layout.addWidget(self.canvas)
        self.vertical_mpl_layout.addWidget(self.mpl_toolbar)
        self.setLayout(self.vertical_mpl_layout)
        