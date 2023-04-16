from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap

from ui_main_user_interface import Ui_main_window

from functools import partial

from epidemic_model import SIR_model
from endemic_model import SIR_vitality

# for debugging
from inspect import stack


class MainWindow(QMainWindow, Ui_main_window):
    model = None
    model_index = None
    model_incidence = None

    def __init__(self, app):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Compartmental models")

        self.app = app

        
        print("initial")
        self.change_model(0, True)

        # binding button's "clicked" signals to slots
        self.perform_button.clicked.connect(self.perform)
        self.clear_button.clicked.connect(self.clear)
        self.reset_button.clicked.connect(self.reset)

        # binding action's "triggered" signals to slots
        self.perform_action.triggered.connect(self.perform)
        self.clear_action.triggered.connect(self.clear)
        self.reset_action.triggered.connect(self.reset)
        self.quit_action.triggered.connect(self.quit)

        # Use QSignalMapper ???
        self.standard_incidence_action.triggered.connect(partial(self.change_model, 0, False))
        self.mass_action_incidence_action.triggered.connect(partial(self.change_model, 0, True))
        
        #
        self.pop_standard_incidence_action.triggered.connect(partial(self.change_model, 1, False))
        self.pop_mass_action_incidence_action.triggered.connect(partial(self.change_model, 1, True))

        #
        self.standard_radioButton.clicked.connect(partial(self.change_model_incidence, False))
        self.mass_action_radioButton.clicked.connect(partial(self.change_model_incidence, True))

        # binding checkBox's "state changed" signals to slot, which redraws 
        # the graphics every time. Hopefully, it is a temporary solution.
        # TODO: MAKE A NORMAL HIDE/DISPLAY FUCNTION'S GRAPH SLOT!
        # TODO: it is susceptible, not suseptible
        self.suseptible_checkBox.stateChanged.connect(self.change_graph_visibility)
        self.infectious_checkBox.stateChanged.connect(self.change_graph_visibility)
        self.recovered_checkBox.stateChanged.connect(self.change_graph_visibility)

    # a method which displays graphs
    def draw(self):

        # clearing the axis
        self.dynamics_graph.canvas.ax.clear()
        self.phase_graph.canvas.ax.clear()
        self.frac_phase_graph.canvas.ax.clear()
        self.population_graph.canvas.ax.clear()

        # depending on chosen checkBoxes displaying the graphs needed
        if (self.suseptible_checkBox.isChecked()):
            self.dynamics_graph.canvas.ax.plot(self.model.time_data, self.model.suseptible_data, label = 'S(t)')
        if (self.infectious_checkBox.isChecked()):
            self.dynamics_graph.canvas.ax.plot(self.model.time_data, self.model.infectious_data, label = 'I(t)')
        if (self.recovered_checkBox.isChecked()):
            self.dynamics_graph.canvas.ax.plot(self.model.time_data, self.model.recovered_data, label = 'R(t)')

        # displaying a phase graph
        self.phase_graph.canvas.ax.plot(self.model.suseptible_data, self.model.infectious_data, label = 'I(S)')
        self.phase_graph.canvas.ax.plot(range(0, self.model.total_population, 1), range(self.model.total_population, 0, -1))

        # displaying a phase graph in fractions
        self.frac_phase_graph.canvas.ax.plot(self.model.suseptible_fraction_data, self.model.infectious_fraction_data, label = 'i(s)')

        # displaying population dynamics
        if (self.model_index == 0):
            self.population_graph.canvas.ax.plot(self.model.time_data, [self.total_population] * (self.observation_time + 2), label = 'N(t)')
        elif(self.model_index == 1):
            self.population_graph.canvas.ax.plot(self.model.time_data, self.model.population_data, label = 'N(t)')

        # creating a legend on both axis, so we can understand which function has a certain color
        # on a graph
        self.dynamics_graph.canvas.ax.legend()
        self.phase_graph.canvas.ax.legend()
        self.frac_phase_graph.canvas.ax.legend()
        self.population_graph.canvas.ax.legend()

        # actually displaying the changes made to the axis
        self.dynamics_graph.canvas.draw()
        self.phase_graph.canvas.draw()
        self.frac_phase_graph.canvas.draw()
        self.population_graph.canvas.draw()
        
    # this method is used to create a model's class, to perform the calculation, and to draw the graphs
    def perform(self):
        # getting the data
        self.get_user_data()

        # time step is set as 1 day
        step = 1

        #
        if (self.model_index == 0):
            self.model = SIR_model(self.model_incidence, self.suseptible, self.infectious, self.recovered,
                                   self.total_population, self.contact_rate, self.recovery_rate, self.observation_time)
        elif (self.model_index == 1):
            self.model = SIR_vitality(self.model_incidence, self.suseptible, self.infectious, self.recovered,
                                      self.total_population, self. observation_time, self.contact_rate, self.recovery_rate,
                                      self.mortality_rate, self.total_births)
        else:
            raise ValueError()
        
        self.model.compute(step)

        self.draw()
        
        self.basic_reproduction_number_label.setText(f'Basic reproduction number: {self.model.basic_reproduction_number}')

    #
    def get_user_data(self):
        self.total_population = self.population_size_spinBox.value()
        self.infectious = self.infections_size_spinBox.value()
        self.contact_rate = self.contact_rate_dSpinBox.value()
        self.recovery_rate = self.recovery_rate_dSpinBox.value()
        self.observation_time = self.observation_time_spinBox.value()

        if (self.model_index == 1):
            self.mortality_rate = self.mortality_rate_dSpinBox.value()
            self.total_births = self.total_births_spinBox.value()
        else:
            self.mortality_rate = -1
            self.total_births = -1

        self.suseptible = self.total_population - self.infectious
        self.recovered = self.total_population - self.infectious - self.suseptible

    #
    def clear(self):
        self.dynamics_graph.canvas.ax.clear()
        self.phase_graph.canvas.ax.clear()
        self.dynamics_graph.canvas.draw()
        self.phase_graph.canvas.draw()

        self.basic_reproduction_number_label.setText("Basic reproduction number:")
    
    # TODO: reset to default values for the model+incidence
    def reset(self):
        self.total_population = self.population_size_spinBox.setValue(0)
        self.infectious = self.infections_size_spinBox.setValue(0)
        self.contact_rate = self.contact_rate_dSpinBox.setValue(0.0)
        self.recovery_rate = self.recovery_rate_dSpinBox.setValue(0.0)
        self.observation_time = self.observation_time_spinBox.setValue(0)

        self.clear()

    #
    def quit(self):
        self.app.exit()

    #
    def change_graph_visibility(self):
        if (self.model != None):
            self.draw()

    #
    def change_model_incidence(self, incidence: bool):
        self.change_model(self.model_index, incidence)

    #
    def change_model(self, index: int, incidence: bool):
        
        print(f'[{self.model_index, index, self.model_incidence, incidence}]')
        self.model_index = index
        self.model_incidence = incidence

        self.interface_change()
        self.clear()

    #
    def interface_change(self):
        if (self.model_index == 0):
            # Displaying the name of the model
            self.model_displayed_label.setText("Model: Classical epidemic SIR model")

            # Hiding the groupBox which contains population dynamic parameters:
            # \nu - total briths and \mu - mortality rate
            self.pop_dyn_groupBox.setVisible(False)
        elif(self.model_index == 1):
            # Displaying the name of the model
            self.model_displayed_label.setText("Model: Endemic model with population dynamics")

            # Displaying the groupBox which contains population dynamic parameters
            self.pop_dyn_groupBox.setVisible(True)
        
        if (self.model_incidence == True):
            self.mass_action_radioButton.setChecked(True)
        else:
            self.standard_radioButton.setChecked(True)

        
        # Refreshing the picture
        self.refresh_picture()
    
    #
    def refresh_picture(self):
        if (self.model_index == 0):
            if (self.model_incidence == True):
                self.model_pixlabel.setPixmap(QPixmap('resources/images/SIR_epidemic_mass_action.png'))
            else:
                self.model_pixlabel.setPixmap(QPixmap('resources/images/SIR_epidemic_standard'))
        elif (self.model_index == 1):
            if (self.model_incidence == True):
                self.model_pixlabel.setPixmap(QPixmap('resources/images/SIR_endemic_mass_action'))
            else:
                self.model_pixlabel.setPixmap(QPixmap('resources/images/SIR_endemic_standard'))