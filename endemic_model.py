from epidemic_model import SIR_model

class SIR_vitality(SIR_model):

    # An initialization method for our class
    def __init__(self, incidence: bool, S: int, I: int, R: int, N: int, T:int,
                 beta: float, gamma: float, mu: float, nu: int):
        
        assert mu > 0, f'ValueError: {mu} can not be less than zero'
        assert nu >= 0, f'ValueError: {nu} can not be less or equal to zero'

        super().__init__(incidence, S, I, R, N, beta, gamma, T)

        # Mortality rate per capita per unit time (mu)
        self.__mortality_rate = mu
        
        # Total births per unit time (nu)
        self.__total_births = nu

        # List that holds the amount of people in population
        self.population_data = list()

        # Calctulation the R0 - threshold quantity
        self.refresh_r0()
    
    # Adding a representation for SIR with population dynamics
    def __repr__(self):
        return f'SIR_POPULATION(S = {self.susceptible}, I = {self.infectious}, R ={self.recovered}, ' \
               f'N0 = {self.initial_population}, beta = {self.contact_rate}, gamma = {self.recovery_rate}, ' \
               f'mu = {self.mortality_rate}, nu = {self.total_births}, T = {self.observation_time})'

    # Getter for mortality rate (mu)
    @property
    def mortality_rate(self):
        return self.__mortality_rate
    
    # Setter for mortality rate (mu)
    @mortality_rate.setter
    def mortality_rate(self, mu: float):
        if (mu <= 0):
            raise ValueError()
        else:
            self.__mortality_rate = mu
            self.refresh_r0()
    
    # Getter for total births (nu)
    @property
    def total_births(self):
        return self.__total_births
    
    # Setter for total births (nu)
    @total_births.setter
    def total_births(self, nu: int):
        if (nu < 0):
            raise ValueError()
        else:
            self.__total_births
            self.refresh_r0()

    # Getter for basic reproduction number (R0)
    @property
    def basic_reproduction_number(self):
        return self.__basic_reproduction_number
    # NO SETTER FOR IT IS NEEDED, THIS VALUE !MUST! BE CALCULATED

    # A method for (re)calculation the R0 threshold value
    def refresh_r0(self):
        nu = self.total_births
        mu = self.mortality_rate
        beta = self.contact_rate
        gamma = self.recovery_rate

        if (self.mass_action_incidence):
            self.__basic_reproduction_number = ( nu * beta ) / ( mu * (gamma + mu) )
        else:
            self.__basic_reproduction_number = beta / ( gamma + mu )

    # All this equations are used in the Runge-Kutta's method, hence the increments
    # Dynamics equation for susceptible compartment (dS/dt basically)
    def susceptible_dynamics(self, S_inc = 0.0, I_inc = 0.0, N_inc = 0.0):
        mass_action = self.mass_action_incidence
        
        beta = self.contact_rate
        nu = self.total_births
        mu = self.mortality_rate

        S = self.susceptible_data[-1] + S_inc
        I = self.infectious_data[-1] + I_inc
        N = self.population_data[-1] + N_inc

        if (mass_action):
            return nu - beta * I * S - mu * S
        else:
            return nu - beta * I * S / N - mu * S

    # Dynamics equation for infectious compartment (dI/dt)
    def infectious_dynamics(self, S_inc = 0.0, I_inc = 0.0, N_inc = 0.0):
        mass_action = self.mass_action_incidence

        beta = self.contact_rate
        gamma = self.recovery_rate
        mu = self.mortality_rate

        S = self.susceptible_data[-1] + S_inc
        I = self.infectious_data[-1] + I_inc
        N = self.population_data[-1] + N_inc

        if (mass_action):
            return beta * I * S - gamma * I - mu * I
        else:
            return beta * I * S / N - gamma * I - mu * I

    # Dynamics equation for recovered compartment (dR/dt)
    def recovered_dynamics(self, I_inc = 0.0, R_inc = 0.0):
        gamma = self.recovery_rate
        mu = self.mortality_rate

        I = self.infectious_data[-1] + I_inc
        R = self.recovered_data[-1] + R_inc

        return gamma * I - mu * R 

    # Popylation dynamics equation (dN/dt)
    def population_dynamics(self, N_inc = 0.0):
        nu = self.total_births
        mu = self.mortality_rate
        N = self.population_data[-1] + N_inc

        return nu - mu * N

    # The implementation of Runge-Kutta's method for
    # SIR model with population dynamics
    def Runge_Kutta_fourth_order(self, increment: float):
        s1 = self.susceptible_dynamics()
        i1 = self.infectious_dynamics()
        r1 = self.recovered_dynamics()
        n1 = self.population_dynamics()

        s2 = self.susceptible_dynamics(increment * s1 / 2.0, increment * i1 / 2.0)
        i2 = self.infectious_dynamics(increment * s1 / 2.0, increment * i1 / 2.0)
        r2 = self.recovered_dynamics(increment * i1 / 2.0, increment * r1 / 2.0)
        n2 = self.population_dynamics(increment * n1 / 2.0)

        s3 = self.susceptible_dynamics(increment * s2 / 2.0, increment * i2 / 2.0)
        i3 = self.infectious_dynamics(increment * s2 / 2.0, increment * i2 / 2.0)
        r3 = self.recovered_dynamics(increment * i2 / 2.0, increment * r2 / 2.0)
        n3 = self.population_dynamics(increment * n2 / 2.0)

        s4 = self.susceptible_dynamics(increment * s3, increment * i3)
        i4 = self.infectious_dynamics(increment * s3, increment * i3)
        r4 = self.recovered_dynamics(increment * i3, increment * r3)
        n4 = self.population_dynamics(increment * n3 / 2.0)

        self.susceptible_data.append(self.susceptible_data[-1] + (increment / 6.0) * (s1 + (2.0 * s2) + (2.0 * s3) + s4))
        self.infectious_data.append(self.infectious_data[-1] + (increment / 6.0) * (i1 + (2.0 * i2) + (2.0 * i3) + i4))
        self.recovered_data.append(self.recovered_data[-1] + (increment / 6.0) * (r1 + (2.0 * r2) + (2.0 * r3) + r4))
        self.population_data.append(self.population_data[-1] + (increment / 6.0) * (n1 + (2.0 * n2) + (2.0 * n3) + n4))

        self.susceptible_fraction_data.append(self.susceptible_data[-1] / self.population_data[-1])
        self.infectious_fraction_data.append(self.infectious_data[-1] / self.population_data[-1])
    
    # method that integrates the system with Runge-Kutta's method
    # and stores the output into the data lists
    def compute(self, time_step: float):
        # clearing the data lists
        self.susceptible_data.clear()
        self.infectious_data.clear()
        self.recovered_data.clear()
        self.population_data.clear()

        self.susceptible_fraction_data.clear()
        self.infectious_fraction_data.clear()
        
        self.time_data.clear()

        # setting the timeline to zero
        time = 0.0

        # adding the initial data
        self.susceptible_data.append(float(self.susceptible))
        self.infectious_data.append(float(self.infectious))
        self.recovered_data.append(float(self.recovered))
        self.population_data.append(float(self.initial_population))

        self.susceptible_fraction_data.append(self.susceptible_fraction)
        self.infectious_fraction_data.append(self.infectious_fraction)

        self.time_data.append(time)

        # performing the calculation
        while (time <= self.observation_time):
            time += time_step
            self.Runge_Kutta_fourth_order(time_step)
            self.time_data.append(time)