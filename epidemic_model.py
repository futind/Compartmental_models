class SIR_model:
    # A list, which contains all the instaces of a class
    instances = []
    def __init__(self, incidence: bool, S: int, I: int, R: int, N:int, beta: float, gamma: float, T:int):

        # This assertions are preliminary
        # TO DO: Raise ValueErrors if the values are wrong and handle it with messageBoxes
        assert S >= 0, f"Suseptible {S} can not be less than 0"
        assert I >= 0, f"Infectious {I} can not be less than 0"
        assert R >= 0, f"Recovered {R} can not be less than 0"
        assert N > 0, f"Total number {N} can not be less or equal to 0"
        assert beta >= 0, f"Contact rate {beta} can not be less than 0"
        assert gamma >= 0, f"Recovery rate {gamma} can not be less than 0"

        # If mass_action_incidence = True, then using mass action law incidence
        # Else if mass_action_incidence = False using standard incidence
        self.__mass_action_incidence = incidence

        # Total number (N)
        self.__total_population = N
        
        # Suseptible (S)
        self.__suseptible = S
        self.__suseptible_fraction = S/N

        # Infectious (I)
        self.__infectious = I
        self.__infectious_fraction = I/N

        # Recovered (R)
        self.__recovered = R
        self.__recovered_fraction = R/N

        # Contact rate (beta)
        self.__contact_rate = beta
        
        # Recovery rate (gamma)
        self.__recovery_rate = gamma

        # Time of observation in days(T)
        self.__observation_time = T

        # The basic reproduction number, one of most important
        # threshold qualities of an infection 
        self.__basic_reproduction_number = self.contact_rate / self.recovery_rate

        # Lists that hold the computation data
        # They are needed so we don't have to compute
        # every time we want to 
        self.suseptible_data = list()
        self.infectious_data = list()
        self.recovered_data = list()

        self.time_data = list()

        self.suseptible_fraction_data = list()
        self.infectious_fraction_data = list()
        
        # Adding a created instance into a list of all instances
        SIR_model.instances.append(self)

        print(f'CLASSIC: {self.instances}')
    
    # Adding a representation of our class
    def __repr__(self):
        return f'SIR(S = {self.suseptible}, I = {self.infectious}, R ={self.recovered}, ' \
               f'N = {self.total_population}, beta = {self.contact_rate}, gamma = {self.recovery_rate}), '\
               f'T = {self.observation_time})'
    
    # Getter for incidence
    @property
    def mass_action_incidence(self):
        return self.__mass_action_incidence
    
    # Setter for incidence
    @mass_action_incidence.setter
    def mass_action_incidence(self, incidence: bool):
        self.__mass_action_incidence = incidence

    # Getter for total population (N)
    @property
    def total_population(self):
        return self.__total_population
    
    # Setter for total population (N)
    @total_population.setter
    def total_population(self, N):
        # If total population is less or equal to 0 raising a ValueError
        if (N <= 0):
            raise ValueError()
        else:
            self.__total_population = N
            self.refresh_r0()
    
    # Getter for suseptible (S)
    @property
    def suseptible(self):
        return self.__suseptible
    
    # Getter for suseptible fraction (s)
    @property
    def suseptible_fraction(self):
        return self.__suseptible_fraction

    # Setter for suseptible (S)
    @suseptible.setter
    def suseptible(self, S):
        if (S < 0) | (S > self.__total_population):
            raise ValueError()
        else:
            self.__suseptible = S
            self.__suseptible_fraction = self.__suseptible / self.__total_population

    # Getter for infectious (I)
    @property
    def infectious(self):
        return self.__infectious
    
    # Getter for infectious fraction (i)
    @property
    def infectious_fraction(self):
        return self.__infectious_fraction
    
    # Setter for infectious (I)
    @infectious.setter
    def infectious(self, I):
        if (I < 0) | (I > self.__total_population):
            raise ValueError()
        else:
            self.__infectious = I
            self.__infectious_fraction = self.__infectious / self.__total_population
    
    # Getter for recovered (R)
    @property
    def recovered(self):
        return self.__recovered
    
    # Getter for recovered fraction
    @property
    def recovered_fraction(self):
        return self.__recovered_fraction

    # Setter for recovered (R)
    @recovered.setter
    def recovered(self, R):
        if (R < 0) | (R > self.__total_population):
            raise ValueError()
        else:
            self.__recovered = R
            self.__recovered_fraction = self.__recovered / self.__total_population
    
    # Getter for contact rate (beta)
    @property
    def contact_rate(self):
        return self.__contact_rate
    
    # Setter for contact rate (beta)
    @contact_rate.setter
    def contact_rate(self, beta):
        if (beta <= 0):
            raise ValueError()
        else:
            self.__contact_rate = beta
            self.refresh_r0()
    
    # Getter for recovery rate (gamma)
    @property
    def recovery_rate(self):
        return self.__recovery_rate

    # Setter for recovery rate (gamma)
    @recovery_rate.setter
    def recovery_rate(self, gamma):
        if (gamma <= 0):
            raise ValueError()
        else:
            self.__recovery_rate = gamma
            self.refresh_r0()
    
    # Getter for time of observation (T)
    @property
    def observation_time(self):
        return self.__observation_time
    
    # Setter for time of observation (T)
    @observation_time.setter
    def observation_time(self, T):
        if (T <= 0):
            raise ValueError()
        else:
            self.__observation_time = T
    
    # Getter for basic reproduction number (R0)
    @property
    def basic_reproduction_number(self):
        return self.__basic_reproduction_number
    # NO SETTER FOR IT IS NEEDED, THIS VALUE MUST BE CALCULATED
    
    # Method for refreshing basic reproduction number
    def refresh_r0(self):
        
        beta = self.contact_rate
        gamma = self.recovery_rate
        N = self.total_population

        if (gamma <= 0) | (beta < 0) | (N <= 0):
            raise ValueError()

        if (self.mass_action_incidence):
            self.__basic_reproduction_number = beta * N / gamma
        else:
            self.__basic_reproduction_number = beta / gamma
    
    # All this equations are used in the Runge-Kutta's method, hence the increments
    # Dynamics equation for suseptible compartment (dS/dt basically)
    def suseptible_dynamics(self, S_inc = 0.0, I_inc = 0.0):
        mass_action = self.mass_action_incidence

        beta = self.contact_rate

        S = self.suseptible_data[-1] + S_inc
        I = self.infectious_data[-1] + I_inc
        N = self.total_population

        if (mass_action):
            return ( - beta * I * S )
        else:
            return ( - beta * I * S / N )
    
    # Dynamics equation for infectious compartment (dI/dt)
    def infectious_dynamics(self, S_inc = 0.0, I_inc = 0.0):
        mass_action = self.mass_action_incidence

        beta = self.contact_rate
        gamma = self.recovery_rate

        S = self.suseptible_data[-1] + S_inc
        I = self.infectious_data[-1] + I_inc
        N = self.total_population

        if (mass_action):
            return ( beta * I * S - gamma * I )
        else:
            return ( beta * I * S / N - gamma * I )

    # Dynamics equation for recovered compartment (dR/dt)
    def recovered_dynamics(self, I_inc = 0.0, R_inc = 0.0):
        gamma = self.recovery_rate

        I = self.infectious_data[-1] + I_inc

        return gamma * I
    
    def Runge_Kutta_fourth_order(self, increment):
        s1 = self.suseptible_dynamics()
        i1 = self.infectious_dynamics()
        r1 = self.recovered_dynamics()

        s2 = self.suseptible_dynamics(increment * s1 / 2.0, increment * i1 / 2.0)
        i2 = self.infectious_dynamics(increment * s1 / 2.0, increment * i1 / 2.0)
        r2 = self.recovered_dynamics(increment * i1 / 2.0, increment * r1 / 2.0)

        s3 = self.suseptible_dynamics(increment * s2 / 2.0, increment * i2 / 2.0)
        i3 = self.infectious_dynamics(increment * s2 / 2.0, increment * i2 / 2.0)
        r3 = self.recovered_dynamics(increment * i2 / 2.0, increment * r2 / 2.0)

        s4 = self.suseptible_dynamics(increment * s3, increment * i3)
        i4 = self.infectious_dynamics(increment * s3, increment * i3)
        r4 = self.recovered_dynamics(increment * i3, increment * r3)

        self.suseptible_data.append(self.suseptible_data[-1] + (increment / 6.0) * (s1 + (2.0 * s2) + (2.0 * s3) + s4))
        self.infectious_data.append(self.infectious_data[-1] + (increment / 6.0) * (i1 + (2.0 * i2) + (2.0 * i3) + i4))
        self.recovered_data.append(self.recovered_data[-1] + (increment / 6.0) * (r1 + (2.0 * r2) + (2.0 * r3) + r4))

        self.suseptible_fraction_data.append(self.suseptible_data[-1] / self.total_population)
        self.infectious_fraction_data.append(self.infectious_data[-1] / self.total_population)
    
    # method which actually uses Runge-Kutta's fourth order numerical method
    # for integration 
    def compute(self, time_step: float):
        self.suseptible_data.clear()
        self.infectious_data.clear()
        self.recovered_data.clear()
        
        self.suseptible_fraction_data.clear()
        self.infectious_fraction_data.clear()
        
        self.time_data.clear()

        time = 0.0

        self.suseptible_data.append(float(self.suseptible))
        self.infectious_data.append(float(self.infectious))
        self.recovered_data.append(float(self.recovered))

        self.suseptible_fraction_data.append(self.suseptible_fraction)
        self.infectious_fraction_data.append(self.infectious_fraction)

        self.time_data.append(time)

        while (time <= self.observation_time):
            time += time_step
            self.Runge_Kutta_fourth_order(time_step)
            self.time_data.append(time)

            
    