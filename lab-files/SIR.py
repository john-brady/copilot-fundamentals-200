class SIRModel:
    def __init__(self, susceptible, infected, recovered):
        self.susceptible = susceptible
        self.infected = infected
        self.recovered = recovered

    def update(self, transmission_rate, recovery_rate):
        new_infected = transmission_rate * self.susceptible * self.infected
        new_recovered = recovery_rate * self.infected

        self.susceptible -= new_infected
        self.infected += new_infected - new_recovered
        self.recovered += new_recovered

    def status(self):
        return self.susceptible, self.infected, self.recovered