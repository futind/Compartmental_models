

class SIR_model:
    def __init__(self, S: int, I: int, R: int, N:int , beta: float, gamma: float):

        # This assertions are preliminary
        # TO DO: Raise ValueErrors if the values are wrong and handle it with messageBoxes
        assert S >= 0, f"Suseptible {S} can not be less than 0"
        assert I >= 0, f"Infectious {I} can not be less than 0"
        assert R >= 0, f"Recovered {R} can not be less than 0"
        assert N > 0, f"Total number {N} can not be less or equal to 0"
        assert beta >= 0, f"Contact rate {beta} can not be less than 0"
        assert gamma >= 0, f"Recovery rate {gamma} can not be less than 0"

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
    
    # Getter for infectious fraction
    @property
    def infectious_fraction(self):
        return self.__infectious_fraction
    
    # Setter for infectious (I)
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
        if (beta < 0):
            raise ValueError()
        else:
            self.__contact_rate = beta
    
    # Getter for recovery rate (gamma)
    @property
    def recovery_rate(self):
        return self.__recovery_rate

    # Setter for recovery rate (gamma)
    @recovery_rate.setter
    def recovery_rate(self, gamma):
        if (gamma < 0):
            raise ValueError()
        else:
            self.__recovery_rate = gamma
    
    
            

        
    

    
    # return Mu*N - Beta * S * I / N - Mu * S;
    # return Beta * S * I / N - Gamma * I - Mu * I;
    # return Gamma * I - Mu * R;
