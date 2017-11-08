from decimal import Decimal


def _to_decimal(number_or_none):
    if number_or_none is None:
        return None
    return Decimal(number_or_none)


class MonthlyReport:
    def __init__(self, month=None, year=None, sale=None, pointz_sale=None, base_coin_cost=None):
        self.base_coin_cost = base_coin_cost
        self.pointz_sale = pointz_sale
        self.sale = sale
        self.year = year
        self.month = month

    @property
    def base_coin_cost(self):
        return self._base_coin_cost

    @base_coin_cost.setter
    def base_coin_cost(self, value):
        self._base_coin_cost = _to_decimal(value)

    @property
    def pointz_sale(self):
        return self._pointz_sale

    @pointz_sale.setter
    def pointz_sale(self, value):
        self._pointz_sale = _to_decimal(value)

    @property
    def sale(self):
        return self._sale

    @sale.setter
    def sale(self, value):
        self._sale = _to_decimal(value)

    @property
    def header(self):
        return f'{self.month}-{self.year}'

    @property
    def pointz_percentage(self):
        return round(self.pointz_sale * 100 / self.sale)

    @property
    def cost_percentage(self):
        return round(self.base_coin_cost * 100 / (self.sale + self.pointz_sale))

    @classmethod
    def create_from_dct(cls, dct):
        report = cls()
        for key in 'pointz_sale sale year month'.split():
            setattr(report, key, dct[key])

        return report
