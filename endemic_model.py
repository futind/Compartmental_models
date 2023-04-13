from epidemic_model import SIR_model

class SIR_vitality(SIR_model):
    instances = []

    def __init__(self, incidence: bool, S: int, I: int, R: int, N: int, T:int,
                 beta: float, gamma: float, mu: float, nu: int):
        
        assert mu > 0, f'ValueError: {mu} can not be less than zero'
        assert nu >= 0, f'ValueError: {nu} can not be less or equal to zero'

        super().__init__(incidence, S, I, R, N, beta, gamma, T)

        self.__mortality_rate = mu

        self.__total_births = nu

        self.population_data = list()

        self.refresh_r0()

        self.instances.append(self)

        print(f'VITALITY: {self.instances}')
    
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
            self.refresh_r0()
    
    # Getter for total births
    @property
    def total_births(self):
        return self.__total_births
    
    # Setter for total births
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
    # NO SETTER FOR IT IS NEEDED, THIS VALUE MUST BE CALCULATED

    def refresh_r0(self):
        nu = self.total_births
        mu = self.mortality_rate
        beta = self.contact_rate
        gamma = self.recovery_rate

        if (self.mass_action_incidence):
            self.__basic_reproduction_number = ( nu * beta ) / ( mu * (gamma + mu) )
        else:
            self.__basic_reproduction_number = beta / ( gamma + mu )

    def suseptible_dynamics(self, S_inc = 0.0, I_inc = 0.0, N_inc = 0.0):
        mass_action = self.mass_action_incidence
        
        beta = self.contact_rate
        nu = self.total_births
        mu = self.mortality_rate

        S = self.suseptible_data[-1] + S_inc
        I = self.infectious_data[-1] + I_inc
        N = self.population_data[-1] + N_inc

        if (mass_action):
            return nu - beta * I * S - mu * S
        else:
            return nu - beta * I * S / N - mu * S


    def infectious_dynamics(self, S_inc = 0.0, I_inc = 0.0, N_inc = 0.0):
        mass_action = self.mass_action_incidence

        beta = self.contact_rate
        gamma = self.recovery_rate
        mu = self.mortality_rate

        S = self.suseptible_data[-1] + S_inc
        I = self.infectious_data[-1] + I_inc
        N = self.population_data[-1] + N_inc

        if (mass_action):
            return beta * I * S - gamma * I - mu * I
        else:
            return beta * I * S / N - gamma * I - mu * I

    def recovered_dynamics(self, I_inc = 0.0, R_inc = 0.0):
        gamma = self.recovery_rate
        mu = self.mortality_rate

        I = self.infectious_data[-1] + I_inc
        R = self.recovered_data[-1] + R_inc

        return gamma * I - mu * R 

    def population_dynamics(self, N_inc = 0.0):
        nu = self.total_births
        mu = self.mortality_rate
        N = self.population_data[-1] + N_inc

        return nu - mu * N

    def Runge_Kutta_fourth_order(self, increment: float):
        s1 = self.suseptible_dynamics()
        i1 = self.infectious_dynamics()
        r1 = self.recovered_dynamics()
        n1 = self.population_dynamics()

        s2 = self.suseptible_dynamics(increment * s1 / 2.0, increment * i1 / 2.0)
        i2 = self.infectious_dynamics(increment * s1 / 2.0, increment * i1 / 2.0)
        r2 = self.recovered_dynamics(increment * i1 / 2.0, increment * r1 / 2.0)
        n2 = self.population_dynamics(increment * n1 / 2.0)

        s3 = self.suseptible_dynamics(increment * s2 / 2.0, increment * i2 / 2.0)
        i3 = self.infectious_dynamics(increment * s2 / 2.0, increment * i2 / 2.0)
        r3 = self.recovered_dynamics(increment * i2 / 2.0, increment * r2 / 2.0)
        n3 = self.population_dynamics(increment * n2 / 2.0)

        s4 = self.suseptible_dynamics(increment * s3, increment * i3)
        i4 = self.infectious_dynamics(increment * s3, increment * i3)
        r4 = self.recovered_dynamics(increment * i3, increment * r3)
        n4 = self.population_dynamics(increment * n3 / 2.0)

        self.suseptible_data.append(self.suseptible_data[-1] + (increment / 6.0) * (s1 + (2.0 * s2) + (2.0 * s3) + s4))
        self.infectious_data.append(self.infectious_data[-1] + (increment / 6.0) * (i1 + (2.0 * i2) + (2.0 * i3) + i4))
        self.recovered_data.append(self.recovered_data[-1] + (increment / 6.0) * (r1 + (2.0 * r2) + (2.0 * r3) + r4))
        self.population_data.append(self.population_data[-1] + (increment / 6.0) * (n1 + (2.0 * n2) + (2.0 * n3) + n4))

        self.suseptible_fraction_data.append(self.suseptible_data[-1] / self.population_data[-1])
        self.infectious_fraction_data.append(self.infectious_data[-1] / self.population_data[-1])
    
    def compute(self, time_step: float):
        self.suseptible_data.clear()
        self.infectious_data.clear()
        self.recovered_data.clear()
        self.population_data.clear()

        self.suseptible_fraction_data.clear()
        self.infectious_fraction_data.clear()
        
        self.time_data.clear()

        time = 0.0

        self.suseptible_data.append(float(self.suseptible))
        self.infectious_data.append(float(self.infectious))
        self.recovered_data.append(float(self.recovered))
        self.population_data.append(float(self.total_population))

        self.suseptible_fraction_data.append(self.__suseptible_fraction)
        self.infectious_fraction_data.append(self.infectious_fraction)

        self.time_data.append(time)

        while (time <= self.observation_time):
            time += time_step
            self.Runge_Kutta_fourth_order(time_step)
            self.time_data.append(time)
    
