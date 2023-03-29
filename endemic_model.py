from epidemic_model import SIR_model

class SIR_vitality(SIR_model):
    instances = []

    def __init__(self, S: int, I: int, R: int, N: int, T:int,
                 beta: float, gamma: float, mu: float):
        
        assert mu > 0, f'ValueError: {mu} can not be less than zero'

        super().__init__(S, I, R, N, beta, gamma, T)

        self.__vitality_rate = mu

        self.__basic_reproduction_number = self.contact_rate / (self.recovery_rate + self.vitality_rate)
    
    # Getter for vitality rate
    @property
    def vitality_rate(self):
        return self.__vitality_rate
    
    # Setter for vitality rate
    @vitality_rate.setter
    def vitality_rate(self, mu: float):
        if (mu < 0):
            raise ValueError()
        else:
            self.__vitality_rate = mu
            if (self.recovery_rate > 0.0):
                self.__basic_reproduction_number = self.contact_rate / (self.recovery_rate + self.__vitality_rate)
    
    # Getter for basic reproduction number (R0)
    @property
    def basic_reproduction_number(self):
        return self.__basic_reproduction_number
    # NO SETTER FOR IT IS NEEDED, THIS VALUE MUST BE CALCULATED

    def suseptible_dynamics(self, S_step_increment = 0.0, I_step_increment = 0.0):
        return (self.vitality_rate * self.total_population - self.vitality_rate 
                * (self.suseptible_data[-1] + S_step_increment) 
                + super().suseptible_dynamics(S_step_increment, I_step_increment))

    def infectious_dynamics(self, S_step_increment = 0.0, I_step_increment = 0.0):
        return (super().infectious_dynamics(S_step_increment, I_step_increment)
                - self.vitality_rate * (self.infectious_data[-1] + I_step_increment))

    def recovered_dynamics(self, I_step_increment = 0.0, R_step_increment = 0.0):
        return (super().recovered_dynamics(I_step_increment, R_step_increment)
                - self.vitality_rate * (self.recovered_data[-1] + R_step_increment))

    def Runge_Kutta_fourth_order(self, increment: float):
        super().Runge_Kutta_fourth_order(increment)
    
    def compute(self, increment: float):
        super().compute(increment)
    
