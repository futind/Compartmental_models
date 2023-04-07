from epidemic_model import SIR_model

class SIR_vitality(SIR_model):
    instances = []

    def __init__(self, S: int, I: int, R: int, N: int, T:int,
                 beta: float, gamma: float, mu: float, nu: float):
        
        assert mu > 0, f'ValueError: {mu} can not be less or equal to zero'
        assert nu >= 0, f'ValueError: {nu} can not be less than zero'

        super().__init__(S, I, R, N, beta, gamma, T)

        # mu is deaths per capita (per unit time?)
        self.__mortality_rate = mu
        # nu is a total amount of newborns (per unit time?)
        self.__total_births = nu

        # basic reproduction number
        self.__basic_reproduction_number = (self.contact_rate * self.total_births) / (self.mortality_rate * (self.recovery_rate + self.mortality_rate))

        self.population_data = list()
        self.sirsum_test_data = list()
        SIR_vitality.instances.append(self)
    
    # Adding a representation of our class
    def __repr__(self):
        return f'SIR_vitality(S = {self.suseptible}, I = {self.infectious}, R ={self.recovered}, ' \
               f'N = {self.total_population}), beta = {self.contact_rate}, gamma = {self.recovery_rate}, ' \
               f'mu = {self.mortality_rate},)'

    # Getter for mortality rate
    @property
    def mortality_rate(self):
        return self.__mortality_rate
    
    # Setter for mortality rate
    @mortality_rate.setter
    def mortality_rate(self, mu: float):
        if (mu <= 0):
            raise ValueError()
        else:
            self.__mortality_rate = mu
            self.__basic_reproduction_number = (self.contact_rate * self.total_births) / (self.mortality_rate * (self.recovery_rate + self.mortality_rate))
    
    # Getter for total births
    @property
    def total_births(self):
        return self.__total_births
    
    #Setter for total births
    @total_births.setter
    def total_births(self, nu: float):
        if (nu < 0):
            raise ValueError()
        else:
            self.__total_births = nu
    
    # Getter for basic reproduction number (R0)
    @property
    def basic_reproduction_number(self):
        return self.__basic_reproduction_number
    # NO SETTER FOR IT IS NEEDED, THIS VALUE MUST BE CALCULATED

    def suseptible_dynamics(self, S_step_increment = 0.0, I_step_increment = 0.0):
        return (self.total_births - self.contact_rate * (self.infectious_data[-1] + I_step_increment) 
                * (self.suseptible_data[-1] + S_step_increment) - self.mortality_rate * (self.suseptible_data[-1] + S_step_increment))

    def infectious_dynamics(self, S_step_increment = 0.0, I_step_increment = 0.0):
        return (self.contact_rate * (self.infectious_data[-1] + I_step_increment) * (self.suseptible_data[-1] + S_step_increment)
                - self.recovery_rate * (self.infectious_data[-1] + I_step_increment) - self.mortality_rate 
                * (self.infectious_data[-1] + I_step_increment))

    def recovered_dynamics(self, I_step_increment = 0.0, R_step_increment = 0.0):
        return (self.recovery_rate * (self.infectious_data[-1] + I_step_increment) 
                - self.mortality_rate * (self.recovered_data[-1] + R_step_increment))
    
    def population_dynamics(self, N_step_increment = 0.0):
        return (self.total_births - self.mortality_rate * (self.population_data[-1] + N_step_increment))

    def Runge_Kutta_fourth_order(self, increment: float):
        super().Runge_Kutta_fourth_order(increment)
        self.sirsum_test_data.append(self.suseptible_data[-1] + self.infectious_data[-1] + self.recovered_data[-1])
        
    
    def Runge_Kutta_population(self, increment: float):
        n1 = self.population_dynamics()
        n2 = self.population_dynamics(increment * n1 / 2.0)
        n3 = self.population_dynamics(increment * n2 / 2.0)
        n4 = self.population_dynamics(increment * n3)

        self.population_data.append(self.population_data[-1] + (increment / 6.0) * (n1 + (2 * n2) + (2 * n3) + n4))
        

    def compute(self, increment: float):
        super().compute(increment)

        self.sirsum_test_data.clear()

        time = 0.0

        self.sirsum_test_data.append(float(self.suseptible) + float(self.infectious) + float(self.recovered))
        
        self.population_data.append(self.total_population)
        while(time <= self.observation_time):
            time += increment
            self.Runge_Kutta_population(increment)
            
        

    
