from PySide6.QtWidgets import QMainWindow
from ui_main_user_interface import Ui_main_window

from base_model import SIR_model

class MainWindow(QMainWindow, Ui_main_window):
    def __init__(self, app):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Compartmental models")

        self.app = app

        # binding button's "clicked" signals to slots
        self.perform_button.clicked.connect(self.perform)
        self.clear_button.clicked.connect(self.clear)

        # binding action's "triggered" signals to slots
        self.perform_action.triggered.connect(self.perform)
        self.clear_action.triggered.connect(self.clear)
        self.reset_action.triggered.connect(self.reset)
        self.quit_action.triggered.connect(self.quit)

        # binding checkBox's "state changed" signals to slot, which redraws 
        # the graphics every time. Hopefully, it is a temporary solution.
        # TO DO: MAKE A NORMAL HIDE/DISPLAY FUCNTION'S GRAPH SLOT!
        self.suseptible_checkBox.stateChanged.connect(self.change_graph_visibility)
        self.infectious_checkBox.stateChanged.connect(self.change_graph_visibility)
        self.recovered_checkBox.stateChanged.connect(self.change_graph_visibility)

        # creating a model class, so if there is no model instantiated,
        # checkbox's slot wouldn't do anything
        self.model = None

    # a method which displays graphs
    def draw(self, model: SIR_model):
        # clearing the axis
        self.dynamics_graph.canvas.ax.clear()
        self.phase_graph.canvas.ax.clear()

        # depending on chosen checkBoxes displaying the graphs needed
        if (self.suseptible_checkBox.isChecked()):
            self.dynamics_graph.canvas.ax.plot(model.time_data, model.suseptible_data, label = 'S(t)')
        if (self.infectious_checkBox.isChecked()):
            self.dynamics_graph.canvas.ax.plot(model.time_data, model.infectious_data, label = 'I(t)')
        if (self.recovered_checkBox.isChecked()):
            self.dynamics_graph.canvas.ax.plot(model.time_data, model.recovered_data, label = 'R(t)')

        # displaying a phase pane graph
        self.phase_graph.canvas.ax.plot(model.suseptible_data, model.infectious_data, label = 'I(S)')
        self.phase_graph.canvas.ax.plot(range(0, self.total_population, 1), range(self.total_population, 0, -1))

        # creating a legend on both axis, so we can understand which function has a certain color
        # on a graph
        self.dynamics_graph.canvas.ax.legend()
        self.phase_graph.canvas.ax.legend()

        # actually displaying the changes made to the axis
        self.dynamics_graph.canvas.draw()
        self.phase_graph.canvas.draw()
        
    # this method is used to create a model's class, to perform the calculation, and to draw the graphs
    def perform(self):
        self.get_user_data()
        step = 1

        self.model = SIR_model(self.suseptible, self.infectious, self.recovered, self.total_population,
                                self.contact_rate, self.recovery_rate, self.observation_time)
        self.model.compute(step)

        self.draw(self.model)
        #if 
        self.basic_reproduction_number_label.setText(f'Basic reproduction number: {self.basic_reproduction_number}')

    def get_user_data(self):
        self.total_population = self.population_size_spinBox.value()
        self.infectious = self.infections_size_spinBox.value()
        self.contact_rate = self.contact_rate_dSpinBox.value()
        self.recovery_rate = self.recovery_rate_dSpinBox.value()
        self.observation_time = self.observation_time_spinBox.value()

        self.suseptible = self.total_population - self.infectious
        self.recovered = self.total_population - self.infectious - self.suseptible
        
        self.basic_reproduction_number = self.contact_rate / self.recovery_rate

    def clear(self):
        self.dynamics_graph.canvas.ax.clear()
        self.phase_graph.canvas.ax.clear()
        self.dynamics_graph.canvas.draw()
        self.phase_graph.canvas.draw()

        self.basic_reproduction_number_label.setText("Basic reproduction number:")
    
    def reset(self):
        self.total_population = self.population_size_spinBox.setValue(0)
        self.infectious = self.infections_size_spinBox.setValue(0)
        self.contact_rate = self.contact_rate_dSpinBox.setValue(0.0)
        self.recovery_rate = self.recovery_rate_dSpinBox.setValue(0.0)
        self.observation_time = self.observation_time_spinBox.setValue(0)

        self.clear()

    def quit(self):
        self.app.exit()

    def change_graph_visibility(self):
        if (self.model != None):
            self.draw(self.model)