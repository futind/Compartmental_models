from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap

from ui_main_user_interface import Ui_main_window

from functools import partial

from epidemic_model import SIR_model
from endemic_model import SIR_vitality



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

        # Use QSignalMapper ???
        self.standard_incidence_action.triggered.connect(partial(self.change_model_sir_classic, False))
        self.mass_action_incidence_action.triggered.connect(partial(self.change_model_sir_classic, True))
        
        #
        self.pop_standard_incidence_action.triggered.connect(partial(self.change_model_sir_vitality, False))
        self.pop_mass_action_incidence_action.triggered.connect(partial(self.change_model_sir_vitality, True))

        

        # binding checkBox's "state changed" signals to slot, which redraws 
        # the graphics every time. Hopefully, it is a temporary solution.
        # TODO: MAKE A NORMAL HIDE/DISPLAY FUCNTION'S GRAPH SLOT!
        self.suseptible_checkBox.stateChanged.connect(self.change_graph_visibility)
        self.infectious_checkBox.stateChanged.connect(self.change_graph_visibility)
        self.recovered_checkBox.stateChanged.connect(self.change_graph_visibility)
        
        self.standard_radioButton.toggled.connect(self.change_incidence_SI)
        self.mass_action_radioButton.toggled.connect(self.change_incidence_MAI)

        # creating a model class, so if there is no model instantiated,
        # checkbox's slot wouldn't do anything
        self.model = None
        self.model_incidence = True
        self.model_index = 0
        self.change_model_sir_classic(True)

    # a method which displays graphs
    def draw(self):

        # clearing the axis
        self.dynamics_graph.canvas.ax.clear()
        self.phase_graph.canvas.ax.clear()

        # depending on chosen checkBoxes displaying the graphs needed
        if (self.suseptible_checkBox.isChecked()):
            self.dynamics_graph.canvas.ax.plot(self.model.time_data, self.model.suseptible_data, label = 'S(t)')
        if (self.infectious_checkBox.isChecked()):
            self.dynamics_graph.canvas.ax.plot(self.model.time_data, self.model.infectious_data, label = 'I(t)')
        if (self.recovered_checkBox.isChecked()):
            self.dynamics_graph.canvas.ax.plot(self.model.time_data, self.model.recovered_data, label = 'R(t)')

        # displaying a phase pane graph
        self.phase_graph.canvas.ax.plot(self.model.suseptible_data, self.model.infectious_data, label = 'I(S)')
        self.phase_graph.canvas.ax.plot(range(0, self.model.total_population, 1), range(self.model.total_population, 0, -1))

        # creating a legend on both axis, so we can understand which function has a certain color
        # on a graph
        self.dynamics_graph.canvas.ax.legend()
        self.phase_graph.canvas.ax.legend()

        # actually displaying the changes made to the axis
        self.dynamics_graph.canvas.draw()
        self.phase_graph.canvas.draw()
        
    # this method is used to create a model's class, to perform the calculation, and to draw the graphs
    def perform(self):
        # getting the data
        self.get_user_data()

        # time step is set as 1 day
        step = 1

        

        #
        if (self.model_index == 0):
            self.model = SIR_model(self.suseptible, self.infectious, self.recovered,
                                   self.total_population, self.contact_rate,
                                   self.recovery_rate, self.observation_time)
        elif (self.model_index == 1):
            self.model = SIR_vitality(self.suseptible, self.infectious, self.recovered,
                                      self.total_population, self.observation_time,
                                      self.contact_rate, self.recovery_rate, self.vitality_rate)
        else:
            raise ValueError()
        
        self.model.compute(step)

        self.draw()
        
        self.basic_reproduction_number_label.setText(f'Basic reproduction number: {self.model.basic_reproduction_number}')

    def get_user_data(self):
        self.total_population = self.population_size_spinBox.value()
        self.infectious = self.infections_size_spinBox.value()
        self.contact_rate = self.contact_rate_dSpinBox.value()
        self.recovery_rate = self.recovery_rate_dSpinBox.value()
        self.observation_time = self.observation_time_spinBox.value()

        if (self.model_index == 1):
            self.vitality_rate = self.vitality_rate_dSpinBox.value()
        else:
            self.vitality_rate = -1

        self.suseptible = self.total_population - self.infectious
        self.recovered = self.total_population - self.infectious - self.suseptible

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
    
    #
    def change_incidence_MAI(self):
        self.model_incidence = True

        self.refresh_picture()
    
    #
    def change_incidence_SI(self):
        self.model_incidence = False

        self.refresh_picture()
    
    def refresh_picture(self):
        if (self.model_index == 0):
            if (self.model_incidence == True):
                self.model_pixlabel.setPixmap(QPixmap('resources/images/SIR_epidemic_mass_action.png'))
            else:
                self.model_pixlabel.setPixmap(QPixmap('resources/images/SIR_epidemic_standard'))
        else:
            if (self.model_incidence == True):
                self.model_pixlabel.setPixmap(QPixmap('resources/images/SIR_endemic_mass_action'))
            else:
                self.model_pixlabel.setPixmap(QPixmap('resources/images/SIR_endemic_standard'))

    def change_model_sir_classic(self, inc: bool):
        
        self.model_incidence = inc

        if ( self.model_index != 0 ):
            self.model_index = 0

            # Displaying the name of the model
            self.model_displayed_label.setText("Model: Classical epidemic SIR model")

            # Hiding the groupBox which contains population dynamic parameters:
            # \nu - total briths and \mu - mortality rate
            self.pop_dyn_groupBox.setVisible(False)

            # Hiding population tab on TabWidget
            #self.population_graphpane.setEnabled(False)
   
            self.clear()
        
        # Refreshing the picture
        self.refresh_picture()
    
    def change_model_sir_vitality(self, inc: bool):
        
        self.model_incidence = inc

        if (self.model_index != 1):
            self.model_index = 1

            # Displaying the name of the model
            self.model_displayed_label.setText("Model: Endemic model with population dynamics")

            # Displaying the groupBox which contains population dynamic parameters
            self.pop_dyn_groupBox.setVisible(True)

            # Displaying population tab
            #self.population_graphpane.setEnabled(True)

            self.clear()
        
        # Refreshing the picture
        self.refresh_picture()