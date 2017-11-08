class DRESummary:
    def __init__(self, monthly_reports):
        self.monthly_reports = monthly_reports

    @property
    def sales(self):
        return sum(report.sale for report in self.monthly_reports)

    @property
    def pointz_sales(self):
        return sum(report.pointz_sale for report in self.monthly_reports)

    @property
    def cost(self):
        return sum(report.base_coin_cost for report in self.monthly_reports)

    @property
    def pointz_percentage(self):
        return round(self.pointz_sales * 100 / self.sales)

    @property
    def cost_percentage(self):
        return round(self.cost * 100 / (self.sales + self.pointz_sales))
