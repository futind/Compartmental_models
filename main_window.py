from PySide6.QtWidgets import QMainWindow
from ui_main_user_interface import Ui_main_window

from base_model import SIR_model

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

        total_population = self.population_size_spinBox.value()
        infectious = self.infections_size_spinBox.value()
        contact_rate = self.contact_rate_dSpinBox.value()
        recovery_rate = self.recovery_rate_dSpinBox.value()
        suseptible = total_population - infectious
        observation_time = self.observation_time_spinBox.value()

        step = 1
        sir = SIR_model(suseptible, infectious, recovery_rate, total_population, contact_rate, recovery_rate, observation_time)
        sir.compute(step)

        # TO DO 1: make the graphics appear (so make the system and RK4 and etc bruh)
        # TO DO 2: make a function to make the calculations, and a function to show graphs
        # you can store the data, no need to recalculate every time user needs to display/erase
        # a graph from a pane

        print("TIME: ", sir.time_data)
        print("S: ", sir.suseptible_data)
        print("I: ", sir.infectious_data)
        print("R: ", sir.recovered_data)
        if (self.suseptible_checkBox.isChecked()):
            self.dynamics_graph.canvas.ax.plot(sir.time_data, sir.suseptible_data)
        if (self.infectious_checkBox.isChecked()):
            self.dynamics_graph.canvas.ax.plot(sir.time_data, sir.infectious_data)
        if (self.recovered_checkBox.isChecked()):
            self.dynamics_graph.canvas.ax.plot(sir.time_data, sir.recovered_data)
        self.phase_graph.canvas.ax.plot(sir.suseptible_data, sir.infectious_data)

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