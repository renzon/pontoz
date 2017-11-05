class MonthlyReport:
    def __init__(self, month, year):
        self.year = year
        self.month = month

    @property
    def header(self):
        return f'{self.month}-{self.year}'


