from PySide6.QtWidgets import QApplication
from main_window import MainWindow

import sys

# initializing the application
app = QApplication(sys.argv)

# initializing the window
Window = MainWindow(app)
# showing the window
Window.show()

# executing the application
app.exec()

