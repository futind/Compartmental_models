from PySide6.QtWidgets import QMainWindow
from ui_main_user_interface import Ui_main_window

import numpy as np

class MainWindow(QMainWindow, Ui_main_window):
    def __init__(self, app):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Compartmental models")

        self.app = app

        self.perform_button.clicked.connect(self.perform)
        self.clear_button.clicked.connect(self.clear)

        self.perform_action.triggered.connect(self.perform)
        self.clear_action.triggered.connect(self.clear)
        self.reset_action.triggered.connect(self.reset)
        self.quit_action.triggered.connect(self.quit)
    
    def perform(self):
        self.dynamics_graph.canvas.ax.clear()
        self.phase_graph.canvas.ax.clear()

        observation_time = self.observation_time_spinBox.value()
        time = np.arange(0, observation_time, 1)

        # TO DO 1: make the graphics appear (so make the system and RK4 and etc bruh)
        # TO DO 2: make a function to make the calculations, and a function to show graphs
        # you can store the data, no need to recalculate every time user needs to display/erase
        # a graph from a pane

        if (self.suseptible_checkBox.isChecked()):
            pass
        if (self.infectious_checkBox.isChecked()):
            pass
        if (self.recovered_checkBox.isChecked()):
            pass

        self.dynamics_graph.canvas.draw()
        self.phase_graph.canvas.draw()
    
    def clear(self):
        self.dynamics_graph.canvas.ax.clear()
        self.phase_graph.canvas.ax.clear()
        self.dynamics_graph.canvas.draw()
        self.phase_graph.canvas.draw()
    
    def reset(self):
        pass

    def quit(self):
        pass