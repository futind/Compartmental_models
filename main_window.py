from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap

from functools import partial
from numpy import arange

from ui_main_user_interface import Ui_main_window

from epidemic_model import SIR_model
from endemic_model import SIR_vitality

class MainWindow(QMainWindow, Ui_main_window):
    # model is a variable that stores the value (SIR_model or SIR_vitality)
    model = None

    # model_index is a variable, that we use to understand what model the user
    # wants to research:
    # 0 - classic epidemic SIR model
    # 1 - endemic SIR model with populational dynamics
    model_index = None
    
    # model incidence is a boolean variable, that stores the incidence, that 
    # user wants to use:
    # False - Standard incidence (beta * I * S / N)
    # True - Mass action law incidence (beta * I * S)
    model_incidence = None

    # initializing the window
    def __init__(self, app):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Compartmental models")

        self.app = app
       
        self.change_model(0, True)
        self.plotting_widget.setCurrentIndex(0)

        # binding button's "clicked" signals to slots
        self.perform_button.clicked.connect(self.perform)
        self.clear_button.clicked.connect(self.clear)
        self.reset_button.clicked.connect(self.reset)

        # binding action's "triggered" signals to slots
        self.perform_action.triggered.connect(self.perform)
        self.clear_action.triggered.connect(self.clear)
        self.reset_action.triggered.connect(self.reset)
        self.quit_action.triggered.connect(self.quit)

        # binding actions and radiobuttons to the slots (Use QSignalMapper for passing the arguments to slots (?))
        # Actions:
        # classic SIR with standard incidence
        self.standard_incidence_action.triggered.connect(partial(self.change_model, 0, False))
        # classic SIR with mass action law incidence
        self.mass_action_incidence_action.triggered.connect(partial(self.change_model, 0, True))
        # SIR model with populational dynamics with standard incidence
        self.pop_standard_incidence_action.triggered.connect(partial(self.change_model, 1, False))
        # SIR model with populational dynamics with mass action law incidence
        self.pop_mass_action_incidence_action.triggered.connect(partial(self.change_model, 1, True))

        # Radiobuttons:
        # Changing model incidence to standard
        self.standard_radioButton.clicked.connect(partial(self.change_model_incidence, False))
        # Changing model incidence to mass action law
        self.mass_action_radioButton.clicked.connect(partial(self.change_model_incidence, True))
        # Changing model to classic SIR
        self.classic_sir_radioButton.clicked.connect(partial(self.change_model_index, 0))
        # Changing model to SIR with populational dynamics
        self.population_sir_radioButton.clicked.connect(partial(self.change_model_index, 1))

        # binding checkBox's "state changed" signals to slot, which redraws 
        # the graphics every time. Hopefully, it is a temporary solution.
        # TODO: MAKE A NORMAL HIDE/DISPLAY FUCNTION'S GRAPH SLOT!
        self.susceptible_checkBox.stateChanged.connect(self.change_graph_visibility)
        self.infectious_checkBox.stateChanged.connect(self.change_graph_visibility)
        self.recovered_checkBox.stateChanged.connect(self.change_graph_visibility)

    # drawing a main dynamics graph
    def comparmental_graph_draw(self):
        # clearing the axis
        self.dynamics_graph.canvas.ax.clear()

        # depending on chosen checkBoxes displaying the graphs needed
        if (self.susceptible_checkBox.isChecked()):
            self.dynamics_graph.canvas.ax.plot(self.model.time_data, self.model.susceptible_data, label = 'S(t)')
        if (self.infectious_checkBox.isChecked()):
            self.dynamics_graph.canvas.ax.plot(self.model.time_data, self.model.infectious_data, label = 'I(t)')
        if (self.recovered_checkBox.isChecked()):
            self.dynamics_graph.canvas.ax.plot(self.model.time_data, self.model.recovered_data, label = 'R(t)')

        # creating a legend on both axis
        self.dynamics_graph.canvas.ax.legend()

        # actually displaying the changes made to the axis
        self.dynamics_graph.canvas.draw()
    
    # drawing a phase graph
    def phase_graph_draw(self):
        # clearing the axis
        self.phase_graph.canvas.ax.clear()

        # displaying a phase graph
        self.phase_graph.canvas.ax.plot(self.model.susceptible_data, self.model.infectious_data, label = 'I(S)')
        self.phase_graph.canvas.ax.plot(range(0, self.model.initial_population, 1), range(self.model.initial_population, 0, -1))

        # creating a legend on both axis
        self.phase_graph.canvas.ax.legend()

        # actually displaying the changes made to the axis
        self.phase_graph.canvas.draw()

    # drawing a phase graph in fractions
    def frac_phase_graph_draw(self):
        # clearing the axis
        self.frac_phase_graph.canvas.ax.clear()

        # displaying a phase graph in fractions
        self.frac_phase_graph.canvas.ax.plot(self.model.susceptible_fraction_data, self.model.infectious_fraction_data, label = 'i(s)')
        self.frac_phase_graph.canvas.ax.plot(arange(0, 1, 0.001), arange(1, 0, -0.001))

        # creating a legend on both axis
        self.frac_phase_graph.canvas.ax.legend()

        # actually displaying the changes made to the axis
        self.frac_phase_graph.canvas.draw()

    # drawing a population dynamics graph
    def population_graph_draw(self):
        # clearing the axis
        self.population_graph.canvas.ax.clear()

        # displaying population dynamics
        if (self.model_index == 0):
            self.population_graph.canvas.ax.plot(self.model.time_data, [self.initial_population] * (self.observation_time + 2), label = 'N(t)')
        elif(self.model_index == 1):
            self.population_graph.canvas.ax.plot(self.model.time_data, self.model.population_data, label = 'N(t)')

        # creating a legend on both axis
        self.population_graph.canvas.ax.legend()

        # actually displaying the changes made to the axis
        self.population_graph.canvas.draw()

    # a method which displays graphs
    def draw(self):
        self.comparmental_graph_draw()
        self.phase_graph_draw()
        self.frac_phase_graph_draw()
        self.population_graph_draw()
        
    # this method is used to create a model's class, to perform the calculation, and to draw the graphs
    def perform(self):
        # getting the data from a user
        self.get_user_data()

        # time step is set as 1 day
        step = 1

        # creating a model instance (depending on the model)
        if (self.model_index == 0):
            self.model = SIR_model(self.model_incidence, self.susceptible, self.infectious, self.recovered,
                                   self.initial_population, self.contact_rate, self.recovery_rate, self.observation_time)
        elif (self.model_index == 1):
            self.model = SIR_vitality(self.model_incidence, self.susceptible, self.infectious, self.recovered,
                                      self.initial_population, self.observation_time, self.contact_rate, self.recovery_rate,
                                      self.mortality_rate, self.total_births)
        else:
            raise ValueError()
        
        # calculating 
        self.model.compute(step)

        # resetting the QTabWidget to the first tab
        self.plotting_widget.setCurrentIndex(0)

        # drawing all the graphs
        self.draw()
        
        # displaying the R0
        self.basic_reproduction_number_label.setText(f'Basic reproduction number: {self.model.basic_reproduction_number:.3}')

    # method that recieves data from a user
    def get_user_data(self):
        self.initial_population = self.population_size_spinBox.value()
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

        self.susceptible = self.initial_population - self.infectious
        self.recovered = self.initial_population - self.infectious - self.susceptible

    # method for clearing the ALL of the graph panes
    def clear(self):
        self.dynamics_graph.canvas.ax.clear()
        self.phase_graph.canvas.ax.clear()
        self.frac_phase_graph.canvas.ax.clear()
        self.population_graph.canvas.ax.clear()

        self.dynamics_graph.canvas.draw()
        self.phase_graph.canvas.draw()
        self.frac_phase_graph.canvas.draw()
        self.population_graph.canvas.draw()
        
        self.basic_reproduction_number_label.setText("Basic reproduction number:")
    
    # TODO: reset to default values for the model+incidence
    def reset(self):
        # kinda default values
        # TODO: make csv lists
        self.initial_population = self.population_size_spinBox.setValue(1000000)
        self.infectious = self.infections_size_spinBox.setValue(1)
        self.contact_rate = self.contact_rate_dSpinBox.setValue(0.33)
        self.recovery_rate = self.recovery_rate_dSpinBox.setValue(0.13)
        self.observation_time = self.observation_time_spinBox.setValue(365)

        self.clear()

    # method for exiting the app
    def quit(self):
        self.app.exit()

    # method that shows and hides certain graphs
    def change_graph_visibility(self):
        if (self.model != None):
            self.comparmental_graph_draw()

    # method that changes model_index (and calls for according changes in interface)
    def change_model_index(self, index: int):
        self.change_model(index, self.model_incidence)

    # method, that changes incidence (and calls for according changes in interface)
    def change_model_incidence(self, incidence: bool):
        self.change_model(self.model_index, incidence)

    # model that changes interface and pictures
    def change_model(self, index: int, incidence: bool):
        
        self.model_index = index
        self.model_incidence = incidence

        self.interface_change()
        self.clear()

    # method, that shows and hides some parts of the interface depending
    # on the model chosen
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
    
    # method, that refreshes picture depending on model and incidence
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