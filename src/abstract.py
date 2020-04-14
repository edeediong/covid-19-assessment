"""Peforms all calculations for the tasks in the Andela BuildforSDG challenge 1-3."""

class Calculate:
    """Calculates everything following guidelines in assessment."""
    def __init__(self, data):
        self.data = data
        self.impact = data["reportedCases"] * 10
        self.severe = data["reportedCases"] * 50
        self.estimator = self.solution()

    def period(self):
        """Converts the timeToElapse and periodType to days"""
        period_type = self.data["periodType"]
        actual_period = self.data["timeToElapse"]
        if period_type == "days":
            return actual_period
        if period_type == "weeks":
            return actual_period * 7
        return actual_period * 30

    def infections_time(self):
        """Shows the infections doubles every three days."""
        impact = self.impact * (2 ** (self.period()//3))
        severe = self.severe * (2 ** (self.period()//3))
        return (impact, severe)

    def severe_infections(self):
        """Shows Severe positive cases that will require hospitalization
            to recover."""
        impact = int(15 / 100 * self.infections_time()[0])
        severe = int(15 / 100 * self.infections_time()[1])
        return (impact, severe)

    def hospital_beds(self):
        """Determines the number of available beds."""
        impact = int((35 / 100 * self.data["totalHospitalBeds"]) - self.severe_infections()[0])
        severe = int((35 / 100 * self.data["totalHospitalBeds"]) - self.severe_infections()[1])
        return (impact, severe)

    def icu_cases(self):
        """Represents the estimated number of severe positive cases
            that will require ICU care."""
        impact = int(5 / 100 * self.infections_time()[0])
        severe = int(5 / 100 * self.infections_time()[1])
        return (impact, severe)

    def ventilator_cases(self):
        """Represents the estimated number of severe positive cases
            that will require ventilators."""
        impact = int(2 /100 * self.infections_time()[0])
        severe = int(2 / 100 * self.infections_time()[1])
        return (impact, severe)

    def dollars_flight(self):
        """Represents the estimate how much money the economy is
            likely to lose daily."""
        avg_income_usd = self.data["region"]["avgDailyIncomeInUSD"]
        avg_income_pop = self.data["region"]["avgDailyIncomePopulation"]
        impact = int(self.infections_time()[0] * avg_income_usd * avg_income_pop\
            * self.period())
        severe = int(self.infections_time()[0] * avg_income_usd * avg_income_pop\
            * self.period())
        return (impact, severe)

    def solution(self):
        """Displays the result in the defined data structure."""
        result = {
            "data": self.data,
            "impact": {
                "currentlyInfected": self.impact,
                "infectionsByRequestedTime": self.infections_time()[0],
                "severeCasesByRequestedTime": self.severe_infections()[0],
                "hospitalBedsByRequestedTime": self.hospital_beds()[0],
                "casesForICYByRequestedTime": self.icu_cases()[0],
                "casesForVentilatorsByRequestedTime": self.ventilator_cases()[0],
                "dollarsInFlight": self.dollars_flight()[0]
            },
            "severeImpact": {
                "currentlyInfected": self.severe,
                "infectionsByRequestedTime": self.infections_time()[1],
                "severeCasesByRequestedTime": self.severe_infections()[1],
                "hospitalBedsByRequestedTime": self.hospital_beds()[1],
                "casesForICYByRequestedTime": self.icu_cases()[1],
                "casesForVentilatorsByRequestedTime": self.ventilator_cases()[1],
                "dollarsInFlight": self.dollars_flight()[1]
            }
        }
        return result
